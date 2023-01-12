import json
import sys
import os
import config
from getpass import getpass
import requests


bitbucket_password = None
bitbucket_user = None
bitbucket_server_url = ""

tidbits_server_url = ""
quick_build_server_url = ""

def initialize(args):
    
    if not _load_bitbucket_server_config(args):
        sys.stderr.write("Failed to configure bitbucket module!\n")
        exit(3) # TODO: Really should make this a non-fatal error...lodge a complaint, but don't abort the entire program. Just disable the failing module.
    if not _load_tidbits_server_config(args):
        sys.stderr.write("Failed to configure bitbucket module!\n")
        exit(3) # TODO: Really should make this a non-fatal error...lodge a complaint, but don't abort the entire program. Just disable the failing module.
    if not _load_quick_build_server_config(args):
        sys.stderr.write("Failed to configure bitbucket module!\n")
        exit(3) # TODO: Really should make this a non-fatal error...lodge a complaint, but don't abort the entire program. Just disable the failing module.

def _load_bitbucket_server_config(args):
    """
    Description: 
    Loads bitbucket server configuration to appropriate global variables. Currently only loaded configuration item is 
    url of bitbucket server and the only affected variable is bitbucket_server_url. Modifies global variables!
    Logs error message to stderr on failure. 
 
    Argument(s):
        args    - dict: a list of commandline arguments passed to JedAI
        
    Return Value(s):
        True if success
        False if failure
 
    Example:
        _load_bitbucket_server_config(args)
    """
    global bitbucket_server_url
    global bitbucket_password
    global bitbucket_user

    if args.bblogin and args.bbpw:
        bitbucket_user = args.bblogin 
        bitbucket_password = args.bbw 
    else:
        try:
            with open(config.bit_bucket_secret_filepath) as file:
                bitbucketConfigJson = json.load(file)
                bitbucket_user = bitbucketConfigJson["user"]
                bitbucket_password = bitbucketConfigJson["password"]
        except:
            sys.stderr.write("Failed to load Bitbucket configuration from bitbucket_config_secret.json!\n")

    if not (bitbucket_user and bitbucket_password): # if bitbucket data has not been set then we ask the user to input it if not in noninteractive
        if args.nonInteractive:
            sys.stderr.write(F"Bitbucket login data is incomplete.  Please validate Bitbucket info\n")
            exit(1)
        else:
            if not bitbucket_user:
                bitbucket_user = input("Please enter the bitbucket username: ")
            if not bitbucket_password:
                bitbucket_password = getpass("Password: ")
    
    # (1) First, try to load the setting from the commandline.
    # (2) If not present, then try to load it from the config file.
    # (3) If even that fails, then try to prompt the user for it, if not in non-interactive mode.
    
    if args.bitbucket_server_url is not None:
        # (1) Set the parameter from the commandline.
        bitbucket_server_url = args.bitbucket_server_url
    else:
        try:
            with open(config.bitbucket_config_filepath) as file:
                # (2) Set the parameter from the config file.
                bitbucket_config_json = json.load(file)
                bitbucket_server_url = bitbucket_config_json["server_url"]
        except:
            sys.stderr.write(F"Failed to load Bitbucket configuration from {config.bitbucket_config_filepath}\n")
            if args.nonInteractive:
                sys.stderr.write("Unrecoverable error. Aborting Bitbucket server URL load.\n")
                return False
            else:
                # (3) Prompt the user for the parameter.
                bitbucket_server_url = input("Please enter the Bitbucket server URL for JedAI to post comments to:")
                
    return True


def _load_tidbits_server_config(args):
    """
    Description: 
    Loads tidbits server configuration to appropriate global variables. Currently only loaded configuration item is 
    url of tidbits server and the only affected variable is tidbits_server_url. Modifies global variables! 
    Logs error message to stderr on failure.
 
    Argument(s):
        args    - dict: a list of commandline arguments passed to JedAI
        
    Return Value(s):
        True if success
        False if failure
 
    Example:
        _load_tidbits_server_config(args)
    """
    global tidbits_server_url
    
    # (1) First, try to load the setting from the commandline.
    # (2) If not present, then try to load it from the config file.
    # (3) If even that fails, then try to prompt the user for it, if not in non-interactive mode.
    
    if args.tidbits_server_url is not None:
        # (1) Set the parameter from the commandline.
        tidbits_server_url = args.tidbits_server_url
    else:
        try:
            with open(config.tidbits_config_filepath) as file:
                # (2) Set the parameter from the config file.
                tidbits_config_json = json.load(file)
                tidbits_server_url = tidbits_config_json["server_url"]
        except:
            sys.stderr.write(F"Failed to load Tidbits configuration from {config.tidbits_config_filepath}\n")
            if args.nonInteractive:
                sys.stderr.write("Unrecoverable error. Aborting Tidbits server URL load.\n")
                return False
            else:
                # (3) Prompt the user for the parameter.
                tidbits_server_url = input("Please enter the Tidbits server URL for JedAI to link to:")

    return True


