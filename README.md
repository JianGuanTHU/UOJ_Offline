# UOJ_Offline

将题目按照./data/31中的格式放进./data文件夹中，注意事项和说明：

- download文件夹中的内容供做题同学下载；
- require文件夹中的内容为评测做题同学提交的代码时所需的文件；
- submit文件夹中的内容为标准提交答案；
- problem.conf文件中定义了一些评测参数：
  - n_tests: 测试点数
  - execute_name: 执行文件名
  - time_limit: 时间限制
  - memory_limit: 空间限制
  - input_pre/input_suf/output_pre/output_suf: 输入/输出前缀/后缀
  - use_builtin_checker: 系统提供的比较答案是否正确的checker（具体cheker名可见./builtin/checker文件夹下，如lcmp要求全匹配，rncmp要求浮点数误差范围内匹配等）

将./submission.conf中的problem_id改为你出的题目号（如1）

执行make，重新编译输出各个checker的可执行文件

执行bash ./run.sh（执行之前请将run.sh中第一行的path改为你的文件夹存放的绝对位置，注意路径中不要有中文），该脚本会将题目文件夹中的submit、require、Makefile等文件复制到./work文件夹下，然后进行评测，评测结果会输出到./result文件夹中。

注意：

- 对于不同的题目，你只需要写不同的judger，uoj_judger_compiler.py, uoj_judger_config.py, uoj_judger_reporter.py, uoj_judger_tester.py, judger_class_lib.py 这些文件不要改动。
- 该版本的UOJ仅供测试judger使用，未加入测试内存、时间使用情况等功能。
- 如有疑问，请联系关健（微信：13051331318，邮箱：j-guan19@mails.tsinghua.edu.cn）。