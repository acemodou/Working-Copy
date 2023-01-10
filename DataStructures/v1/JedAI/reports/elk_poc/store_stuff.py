import sys
import requests , os
import json
import re
from getpass import getpass
from requests.api import request
if __name__=='__main__':
    configdir = input('Type in config dir:')
else:
    from config import configdir

# TODO: Good, small ID to test with:
# 24103342

"""
Interface with JedAI's ELK system to store results.
"""

elk_user = ""
elk_password = ""
config_filename = os.path.join(configdir, "jedai_elk_config.json")
config_filename_secret = os.path.join(configdir, "jedai_elk_config_secret.json")
elkServerUrl = ""

# https://nsg-jira.intel.com/browse/INFS-51012
# https://nsg.elk-champions.intel.com/app/kibana#/home
# https://fmgnsgelk102.fm.intel.com/
# fmgnsgelk102.amr.corp.intel.com [10.4.118.117]
def initialize(args):
    """
    Brief:
        initialize(args) - Initializes elk info for storing data.

    Description: - Initializes elk info.  This enables the other methods to access elk to store data.

    Argument(s):
        args - Arguments passed in via cmd line args

    Return Value(s):
        None

    Example:
        store_stuff.initialize(args)

    Related: - NA

    Author(s):
        Timothy Darrow
    """
    global elk_user
    global elk_password
    global elkServerUrl
    if args.elklogin and args.elkpw and args.elkurl:# check for commandline args
        elk_user = args.elklogin
        elk_password = args.elkpw
        elkServerUrl = args.elkurl
    else:# attempt to load email authentication info from config json
        try:
            with open(config_filename) as file:
                elkConfigJson = json.load(file)
                elkServerUrl = elkConfigJson["serverUrl"]
        except:
            sys.stderr.write(F"Failed to load ELK configuration from {config_filename}!\n")
        try:
            with open(config_filename_secret) as file:
                elkConfigJson = json.load(file)
                elk_user = elkConfigJson["user"]
                elk_password = elkConfigJson["password"]
        except:
            sys.stderr.write(F"Failed to load ELK configuration from {config_filename_secret}!\n")
    if not (elk_user and elk_password and elkServerUrl): # check to make sure elk info is set and if not, then get it from the user if not in noninteractive
        if args.nonInteractive:
            sys.stderr.write("Elk login data is incomplete.  Please validate elk info\n")
            exit(1)
        else:
            if not elk_user:
                elk_user = input("Please enter the JedAI ELK username: ")
            if not elk_password:
                elk_password = getpass("JedAI ELK Password: ")
            if not elkServerUrl:
                elkServerUrl = input("Please enter the JedAI ELK server address: ")
                
    #print(F"Configurations:\n\tserver url = {elkServerUrl}\n\tusername = {elk_user}\n\tpassword = {elk_password}\n")