def _load_quick_build_server_config(args):
    """
    Description: 
    Loads Quick Build server configuration to appropriate global variables. Currently only loaded configuration item is 
    url of Quick Build server and the only affected variable is quick_build_server_url. Modifies global variables!
    Logs error message to stderr on failure. 
 
    Argument(s):
        args    - dict: a list of commandline arguments passed to JedAI
        
    Return Value(s):
        True if success
        False if failure
 
    Example:
        _load_quick_build_server_config(args)
    """
    global quick_build_server_url
    
    # (1) First, try to load the setting from the commandline.
    # (2) If not present, then try to load it from the config file.
    # (3) If even that fails, then try to prompt the user for it, if not in non-interactive mode.
    
    if args.quickbuild_server_url is not None:
        # (1) Set the parameter from the commandline.
        quick_build_server_url = args.quickbuild_server_url
    else:
        try:
            with open(config.quick_build_config_filepath) as file:
                # (2) Set the parameter from the config file.
                quick_build_config_json = json.load(file)
                quick_build_server_url = quick_build_config_json["server_url"]
        except:
            sys.stderr.write(F"Failed to load Quick Build configuration from {config.quick_build_config_filepath}\n")
            if args.nonInteractive:
                sys.stderr.write("Unrecoverable error. Aborting Quickbuild server URL load.\n")
                return False
            else:
                # (3) Prompt the user for the parameter.
                quick_build_server_url = input("Please enter the Quickbuild server URL for JedAI to link to:")

    return True
    
def postCommentOnPR(comment_text, pull_request_id, repo_name, project):
    pull_request_url = F"{bitbucket_server_url}/rest/api/1.0/projects/{project}/repos/{repo_name}/pull-requests/{pull_request_id}/comments"

    headers = {'content-type': 'application/json'}

    comment_json = json.dumps({'text': comment_text})

    response = requests.post(pull_request_url, verify = False, auth = (bitbucket_user, bitbucket_password), headers = headers, data = comment_json)

    if response.status_code == 201:
        print(F"Successfully posted comment to pull request {pull_request_id}, at URL {pull_request_url}.")
    else:
        sys.stderr.write(F"ERROR: Failed to create comment! URL: {pull_request_url}\n")
        sys.stderr.write(F"Received response: \"{response}\" \n")

    return response

