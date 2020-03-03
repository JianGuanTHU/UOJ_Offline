# UOJ_Offline

###出题流程：

- 在本项目issues中提出proposal。需要写一个简略的题目描述，列出考查的知识点。可以提供部分代码或样例数据。因为可能会被建议修改，为减轻大家工作量，不需要将题目完全完善。

- 提醒助教确认。助教会根据情况提出修改意见。如果不太符合课程需要，可能会要求大幅度修改或重新提proposal。通过proposal的同学可以确定免去当次作业。

- 按下述使用步骤完成题面、数据、标答和judger。若有人工评分，需要具体给出评分点。

###使用步骤：

- 将题目按照`./data/`中样题的格式放进`./data`文件夹中
- 将`./submission.conf`中的`problem_id`改为你出的题目号（如31）
- 执行`make`，重新编译输出各个`checker`的可执行文件
- 执行`bash ./run.sh`（执行之前请将`run.sh`中第一行的`path`改为你的文件夹存放的绝对路径，注意路径中不要有中文，运行此脚本需要`python2`环境），该脚本会将题目文件夹中的`submit`、`require`、`Makefile`、`judger`等文件复制到`./work`文件夹下，然后进行评测，评测结果会输出到`./result`文件夹中。

###文件说明：

- `./data`：题目文件夹，其中应包括：

  - `download`文件夹中的文件供做题同学下载；
  - `require`文件夹中的文件是评测提交代码时所需的文件；
  - `submit`文件夹中的内容为标准提交答案；
  - 输入文件、输出文件
  - `judger`：评测文件，具体见下方Judger系统说明
  - `problem.conf`文件中定义了一些评测参数：
    - n_tests: 测试点数
    - execute_name: 执行文件名
    - time_limit: 时间限制
    - memory_limit: 空间限制
    - input_pre/input_suf/output_pre/output_suf: 输入/输出文件前缀/后缀
    - use_builtin_checker: 系统提供的比较答案是否正确的checker（具体cheker名可见`./builtin/checker`文件夹下，如`lcmp`要求全匹配，`rncmp`要求浮点数误差范围内匹配等）

- `./work`：评测时所用的工作文件夹，每次评测前都会清空原有内容

- `./result`：评测结果输出的文件夹，每次评测前都会清空原有内容

  - `checker_error.txt`：每个测试点的评测结果输出文件
  - `compiler_result.txt`：编译错误输出文件
  - `cur_status.txt`：评测状态文件
  - `result.txt`：评测完成后的输出文件

- `./builtin`：包含了系统提供的多种`checker`

- `./include`：包含编译`checker`所需的头文件

- `Makefile`：编译`./builtin`中的`checker`

- `submission.conf`：包含`problem_id`等评测参数

- `find_problem_id.py`：供`run.sh`查询评测题目id使用

- Judger系统：

  - `uoj_judger_compiler.py`,` uoj_judger_config.py`,` uoj_judger_reporter.py`,` uoj_judger_tester.py`，judger工作时需要的头文件，分别提供了编译、参数配置、结果输出、代码评测功能，不要修改。

  - `judger`：出题时需要针对不同题目分别编写的评测文件

    ```python
    main_path = sys.argv[1] #主文件夹，当前文件
    work_path = sys.argv[2] #./work
    result_path = sys.argv[3] #./result
    data_path = sys.argv[4] #./data/31
    
    C = pyjudgerConfig(main_path, work_path, result_path, data_path)	#配置参数类
    n = int(C.config["n_tests"])	#测试点数
    R = pyjudgerReporter(C, n)	#结果输出类
    Co = pyjudgerCompiler(C)	#编译类
    T = pyjudger_custom_tester(C)	#测试类，必要时可在judger文件中重写该类
    ```

###注意：

- 对于不同的题目，你只需增加`data`文件夹下的题目，其他文件不要改动。在写judeger时可参考样题，其中样题的judger分别有以下特征：
  - 24：标准judger
  - 19：重写Executer
  - 22：重写checker
  - 25：选择题
  - 37：重写整个tester+子任务
- 项目中`./work`、`./result`、题目中`submit`、`require`、`download`等空文件夹未显示，运行脚本时将自动处理，无需手动创建；
- 样题均未提供标准答案（包括人工评分标准），如有需要，可联系助教；
- 该项目仅供测试judger使用，未加入测试内存、时间使用情况等功能，且不能明确具体的错误类型，除了编译错误外其他错误均显示为Wrong Answer；
- 如对项目代码疑问，请联系关健（邮箱：j-guan19@mails.tsinghua.edu.cn）。