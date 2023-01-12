import json
import sys
import os 
class WorkflowTask:
    def __init__(self):
        self.taskType = None # A string: the type of the task, e.g. "DockerBuildTaskResult"
        self.taskId = None # A string: the name of the task, e.g. "Memory consumption delta <Product Name>"
        self.status = None # A string: PASSED/FAILED/etc.
        self.quickbuildBuildId = None # An integer, represents this task's build ID.
        self.taskJson = None # A json object/Python dictionary storing just this task's entry in the original workflow execution result json.
        self.errorDetectionProcessable = True # A boolean: If we should be able to get the logs and run error detection on this task.
        self.tidbitTag = None # A string: If this is a test subtask, then this is the associated tidbits tag all the tests were run under.
        self.isATestSubtask = None # A boolean: True if this is a test subtask (links out to Quickbuild or Valet...), false otherwise

    def initializeFromJsonObject(self, jsonDictionary, isATestSubtask = False):
        # Parameter: jsonDictionary is the dictionary that has only this JSON object's data...

        if jsonDictionary is None:
            sys.stderr.write("[WorkflowTask::initializeFromJsonObject] ERROR: No JSON object provided!")
            return False

        self.taskJson = jsonDictionary
        self.isATestSubtask = isATestSubtask

        if isATestSubtask:
            self.errorDetectionProcessable = False
            self.taskType = "TestTaskResult"
        else:
            if "type" in jsonDictionary:
                self.taskType = jsonDictionary["type"]
            else:
                sys.stderr.write("WARNING: WorkflowTask::initializeFromJsonObject(): Failed to find 'type' field\n")
                return False

        if isATestSubtask:
            if "name" in jsonDictionary:
                self.taskId = jsonDictionary["name"]
            else:
                sys.stderr.write("WARNING: WorkflowTask::initializeFromJsonObject(): Failed to find 'name' field for test subtask\n")
                return False
        else:
            if "taskId" in jsonDictionary:
                self.taskId = jsonDictionary["taskId"]
            else:
                sys.stderr.write("WARNING: WorkflowTask::initializeFromJsonObject(): Failed to find 'taskId' field\n")
                return False

        if "status" in jsonDictionary:
            self.status = jsonDictionary["status"]
        else:
            sys.stderr.write("WARNING: WorkflowTask::initializeFromJsonObject(): Failed to find 'status' field\n")
            return False

        if self.taskType == "TriggerQuickbuildConfigurationTaskResult":
            buildIdFieldName = "buildId"
        else:
            buildIdFieldName = "quickbuildBuildId"
        
        if buildIdFieldName in jsonDictionary:
            self.quickbuildBuildId = jsonDictionary[buildIdFieldName]
        else:
            sys.stderr.write(F"WARNING: WorkflowTask::initializeFromJsonObject(): Failed to find '{buildIdFieldName}' field\n")
            self.errorDetectionProcessable = False
            # Don't return false, because actually...we can theoretically process these anyway, and only show them in the failure list, since it is available in the CI environment (even though our Bench tests won't be able to get this info from ELK -- ELK doesn't have all tasks, it only has build subtasks. No test/tidbits subtasks...)...

        if isATestSubtask:
            if "tidbitTag" in jsonDictionary:
                self.tidbitTag = jsonDictionary["tidbitTag"]
            else:
                sys.stderr.write("WARNING: WorkflowTask::initializeFromJsonObject(): Failed to find 'tidbitTag' field for test subtask\n")
                return False

        return True

