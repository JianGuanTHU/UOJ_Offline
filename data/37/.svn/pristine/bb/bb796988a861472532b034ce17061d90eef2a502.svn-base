#coding=utf-8

import os
from uoj_judger_config import *
import judger_class_lib as lib
import traceback

class pyjudger_validator():
	def run(self, config, tester):
		input_file_name = tester.input_file_name
		ret = lib.run_program(
			main_path=config.main_path, \
			result_file_name=config.result_path + "/run_validator_result.txt", \
			input_file_name=input_file_name, \
			output_file_name="/dev/null", \
			error_file_name=config.result_path + "/validator_error.txt", \
			work_path=config.work_path, \
			limit=lib.conf_run_limit('validator', tester.num, lib.RL_VALIDATOR_DEFAULT, config), \
			para_list=[config.config['validator']])
		return lib.RunValidatorResult(type=ret.type, usm=ret.usm, ust=ret.ust, \
									  succeeded=(ret.type==lib.RS_AC and ret.exit_code==0), \
									  info=lib.file_preview(config.result_path + "/validator_error.txt"))

class pyjudger_run_submission_program():

	def run(self, config, tester):
		ret = lib.run_program( \
			main_path=config.main_path, \
			result_file_name=config.result_path + "/run_submission_program.txt", \
			input_file_name=tester.input_file_name, \
			output_file_name=tester.output_file_name, \
			error_file_name="/dev/null", \
			work_path=config.work_path, \
			limit=lib.conf_run_limit("", index=tester.num, val=lib.RL_DEFAULT, config=config), \
			type="default", \
			para_list=[config.exec_file_name])
		if ret.type == lib.RS_AC and ret.exit_code != 0:
			ret.type = lib.RS_RE
		print("run submission program:", ret.type)
		return ret

class pyjudger_run_checker():

	def run(self, config, tester):
		ret = lib.run_program( \
			main_path=config.main_path, \
			result_file_name=config.result_path + "/run_checker_result.txt", \
			input_file_name="/dev/null", \
			output_file_name="/dev/null", \
			error_file_name=config.result_path + "/checker_error.txt", \
			work_path=config.work_path, \
			limit=lib.conf_run_limit("checker", index=tester.num, val=lib.RL_CHECKER_DEFAULT, config=config), \
			readable=[tester.input_file_name, \
					  tester.output_file_name, \
					  tester.answer_file_name], \
			para_list=[config.config['checker'], \
					   os.path.abspath(tester.input_file_name), \
					   os.path.abspath(tester.output_file_name), \
					   os.path.abspath(tester.answer_file_name), \
					   ])
		if ret.type!=lib.RS_AC or ret.exit_code!=0:
			return lib.RunCheckerResult(type=ret.type, usm=ret.usm, ust=ret.ust, scr=0, \
										info=lib.file_preview(config.result_path + "/checker_error.txt"))
		else:
			R = lib.RunCheckerResult(type=ret.type, usm=ret.usm, ust=ret.ust, scr=0, \
									 info=lib.file_preview(config.result_path + "/checker_error.txt"))
			try:
				F = lib.file_preview(config.result_path + "/checker_error.txt")
				R.info = F
				E = F.strip().split(' ')
				if E[0] == "ok":
					R.scr = 100
				elif E[0] == 'points':
					if float(E[1]) != 1:
						return lib.RunCheckerResult(type="RS_JGF", ust=-1, usm=-1, scr=0, info="Checker Judgment Failed")
					else:
						R.scr = (int)(100 * float(E[1]) + 0.5)
				else:
					R.scr = 0
				return R
			except:
				return lib.RunCheckerResult(type="RS_JGF", ust=-1, usm=-1, scr=0, info="Checker Judgment Failed")

class pyjudger_custom_tester():
	def __init__(self, config, validater=None, executer=None, checker=None):
		self.config = config
		self.validater = validater or pyjudger_validator()
		self.executer = executer or pyjudger_run_submission_program()
		self.checker = checker or pyjudger_run_checker()

	def generate_config(self, index):
		def init_file_name(pre, default_pre, index, suf):
			name = ""
			if index < 0:
				name += "ex_"
			name += self.config.config[pre] if (pre in self.config.config) else default_pre
			name += str(abs(index))+"."
			name += self.config.config[suf] if (suf in self.config.config) else "txt"
			return name

		self.input_file_name = \
				self.config.data_path + "/" + init_file_name("input_pre", "input", index, 'input_suf')
		self.output_file_name = \
				self.config.work_path + "/" + init_file_name("output_pre", "output", index, 'output_suf')
		self.answer_file_name = \
				self.config.data_path + "/" + init_file_name("output_pre", "output", index, 'output_suf')
		self.num = index

	def test(self, point_index):
		#init
		self.generate_config(point_index)

		#phase1
		if self.config.config.get('validate_input_before_test') == 'on':
			ok, ret1 = self.run_validator_and_get_result()
			if not ok:
				return lib.PointInfo(point_index, 0, info="validater error", \
					input=lib.file_preview(self.input_file_name))
			if ret1.type != lib.RS_AC:
				return lib.PointInfo(point_index, 0, ust=ret1.ust, usm=ret1.usm, \
					info=ret1.info, input=lib.file_preview(self.input_file_name))

		# phase2
		if self.config.config.get('submit_answer') == 'on':
			ret2 = lib.RunResult(type=lib.RS_AC, ust=-1, usm=-1, exit_code=0)
		else:
			ok, ret2 = self.run_submission_program_and_get_result()
			if not ok:
				return lib.PointInfo(point_index, scr=0, ust=0, usm=0, info="Running Error", \
									input=lib.file_preview(self.input_file_name))
			if 'token' in self.config.config:
				lib.file_hide_token(self.output_file_name, self.config.config['token'])
			if ret2.type != lib.RS_AC:
				print("test:", ret2.info.encode("utf-8"))
				return lib.PointInfo(point_index, 0, ust=ret2.ust, usm=ret2.usm, info=ret2.info, \
									 input=lib.file_preview(self.input_file_name))

		# phase3
		ok, ret3 = self.run_checker_and_get_result()
		if not ok:
			return lib.PointInfo(point_index, 0, info="checker error", \
				input=lib.file_preview(self.input_file_name))
		if ret3.type != lib.RS_AC:
			return lib.PointInfo(point_index, 0, ust=ret2.ust, usm=ret2.usm, \
								info="Checker " + lib.info_str(ret3.type), \
								input=lib.file_preview(self.input_file_name), \
								out=lib.file_preview(self.output_file_name))
		return lib.PointInfo(point_index, \
							 ret3.scr, \
							 usm=ret2.usm, \
							 ust=ret2.ust, \
							 info="Wrong Answer" if ret3.scr == 0 else ("Accepted" if ret3.scr==100 else "Acceptable Answer"), \
							 input=lib.file_preview(self.input_file_name), \
							 out=lib.file_preview(self.output_file_name), \
							 res=ret3.info)

	def run_validator_and_get_result(self):
		try:
			ret = self.validater.run(self.config, self)
			return True, ret
		except:
			traceback.print_exc()
			return False, None

	def run_submission_program_and_get_result(self):
		try:
			ret = self.executer.run(self.config, self)
			return True, ret
		except:
			traceback.print_exc()
			return False, None

	def run_checker_and_get_result(self):
		try:
			ret = self.checker.run(self.config, self)
			return True, ret
		except:
			traceback.print_exc()
			return False, None
