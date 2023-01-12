import argparse
import os
import json
import sys 
import reports
import config
from logfetch import elk
from datetime import datetime
from pathlib import Path  

dataDirectory = "data/"
def _load_quick_build_config():
    """
    Description: 
    Loads Quick Build server configuration to appropriate global variables. Currently only loaded configuration item is 
    url of Quick Build server and the only affected variable is quick_build_server_url. Modifies global variables!
    Logs error message to stderr on failure. 
 
    Argument(s):
        None
        
    Return Value(s):
        None
 
    Example:
        _load_quick_build_config()
    """
    global quick_build_server_url
    
    try:
        with open(config.quick_build_config_filepath) as file:
            quick_build_config_json = json.load(file)
            quick_build_server_url = quick_build_config_json["server_url"]
    except:
        sys.stderr.write(F"Failed to load Quick Build configuration from {config.quick_build_config_filepath}\n")
    

def setupBaseOutputDir(args):
    '''
    Setup output directory 
    '''
    global dataDirectory
    global trainingDbBaseDirectory
    if args.out:
        dataDirectory = args.out
    os.chdir('C:/SRC/Working-Copy/DataStructures/v1/JedAi')
    if not os.path.isdir(dataDirectory):
        os.mkdir(dataDirectory)
    trainingDbBaseDirectory = f'{dataDirectory}/passingDatabases'
    return dataDirectory

def start(args):
    '''
    Description:
        Determines which JedAI workflow to run, based on the commandline arguments JedAI was invoked with.
    
    # TODO: If no commandline arguments were given, we could have a cool TUI or GUI or something that interactively works with the user.
    '''
    setupBaseOutputDir(args)
    if args.bitbucket_comment:
        reports.bitbucket.comment.initialize(args)
    if not args.qblogs and not args.useMockLogfetch:
        elk.initialize(args)
    if args.exportToKibana:
        reports.elk_poc.store_stuff.initialize(args)
    _load_quick_build_config()
    jedai_runtime_timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    if not args.depth:
        args.depth = 12 # TODO: Can use a named constant instead. # TODO: Separate it outside of args maybe??

    if args.trainmode:
        Path(trainingDbBaseDirectory).mkdir(parents = True, exist_ok = True)
   

if __name__ =="__main__":
    #TODO: Understand args and implement it for just workflow json
    parser = argparse.ArgumentParser(prog="Jedai", description="A tool to mine any sort of log", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-o", "--output", dest='out', help="output directory")
    parser.add_argument("--workflowExecutionResultJson", dest= "workflowExecutionResultJson")
    parser.add_argument("-pr","--addPrComment", dest= "bitbucket_comment",help = "whether to post the failure analysis to bitbucket", action = 'store_true',
                        default = False)
    parser.add_argument("-bbusername", "--bitbucketUsername", dest = 'bblogin', help = "bitbucket account username")
    parser.add_argument("-bbpw", "--bitbucketPassword", dest = 'bbpw', help = "bitbucket account password, API token, or personal access token")
    parser.add_argument("-bburl", "--bitbucketURL", dest = 'bitbucket_server_url', help = "url for Bitbucket")
    args = parser.parse_args()
    start(args)
