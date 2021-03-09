#coding=utf-8
import os
class pyjudgerConfig:
	def __init__(self, main_path, work_path, result_path, data_path):
		self.config = dict()

		def load_config(config_file):
			configs = open(config_file, 'r').readlines()
			for each_config in configs:
				key, value = each_config.strip('\n').strip('\r').split(' ')
				self.config[key] = value

		self.main_path = main_path
		self.work_path = work_path
		self.result_path = result_path
		load_config(self.work_path + "/submission.conf")
		self.problem_id = self.config['problem_id']
		self.data_path = data_path
		load_config(self.data_path + "/problem.conf")
		self.exec_file_name = "./main"

		#exec("cp %s/require/* %s 2>/dev/null"%(self.__data_path, self.__work_path))

		#这里可以修改
		if "use_builtin_checker" in self.config:
			self.config["checker"] = self.main_path + "/builtin/checker/" + self.config["use_builtin_checker"]
		else:
			self.config["checker"] = self.data_path + "/chk"
		self.config["validator"] = self.data_path + "/val"

		#os.chdir(self.work_path)
