#include "uoj_judger.h"
#include <limits>

struct SpjPointInfo  {
	int num;
	int scr;
	int ust, usm;
	string info, in, out, res, testsrc;

	SpjPointInfo(const int &_num, const int &_scr,
			const int &_ust, const int &_usm, const string &_info,
			const string &_in, const string &_out, const string &_res, const string &_testsrc)
			: num(_num), scr(_scr),
			ust(_ust), usm(_usm), info(_info),
			in(_in), out(_out), res(_res), testsrc(_testsrc) {
	}
	SpjPointInfo(const PointInfo &po, const string &_testsrc)
			: num(po.num), scr(po.scr),
			ust(po.ust), usm(po.usm), info(po.info),
			in(po.in), out(po.out), res(po.res), testsrc(_testsrc) {
	}
};
	
void add_spjpoint_info(const SpjPointInfo &info) {
	if (info.num >= 0) {
		if(info.ust >= 0) {
			tot_time += info.ust;
		}
		if(info.usm >= 0) {
			max_memory = max(max_memory, info.usm);
		}
	}
	tot_score += info.scr;

	details_out << "<test num=\"" << info.num << "\""
		<< " score=\"" << info.scr << "\""
		<< " info=\"" << htmlspecialchars(info.info) << "\""
		<< " time=\"" << info.ust << "\""
		<< " memory=\"" << info.usm << "\">" << endl;
	if(!info.in.empty()) details_out << "<in>" << htmlspecialchars(info.in) << "</in>" << endl;
	if(!info.out.empty()) details_out << "<out>" << htmlspecialchars(info.out) << "</out>" << endl;
	if(!info.res.empty()) details_out << "<res>" << htmlspecialchars(info.res) << "</res>" << endl;
	if(!info.testsrc.empty()){
		details_out << "<h4>" << htmlspecialchars("command") << "</h4>" << endl;
		details_out << "<pre>" << htmlspecialchars(info.testsrc) << "</pre>" << endl;
	}
	details_out << "</test>" << endl;
}

RunCompilerResult custom_compile(vector<string> _argv)
{
	vector<string> argv;
	argv.push_back("--type=compiler");
	argv.push_back(string("--work-path=") + work_path);
	for(auto s: _argv){
		argv.push_back(s);
	}

	RunResult ret = vrun_program(
			(result_path + "/run_compiler_result.txt").c_str(),
			"/dev/null",
			"stderr",
			(result_path + "/compiler_result.txt").c_str(),
			RL_COMPILER_DEFAULT,
			argv);
	RunCompilerResult res;
	res.type = ret.type;
	res.ust = ret.ust;
	res.usm = ret.usm; 
	res.succeeded = ret.type == RS_AC && ret.exit_code == 0;
	if (!res.succeeded) {
		if (ret.type == RS_AC) {
			res.info = file_preview(result_path + "/compiler_result.txt", 500);
		} else if (ret.type == RS_JGF) {
			res.info = "No Comment";
		} else {
			res.info = "Compiler " + info_str(ret.type);
		}
	}
	return res;
}

