#coding=utf-8
import judger_class_lib as lib

class pyjudgerCompiler(object):
	def __init__(self, config):
		self.config = config

	def run_compiler(self, path, arg):
		argv = ["--type=compiler", "--work-path=" + path]
		argv.extend(arg)

		ret = lib.run_program( \
			main_path=self.config.main_path, \
			result_file_name=self.config.result_path + "/run_compiler_result.txt", \
			input_file_name="/dev/null", \
			output_file_name="stderr", \
			error_file_name=self.config.result_path + "/compiler_result.txt", \
			limit=lib.RL_COMPILER_DEFAULT, \
			para_list=argv)
		res = lib.RunCompilerResult(type=ret.type, ust=ret.ust, usm=ret.usm, \
					succeeded=(ret.type == lib.RS_AC) and (ret.exit_code == 0))
		if not res.succeeded:
			if res.type == lib.RS_AC:
				res.info = lib.file_preview(self.config.result_path + "/compiler_result.txt", 500)
			elif res.type == lib.RS_JGF:
				res.info = "Compiler Dangerous System Call"
			else:
				res.info = "Compiler " + lib.info_str(res.type)
		print(res.info.encode("utf-8"))
		return res

	def compile_cpp(self, name, path=None):
		path = path or self.config.work_path
		argv = ["/usr/bin/g++", "-o", name, "-x", "c++", "answer.code", "-std=c++11", "-lm", "-O2", "-DONLINE_JUDGE"]
		return self.run_compiler(path, argv)

	def compile_command(self, para, path=None):
		path = path or self.config.work_path
		argv = para.split(' ')
		return self.run_compiler(path, argv)

	def compile(self, para):
		name = para
		if name + '_language' in self.config.config:
			lang = self.config.config[name + '_language']
			print("has a language :", lang.encode("utf-8"))
			#TODO check language type
			return self.compile_cpp(name)
		else:
			return self.compile_cpp(name)

# if __name__ == "__main__":
# 	def test():
# 		C = pyjudgerConfig()
# 		os.chdir(C.work_path)
# 		my_compiler = pyjudgerCompiler(C)
# 		#以下是两种编译方法
# 		#1. 默认编译
# 		my_compiler.compile("main")
# 		#2. 使用 g++ 或者 g++-4.8 或者直接用 /usr/bin/g++-4.8
# 		#my_compiler.custom_compile("g++ -o main -x c++ main.code -lm -O2 -DONLINE_JUDGE")
# 	test()
