import os 
import sys 
import shutil
import traceback
import zipfile

import pdb
pdb.set_trace()
try:
    # for utc support
    import pytz 
    from dateutil import tz
    
except ImportError:
    if sys.platform.startswith("win"):
        try:
            pytz_cmd = "pip install pytz --proxy http://proxy-us.intel.com:911"
            date_util_cmd = "pip install python-dateutil --proxy http://proxy-us.intel.com:911"
            os.system(pytz_cmd)
            os.system(date_util_cmd)

        except ImportError:
            print("-W- No pytz module imported: " + pytz_cmd)
            print("-W- No pytz module imported: " + date_util_cmd)

        except:
            print(traceback.print_exc())
    else:
        try:
            pytz_cmd = "sudo pip install pytz --proxy http://proxy-us.intel.com:911"
            date_util_cmd = "sudo pip install python-dateutil --proxy http://proxy-us.intel.com:911"
            os.system(pytz_cmd)
            os.system(date_util_cmd)

        except ImportError:
            print("-W- No pytz module imported: " + pytz_cmd)
            print("-W- No pytz module imported: " + date_util_cmd)

        except:
            print(traceback.print_exc())

def getfilepath(filepath):
    #ToDo: get the file path
    return filepath
import glob 
def openandreadlogs():
    # ToDO: read the logs to be pushed
    # zip_path = getfilepath(os.getcwd())
  
    local_test_dir = os.path.join(os.environ["APPDATA"], "FastLog") \
            if sys.platform.startswith("win") else os.path.join(os.environ['HOME'], ".ctf", "FastLog")
    zip_path = local_test_dir

    # entries = os.listdir(zip_path)
    # print(entries)
    final_dest = os.path.join(os.environ["APPDATA"], "elk") \
            if sys.platform.startswith("win") else os.path.join(os.environ['HOME'], ".ctf", "FastLog")
    # os.mkdir(final_dest)    
    
    # fast_context_dict = {}
    # for dir in os.listdir(zip_path):
    #     if not dir.endswith('.html.zip') and dir.endswith('.zip'):
    #         zip_dir = zip_path + '/'+ dir
    #         with zipfile.ZipFile(zip_dir, "r") as f:
    #                 for name in f.namelist():
    #                     if 'runner.log' in name:
    #                         data = f.read(name).decode('utf-8')
    #                         fast_context_dict['Source log dir'] = \
    #                         find("Source                    :.*", data, re.M)[0].split("Source                    :")[
    #                             1].strip()
    #                         fast_context_dict['local log dir'] = \
    #                         find("Local Drive Destination   :.*", data, re.M)[0].split("Local Drive Destination   :")[
    #                             1].strip()
    #                         fast_context_dict['Shared log dir'] = \
    #                         find("Shared Drive Destination  :.*", data, re.M)[0].split("Shared Drive Destination  :")[
    #                             1].strip()
    #                         fast_context_dict['Test suite RunTime'] = find("Time  :.*", data, re.M)[0].split("Time  :")[
    #                             1].strip()
    # print(fast_context_dict)
            

openandreadlogs()