bool check_gcc_num(string text, int num, string &info)
{
	stringstream ss(text);
	
	int cnt = 0;
	while(ss){
		string firstword;
		ss >> firstword;
		if(firstword == "g++" || firstword == "gcc" || firstword == "ld") cnt++;
		ss.ignore(numeric_limits<streamsize>::max(), '\n');
	}
	if(num == cnt){
		info = "ok";
		return true;
	}else{
		info = "expected " + vtos(num) + " g++, but " + vtos(cnt) + " found\n" + htmlspecialchars(text);
		return false;
	}
}
bool check_file_exist(int i, string &info){
	executef("cd %s; ls > %s", escapeshellarg(work_path).c_str(), escapeshellarg(result_path + "/filelist.txt").c_str());
	ifstream ansin((data_path + "/output" + vtos(i) + ".txt").c_str()); 
	set<string> assertfile, banfile;
	while(true){
		if(!ansin) end_judge_judgement_failed("Can't find answer file.");
		string tmp;
		ansin >> tmp;
		if(tmp == "EOL") break;
		assertfile.insert(tmp);
	}
	while(true){
		if(!ansin) end_judge_judgement_failed("Can't find answer file.");
		string tmp;
		ansin >> tmp;
		if(tmp == "EOL") break;
		banfile.insert(tmp);
	}

	ifstream outin((result_path + "/filelist.txt").c_str()); 
	while(outin){
		string tmp;
		outin >> tmp;
		if(banfile.count(tmp) > 0){
			info = "find unexpected " +  tmp;
			return false;
		}
		assertfile.erase(tmp);
	}
	if(assertfile.empty()){
		info = "ok";
		return true;
	}else{
		info = "didn't find " + *assertfile.begin();
		return false;
	}
}

int main(int argc, char **argv) {
	judger_init(argc, argv);

	report_judge_status_f("Judging #1");
		
	//make
	vector<string> arglist;
	arglist.push_back("/usr/bin/make");
	string extrainfo = "make";
	int i = 1;
	RunCompilerResult c_ret = custom_compile(arglist);
	string chkinfo;
	if (!c_ret.succeeded) {
		SpjPointInfo po(i, 0, 0, 0, "Make Error", "", "", c_ret.info, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}else if(check_file_exist(1, chkinfo)){
		SpjPointInfo po(i, 25, 0, 0, 
				"Accepted",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
	}else{
		SpjPointInfo po(i, 0, 0, 0, 
				"Wrong Answer",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}
	
	report_judge_status_f("Judging #2");
	executef("echo %s >> %s", escapeshellarg("//append some text").c_str(), escapeshellarg(work_path + "/sum.cpp").c_str());
	extrainfo = "echo '//append some text' >> sum.cpp; make";
	i = 2;
	c_ret = custom_compile(arglist);
	if (!c_ret.succeeded) {
		SpjPointInfo po(i, 0, 0, 0, "Make Error", "", "", c_ret.info, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}else if(check_file_exist(i, chkinfo) && check_gcc_num(file_preview(result_path + "/compiler_result.txt", 500), 2, chkinfo)){
		SpjPointInfo po(i, 25, 0, 0, 
				"Accepted",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
	}else{
		SpjPointInfo po(i, 0, 0, 0, 
				"Wrong Answer",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}
	
	report_judge_status_f("Judging #3");
	executef("echo %s >> %s", escapeshellarg("//append some text").c_str(), escapeshellarg(work_path + "/functions.h").c_str());
	extrainfo = "echo '//append some text' >> functions.h; make";
	i = 3;
	c_ret = custom_compile(arglist);
	if (!c_ret.succeeded) {
		SpjPointInfo po(i, 0, 0, 0, "Make Error", "", "", c_ret.info, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}else if(check_file_exist(i, chkinfo) && check_gcc_num(file_preview(result_path + "/compiler_result.txt", 500), 4, chkinfo)){
		SpjPointInfo po(i, 25, 0, 0, 
				"Accepted",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
	}else{
		SpjPointInfo po(i, 0, 0, 0, 
				"Wrong Answer",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}
	
	report_judge_status_f("Judging #4");
	arglist.push_back("clean");
	extrainfo = "make clean";
	i = 4;
	c_ret = custom_compile(arglist);
	if (!c_ret.succeeded) {
		SpjPointInfo po(i, 0, 0, 0, "Make Error", "", "", c_ret.info, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}else if(check_file_exist(i, chkinfo)){
		SpjPointInfo po(i, 25, 0, 0, 
				"Accepted",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
	}else{
		SpjPointInfo po(i, 0, 0, 0, 
				"Wrong Answer",
				"", "", chkinfo, extrainfo);
		add_spjpoint_info(po);
		end_judge_ok();
	}
	
	end_judge_ok();
}
