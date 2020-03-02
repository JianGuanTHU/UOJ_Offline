#coding=utf-8
from uoj_judger_config import  *
import judger_class_lib as lib
import fcntl

class pyjudgerReporter:
	def __init__(self, config, test_num):
		self.config = config
		self.tot_time = 0
		self.max_memory = 0
		self.details_out = ""
		self.tot_score = 0
		self.test_num = test_num

	def report_judgement_status(self, info):
		print self.config.result_path+"/cur_status.txt"
		F = open(self.config.result_path+"/cur_status.txt", "w")
		fcntl.flock(F.fileno(), fcntl.LOCK_EX)
		F.write(info[:512])

	def add_point_info(self, info):
		if info.ust >= 0:
			self.tot_time += info.ust
		if info.usm >= self.max_memory:
			self.max_memory = info.usm
		self.details_out += "<test num=\"%u\" score=\"%u\"  info=\"%s\"  time=\"%u\"  memory=\"%u\">"\
				% (info.num, info.scr / self.test_num, info.info, info.ust, info.usm)
		self.tot_score += info.scr
		if info.input:
			self.details_out += "<in>%s</in>" % (lib.htmlspecialchars(info.input))
		if info.output:
			self.details_out += "<out>%s</out>" % (lib.htmlspecialchars(info.output))
		if info.res:
			self.details_out += "<res>%s</res>" % (lib.htmlspecialchars(info.res))
		if info.extrainfo:
			self.details_out += lib.htmlspecialchars(info.extrainfo)
		self.details_out += "</test>\n"

	def add_subtask_info(self, subTaskIndex, scr=0, info="", points=None):
		self.details_out += "<subtask "
		self.details_out += " num=\"%u\" "%subTaskIndex
		self.details_out += " score=\"%u\" "%scr
		self.details_out += " info=\"%s\" "%lib.htmlspecialchars(info)
		self.details_out += " >\n"

		if points:
			for each in points:
				self.add_point_info(each)
		self.details_out += " </subtask>\n"

	def end_judge_ok(self):
		F = open(self.config.result_path+"/result.txt", "w")
		F.write("score %d\n" % (self.tot_score / self.test_num))
		F.write("time %d\n" % self.tot_time)
		F.write("memory %d\n" % self.max_memory)
		F.write("details\n")
		F.write("<tests>\n")
		F.write(self.details_out)
		F.write("</tests>\n")
		F.close()
		exit(0)

	def end_judge_judgement_failed(self, info=""):
		F = open(self.config.result_path+"/result.txt", "w")
		F.write("error Judgment Failed\n")
		F.write("details\n")
		F.write("<error>%s</error>\n" % lib.htmlspecialchars(info))
		F.close()
		exit(0)

	def end_judge_compile_error(self, info=""):
		F = open(self.config.result_path+"/result.txt", "w")
		F.write("error Compile Error\n")
		F.write("details\n")
		F.write("<error>%s</error>\n" % lib.htmlspecialchars(info))
		F.close()
		exit(0)