class WorkflowExecution:
    def __init__(self):
        self.buildId = None
        self.author = None # A string, the PR author's name.
        self.authorEmail = None # A string
        self.requester = None # A string, the Workflow requester's name.
        self.requesterEmail = None # A string
        self.buildUrl = None # A string, link to the workflow on Quickbuild.
        self.workflowType = None # A string: BUILD/BUILDTEST/etc
        self.pullRequestId = None # An integer, links to the bitbucket pull request that this build originates from...
        self.quickbuildProject = None # A string. It's the Quickbuild workflow configuration name for SSDDEV. In NSG, we had just "ssddev" as an option. With the NPSG-IOG split, IOG moved to "ssddev-optane" for this field.
        self.repoName = None # A string, the bitbucket repository that this build originates from...
        self.subtasks = list() # A list of WorkflowTask objects.
        self.workflowJson = None # Internal data-structure; a json object (i.e. a Python dictionary)

    
    def loadJson(self, filepath):
        try:
            with open(filepath) as file:
                self.workflowJson = json.load(file)
        except:
            sys.stderr.write(F"WorkflowExecutionStructure::loadJson(): Failed to load workflow execution result json \"{filepath}\"\n")
            return False
          # 1) Load the build metadata we're interested in from the top of the JSON.
        if "buildId" in self.workflowJson:
            self.buildId = self.workflowJson["buildId"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'buildId' field in workflow execution result JSON\n")
            return False

        if "author" in self.workflowJson:
            self.author = self.workflowJson["author"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'author' field in workflow execution result JSON\n")
            return False

        if "requester" in self.workflowJson:
            self.requester = self.workflowJson["requester"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'requester' field in workflow execution result JSON\n")
            return False

        if "authorEmail" in self.workflowJson:
            self.authorEmail = self.workflowJson["authorEmail"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'authorEmail' field in workflow execution result JSON\n")
            return False

        if "requesterEmail" in self.workflowJson:
            self.requesterEmail = self.workflowJson["requesterEmail"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'requesterEmail' field in workflow execution result JSON\n")
            return False

        if "buildUrl" in self.workflowJson:
            self.buildUrl = self.workflowJson["buildUrl"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'buildUrl' field in workflow execution result JSON\n")
            return False

        if "workflowType" in self.workflowJson:
            self.workflowType = self.workflowJson["workflowType"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'workflowType' field in workflow execution result JSON\n")
            return False

        if "pullRequestId" in self.workflowJson:
            self.pullRequestId = self.workflowJson["pullRequestId"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'pullRequestId' field in workflow execution result JSON\n")
            return False

        if "project" in self.workflowJson:
            self.quickbuildProject = self.workflowJson["project"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'project' field in workflow execution result JSON\n")
            return False

        if "repoName" in self.workflowJson:
            self.repoName = self.workflowJson["repoName"]
        else:
            sys.stderr.write("WorkflowExecutionStructure::loadJson(): Failed to find 'repoName' field in workflow execution result JSON\n")
            return False
        
         # 2) Iterate over the tasks list and load all the subtasks into our internal data-structures.
        i = 0
        for task in self.workflowJson["taskResults"]:
            if task["type"] == "BuildThenTidbitTestTaskResult":
                for buildTaskResult in task["buildTaskResults"]:
                    subtask = WorkflowTask()

                    if (subtask.initializeFromJsonObject(buildTaskResult)):
                        self.subtasks.append(subtask)
                        i += 1
                    else:
                        sys.stderr.write(F"WARNING: WorkflowExecutionStructure::loadJson(): Skipping invalid task entry {i}\n")
                        i += 1
                        continue
                for testTaskResult in task["testPlanStageResults"]:
                    subtask = WorkflowTask()

                    testPlanStageName = task["taskId"]

                    if (subtask.initializeFromJsonObject(jsonDictionary = testTaskResult, isATestSubtask = True)):
                        subtask.taskId = F"{testPlanStageName}/{subtask.taskId}"
                        self.subtasks.append(subtask)
                        i += 1
                    else:
                        sys.stderr.write(F"WARNING: WorkflowExecutionStructure::loadJson(): Skipping invalid task entry {i}\n")
                        i += 1
                        continue
            else:
                subtask = WorkflowTask()

                if (subtask.initializeFromJsonObject(task)):
                    self.subtasks.append(subtask)
                    i += 1
                else:
                    sys.stderr.write(F"WARNING: WorkflowExecutionStructure::loadJson(): Skipping invalid task entry {i}\n")
                    i += 1
                    continue

        return True




work_flow_data = WorkflowExecution()
file_path = "C:/SRC/Working-Copy/DataStructures/v1/jedAI/WorkflowExecutionResult.json"

work_flow_data.loadJson(file_path)
print(work_flow_data.requester)
