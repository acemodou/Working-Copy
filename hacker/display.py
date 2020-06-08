import os
_SPDK_SETUP_PATH  = "C:/Users/mjaw/Desktop/Personal/gitBase/Working-Copy/Working-Copy/hacker"

def parse_logfile(log):
	""" -----------  -----------"""
	errors = []
	success = []
	with open(log, 'r') as f:
		file_contents = f.read().splitlines()
		for line in file_contents:
			print(line)
			if "ERROR" in line:
				store_new_files = line.split()
				errors.append(store_new_files)
			else:
				store_new_files = line
				success.append(store_new_files)

	if len(errors) > 0:
		# print(F"-I- SPDK status code is :  {errors[0][6]} expected : {errors[0][7]}")
		st1 = "Test Fail".center(100, "=")
		return st1
	else:
		return success



def get_test_runinfo():
	#TODO: Test run info is irrelvant
	# TODO: How can i stop SPDK from printing logs
	_testlog= os.path.abspath(os.path.join(_SPDK_SETUP_PATH, "failog.log"))

	print("-I- Kicking off spdk test execution")
	print(parse_logfile(_testlog))


if __name__=="__main__":
	get_test_runinfo()