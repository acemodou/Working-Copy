import os
"""
Description:
    Store configurations for jedAI's usage
"""
configdir =  'config'

# Configuration json filepaths
bitbucket_config_filepath = os.path.join(configdir, "bitbucket_config.json")
elk_config_filepath = os.path.join(configdir, "logsource_elk_config.json")
email_config_filepath = os.path.join(configdir, "email_config.json")
quick_build_config_filepath = os.path.join(configdir, "quickbuild_config.json")
tidbits_config_filepath = os.path.join(configdir, "tidbits_config.json")

# Secret configuration json filepaths i.e. the username and password or any keys
elk_config_filepath_secret = os.path.join(configdir, "logsource_elk_config_secret.json")
bit_bucket_secret_filepath = os.path.join(configdir, "bitbucket_config_secret.json")


shadowProgramUserList = [
    # Team JedAI members
    "ciprian.elies@intel.com",
    "modou.jaw@intel.com",
    "timothy.darrow@intel.com"
]

maintainersList = [
    "ciprian.elies@intel.com",
    "modou.jaw@intel.com",
    "timothy.darrow@intel.com"
]
