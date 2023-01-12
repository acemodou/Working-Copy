from os import path
import requests
import json
import os
from getpass import getpass
from pathlib import Path
import time
import datetime
import sys


if __name__=='__main__':
    configdir = input('Type in config dir:')
    elk_config_filepath = os.path.join(configdir, "logsource_elk_config.json")
    elk_config_filepath_secret = os.path.join(configdir, "logsource_elk_config_secret.json")
else:
    from config import elk_config_filepath, elk_config_filepath_secret

def initialize(args = None):
    """
    Brief:
        initialize(args) - Initializes elk login info and elk url

    Description: - Initializes elk login info and elk url.  This enables the other methods to access the elk server.

    Argument(s):
        args - Arguments passed in via cmd line args

    Return Value(s):
        None

    Example:
        elk.initialize(args)

    Related: - NA

    Author(s):
        Timothy Darrow
    """
    global elk_password
    global elk_user
    global elk_server_url
    if args != None and args.elklogin and args.elkpw: # check for cmd line args
        elk_user = args.elklogin
        elk_password = args.elkpw
    else: #attempt to load values from config json
        try:
            with open(elk_config_filepath_secret) as file:
                elkConfigJson = json.load(file)
                elk_user = elkConfigJson["user"]
                elk_password = elkConfigJson["password"]
        except:
            sys.stderr.write(F"Failed to load ELK configuration from {elk_config_filepath_secret}\n")
    
    if args != None and args.elkurl: # check for cmd line arg
        elk_server_url = args.elkurl
    else: # Attempt to load value from config json
        _load_elk_server_config()
        
    if not (elk_user and elk_password and elk_server_url): # if we were unable to get needed variables we need to get them from the user or fail if in noninteractive
        if args != None and args.nonInteractive:
            sys.stderr.write(F"Logsource Elk configuration is incomplete. Please validate elk info\n")
            exit(1)
        else:# get the missing values from the user
            if not elk_server_url:
                elk_server_url = input("Please enter the logsource ELK server address: ")
            if not elk_user:
                elk_user = input("Please enter the logsource ELK username: ")
            if not elk_password:
                elk_password = getpass("Logsource ELK Password: ")

def _load_elk_server_config():
    """
    Description: 
    Loads elk server configuration to appropriate global variables. Currently only loaded configuration item is url of 
    elk server and the only affected variable is elk_server_url. Modifies global variables!
    Logs error message to stderr on failure. 
 
    Argument(s):
        None
        
    Return Value(s):
        None
 
    Example:
        _load_elk_server_config()
    """
    global elk_server_url
    
    try:
        with open(elk_config_filepath) as file:
            elkConfigJson = json.load(file)
            elk_server_url = elkConfigJson["serverUrl"]
    except:
        sys.stderr.write(F"Failed to load ELK configuration from {elk_config_filepath}\n")