def bitbucketCommentFailureAnalysis(repo_name, project, workflow_data, jedaiQuickbuildID):
    """
    Description: Generates the Bitbucket comment with the JedAI report:
     * What targets failed?
     * Useful links (like the quickbuild submission link)
     * Attached detail error report

    Argument(s):
        repo_name           -   string:                     The Bitbucket repository for the pull request.
        project             -   string:                     The Bitbucket project for the pull request.
        workflow_data       -   WorkflowExecutionStructure  Contains all of the metadata for the workflow, and sub-datastructures containing all subtask metadata.
        jedaiQuickbuildID   -   int:                        The Quickbuild workflow that ran JedAI.

        # TODO: Maybe create a design flowchart highlighting the difference between the failingTargetsList, and the "otherFailingTargets", and how the failingTargetsList gets split up into two categories technically: targets we processed, and targets we didn't process for whatever reason.

    Return Value(s):
        N/A

    Example:
        <ADD EXAMPLES HERE>
    """

    detailedErrorHtmlURL = F"{quick_build_server_url}/download/{jedaiQuickbuildID}/artifacts/data/builds/{workflow_data.buildId}/reports/{workflow_data.buildId}-error-report.html"

    workflow_type = workflow_data.workflowType
    if workflow_data.workflowType is None:
        # Default initialization for this parameter if not specified.
        sys.stderr.write("[generateSummaryReportHtml()] WARNING: No workflowType specified.\n")
        workflow_type = ""

    maintainerString = "For any issues, questions, or concerns regarding JedAI, please reach out to us: \n"
    for maintainer in config.maintainersList:
        maintainerString += F"{maintainer}\n"

    failing_build_subtasks = workflow_data.getTasksByCriteria(criteria = [("status", "FAILED"), ("errorDetectionProcessable", [True])])
    failing_other_subtasks = workflow_data.getTasksByCriteria(criteria = [("status", "FAILED"), ("errorDetectionProcessable", [False])])

    if (len(failing_build_subtasks) == 0) and (len(failing_other_subtasks) == 0):
        comment = """\
JedAI did not detect failed build subtasks in your {workflow_type} workflow submission [{workflow_data.buildId}]({workflow_data.buildUrl}), were the failures perhaps in a test subtask or in the parent workflow itself?

Please check Quickbuild: {workflow_data.buildUrl}
""".format(**locals())

        comment += """\


{maintainerString}
        """.format(**locals())

        if jedaiQuickbuildID:
            comment += """\

*[DEBUG: [Click here to view the JedAI Postprocessor Workflow]({qb_url}/build/{jedaiQuickbuildID}/overview)]*
""".format(**locals(), qb_url=quick_build_server_url)

    else:
        
        tableOfContentsForFailingBuildTargets = ""
        targetNum = 0
        # Fill the Table of Contents with one line for every target.
        for subtask in failing_build_subtasks:
            tableOfContentsForFailingBuildTargets += F" * {subtask.quickbuildBuildId} - {subtask.taskId}"
            if (subtask.jedai_processing_data.processing_result is not None):
                tableOfContentsForFailingBuildTargets += F" ***(PROCESSING ERROR: {subtask.jedai_processing_data.processing_result})***"
            tableOfContentsForFailingBuildTargets += "\n"
            targetNum = targetNum + 1

        tableOfContentsForOtherFailingTargets = ""
        targetNum = 0
        for subtask in failing_other_subtasks:
            tableOfContentsForOtherFailingTargets += F" * {subtask.taskType} - {subtask.taskId}"
            if subtask.tidbitTag is not None:
                tidbitsUrl = F"{tidbits_server_url}/tidbits/tb_testrunquery.php?tidbit={subtask.tidbitTag}"
                tableOfContentsForOtherFailingTargets += F" *(tidbits tag: [{subtask.tidbitTag}]({tidbitsUrl})*)"
            tableOfContentsForOtherFailingTargets += "\n"
            targetNum += 1

        # Actual comment's contents.
        comment = """\
JedAI has detected the following failures in {workflow_type} workflow submission [{workflow_data.buildId}]({workflow_data.buildUrl}):

### Failing Build Targets
""".format(**locals())
        
        if len(failing_build_subtasks) == 0:
            comment += """\
JedAI did not find failed build subtasks in your build submission [{workflow_data.buildId}]({workflow_data.buildUrl}/summary), were the failures perhaps in a test subtask or in the parent workflow itself?
            """.format(**locals())
        else:
            comment += """\
Please refer to the following file for a detailed error listing: {detailedErrorHtmlURL}
{tableOfContentsForFailingBuildTargets}
""".format(**locals())

            comment += """\
Note that this version of JedAI does not target test subtasks, please refer to Quickbuild for any such failures: {workflow_data.buildUrl}
""".format(**locals())

        if len(failing_other_subtasks) != 0:
            comment += """\


### Other Failing Targets
JedAI detected the following additional failing tasks with task types not targeted in this version. Please refer to [Quickbuild]({workflow_data.buildUrl}) for these failures.

{tableOfContentsForOtherFailingTargets}
""".format(**locals())

        comment += """\


{maintainerString}
""".format(**locals())

        
        if jedaiQuickbuildID:
            comment += """\


*[DEBUG: [Click here to view the JedAI Postprocessor Workflow]({qb_url}/build/{jedaiQuickbuildID}/overview)]*
""".format(**locals(), qb_url=quick_build_server_url)

    postCommentOnPR(comment, workflow_data.pullRequestId, repo_name, project)


if __name__ == "__main__":
    pr_id = input("Please enter the pull request ID to leave a test comment on: ")
    repo = input("Please enter the repo name to leave a test comment on: ")
    project = input("Please enter the repo project to leave a test comment on: ")
    comment_text = input("What comment would you like to post? ")
    response = postCommentOnPR(pr_id, repo, project)