import os

RS_AC = 0
RS_JGF = 7
RS_MLE = 3
RS_TLE = 4
RS_OLE = 5
RS_RE = 2
RS_DGS = 6

class PointInfo:
	def __init__(self, num, scr, ust=0, usm=0 \
				 , info="", input="", out="", res="", extrainfo=""):
		self.num = num
		self.scr = scr
		self.ust = ust
		self.usm = usm
		self.info = info
		self.input = input
		self.output = out
		self.res = res
		self.extrainfo = extrainfo

class RunLimit:
	def __init__(self, time=0, memory=0, output=0):
		self.time = time
		self.memory = memory
		self.output = output

RL_DEFAULT = RunLimit(1, 256, 64)
RL_JUDGER_DEFAULT = RunLimit(600, 1024, 128)
RL_CHECKER_DEFAULT = RunLimit(5, 256, 64)
RL_VALIDATOR_DEFAULT = RunLimit(5, 256, 64)
RL_MARKER_DEFAULT = RunLimit(5, 256, 64)
RL_COMPILER_DEFAULT = RunLimit(15, 512, 64)

class CustomTestInfo:
	def __init__(self, ust=0, usm=0, info="", exp="", out=""):
		self.ust = ust
		self.usm = usm
		self.info = info
		self.exp = exp
		self.out = out

class RunResult:
	#TODO exit_code default is -1?
	def __init__(self, type=0, ust=0, usm=0, exit_code=-1):
		self.type = type
		self.ust = ust
		self.usm = usm
		self.exit_code = exit_code
		
	@property
	def info(self):
		return info_str(self.type)

def RunResult_failed_result():
	return RunResult(type=RS_JGF, ust=-1, usm=-1)

class RunCheckerResult:
	def __init__(self, type=0, ust=0, usm=0, scr=0, info=""):
		self.type = type
		self.ust = ust
		self.usm = usm
		self.scr = scr
		self.info = info

def RunCheckerResult_failed_result():
	return RunCheckerResult(type=RS_JGF, ust=-1, usm=-1, \
							scr=0, info="Checker Judgment Failed")

class RunValidatorResult:
	def __init__(self, type=0, ust=0, usm=0, succeeded=False, info=""):
		self.type = type
		self.ust = ust
		self.usm = usm
		self.succeeded = succeeded
		self.info = info

def RunValidatorResult_failed_result():
	return RunValidatorResult(type=RS_JGF, ust=-1, usm=-1, \
							  succeeded=False, info="Validator Judgment Failed")

class RunCompilerResult:
	def __init__(self, type=0, ust=0, usm=0, succeeded=False, info=""):
		self.type = type
		self.ust = ust
		self.usm = usm
		self.succeeded = succeeded
		self.info = info

def RunCompilerResult_failed_result():
	return RunCompilerResult(type=RS_JGF, ust=-1, usm=-1, \
							 succeeded=False, info="Compile Failed")

def numbers_to_strings(argument):
	switcher = { \
		0: "zero", \
		1: "one", \
		2: "two", \
	}
	return switcher.get(argument, "nothing")

def info_str(id):
	switcher = { \
		RS_MLE: "zero", \
		RS_TLE: "Time Limit Exceeded", \
		RS_OLE: "Output Limit Exceeded", \
		RS_RE: "Runtime Error", \
		RS_DGS: "Dangerous Syscalls", \
		RS_JGF: "Judgement Failed" \
	}
	return switcher.get(id, "nothing")

def escapeshellarg(arg):
	return "'" + arg.replace("\\", "\\\\") + "'"

def run_program(main_path, result_file_name, input_file_name, output_file_name, error_file_name, \
		limit, para_list=None, type=None, work_path=None, readable=None, raw_para=None):

	para_list = para_list or []
	readable = readable or []
	#limit : RunLimit
	command = " ".join([main_path + "/run/run_program", \
						">" + escapeshellarg(result_file_name), \
						"--in=" + escapeshellarg(input_file_name), \
						"--out=" + escapeshellarg(output_file_name), \
						"--err=" + escapeshellarg(error_file_name), \
						"--tl=" + str(limit.time), \
						"--ml=" + str(limit.memory), \
						"--ol=" + str(limit.output), \
						])
	command += " --type=" + str(type) if (type) else ""
	command += " --work-path=" + work_path if (work_path) else ""
	command += " " +  " ".join([" --add-readable=" + each for each in readable])
	command += " " + " ".join([para for para in para_list])
	command += (" " + raw_para) if raw_para else ""
	print "command is : ", command
	try:
		os.system(command)
		#print open(result_file_name,'r').readline()
		data_raw = '\n'.join(open(result_file_name,'r').readline().split(' '))
		data = open(result_file_name,'r').readline().strip().split(' ')
		print("data", data)
		result = RunResult(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
		return result
	except:
		return RunResult_failed_result()

def file_preview(input_file_name, range=100):
	try:
		str = "".join(open(input_file_name, 'r').readlines())
		if len(str) > range * 4:
			return str[:range * 4] + "..."
		else:
			return str
	except:
		return "no such file:"+input_file_name

def file_hide_token(file_name, token):
	# examine token
	try:
		f = open(file_name, "r")
		data = f.read()
		f.close()
		if data[:len(token)] != token:
			raise Exception
		f = open(file_name, "w")
		f.write(data[len(token):])
		f.close()
	except:
		f = open(file_name, "w")
		f.write("Unauthorized output\n")
		f.close()

def conf_run_limit(pre, index, val, config):
	def init_limit(key, default):
		return config.config[key] if key in config.config else default
	if pre == "":
		pre = "_"
	return RunLimit(time=init_limit(pre+"time_limit_" + str(index), val.time), \
					memory=init_limit(pre+"memory_limit_" + str(index), val.memory), \
					output=init_limit(pre+"output_limit_" + str(index), val.output) \
					)

def htmlspecialchars(string=""):
	string = string.replace('&', "&amp;")
	string = string.replace('<', "&lt;")
	string = string.replace('>', "&gt;")
	string = string.replace('"', "&quot;")
	string = string.replace('\0', "<b>\\0</b>")
	return string
