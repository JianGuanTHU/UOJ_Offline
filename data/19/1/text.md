### 题目描述

现在已有<samp>main.cpp</samp>、<samp>product.cpp</samp>、<samp>sum.cpp</samp>、<samp>functions.h</samp>四个文件。

文件内容见[下载链接](/download.php?type=problem&id=18)

你需要编写一个<samp>Makefile</samp>文件完成程序的编译过程，要求：

 * 在<samp>linux</samp>系统下，<samp>Makefile</samp>文件能正常运行。（编译器为g++。）

 * 使用<samp>make</samp>命令，能够联合编译多个源文件，最终生成名为<samp>main</samp>的可执行文件。（linux下无exe后缀。）main可以正常执行，其输出请查看示例。

 * 使用<samp>make debug</samp>命令，能够生成开启调试模式的可执行文件，同样生成名为<samp>main</samp>的可执行文件。调试模式的具体输出请查看示例。

 * 使用<samp>make clean</samp>命令，能够清理之前生成的文件，还原成最初的样子。

**注意：你Makefile文件在结束任务后必须返回0。若返回非0值，则认为make失败，评测系统会给出Make Error的提示。**

### 输入样例

```
1 1
```

### 输出样例

```
2
1
```

### 调试模式输入样例

```
1 1
```

### 调试模式输出样例

```
running sum(a = 1, b = 1)
2
running sum(a = 1, b = 1)
1
```

### 提交要求

提交一个<samp>Makefile</samp>文件，满足上述需求。

### 评分标准

OJ自动评测占100%。
