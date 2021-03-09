第10课

1. 下面关于模板特化正确的有
   A. 函数模板可以部分特化
   B. 类模板可以全部特化也可以部分特化
   C. 函数模板特化的类型在一些情况下无需指定，可以由编译器自行推导出
   D. 程序在运行时才会选择是使用基础函数模板还是特化的模板

2. 按照C++标准中对vector操作的要求，描述正确的是

```c++
   #include <iostream>
   #include <vector>
   using namespace std;
   
   int main(){
     vector<int> vec = {1,2,3,4,5};
     auto a = vec.end();
     auto b = vec.begin();
     auto c = vec.begin() + 2;
     auto d = vec.erase(vec.begin() + 1);
     return 0;
   }
```

A. 在erase执行前，`a`指向的整型数据的值为5

B. 在main函数返回前，`b`仍然有效，最终指向的整型数据的值为1

C. 在main函数返回前，`c`仍然有效，最终指向的整型数据的值为3

D. 在main函数返回前，`d`仍然有效，最终指向的整型数据的值为2

3. 下列关于STL说法正确的是：

A. list中插入删除操作会使操作位置之后的迭代器失效

B. map中元素的key不可重复

C. set中的元素不是按插入顺序排序，而是按照值排序

D. vector使用insert随机插入元素的平均复杂度为O(1)

第十一课

4.	下列关于string类的说法正确的是

A.	使用循环和operator+拼接string类的多个对象，假设长度为常数，则其时间复杂度与对象个数的平方成正比。

B.	使用string类的优势之一在于string类对象之间可以方便地使用+、==、<、>等运算符进行运算。

C.	string类对象可以通过cin的operator>>从标准输入中输入字符串，直至遇见换行符或文件结束才会停止。

D.	string类对象只能通过迭代器访问元素，不能通过位置索引访问元素


5 下列说法中正确的是

A.	endl可以看作是ostream类的对象，可将其与流运算符搭配将换行符写入输出流并清空缓冲区

B.	ostream类不允许复制，但允许移动

C.	istream和ostream都是iostream的子类，分别继承了输入和输出的功能

D.	stringstream利用对象内部的buffer实现输入和输出，使用clear()函数可以清空buffer


6.	下面关于字符串匹配的说法正确的是

A.	正则表达式``ooo?o?p``能匹配``oop``，而不能匹配``ooop``和``oooop``

B.	正则表达式``-?\d*(\.\d*)?``可以匹配``-1``, ``12.1``，不能匹配``1.``

C.	用正则表达式``([a-z]*)(\d)(?:[A-Z]+) (?:[a-z]*) (\d+)``匹配字符串``0SYYxkk1``，捕获到的分组中2号是0

D.	用正则表达式``^[1-9]\d{0,3}-(1[0-2]|0?[1-9])-(3[01]|[12]\d|0?[1-9])$``可以匹配``2020-5-1``或``2020-05-01``



第十二课

7 关于以下代码，说法正确的是

```
#include <functional>
#include <algorithm>
using namespace std;

bool compPt(int a, int b)
{
	return a < b;
}

class CompCls
{
public:
	bool operator()(int a, int b) const
	{
		return a < b;
	}
};

function<bool(int, int)> fn = compPt;

template<class T, class Compare>
void mysort1(T* first, T* last, Compare comp)
{
	for (auto i = first; i != last; i++)
		for (auto j = i; j != last; j++)
			if (!comp(*i, *j)) swap(*i, *j);
}

template<class T>
void mysort2(T* first, T* last, function<bool(T, T)> comp)
{
	for (auto i = first; i != last; i++)
		for (auto j = i; j != last; j++)
			if (!comp(*i, *j)) swap(*i, *j);
}

int main()
{
	int arr[] = {2, 1, 3, 5, 4};
	//(1)
	return 0;
}
```


A (1)处，如果要调用mysort1，第三个参数可以接受compPt, CompCls()，但不能接受fn。

B (1)处，如果要调用mysort2，第三个参数可以接受compPt, CompCls()和fn。

C mysort1和mysort2的区别在于，comp在mysort1中是早绑定，在mysort2中是晚绑定。

D compPt(1,2) CompCls(1, 2) fn(1,2) 的返回值都是True


8  对于以下代码，正确的有

```
#include <memory>
#include <iostream>
using namespace std;
void f(shared_ptr<int> p1){
    cout << p1.use_count();
    static auto t2 = p1;
}
int main()
{
	int &x = new int(1);
	{
        shared_ptr<int> p1(x);
        f(p1);
        cout << p1.use_count();
        f(p1);
        cout << p1.use_count();
    }
    //(1)
    return 0;
}
```

A 输出是 2232

B 输出是 1222

C 在(1)处，x已经被析构

D 若在(1)处加入``shared_ptr<int> p2(x); ``，则可能导致x被析构两次。


9 关于智能指针的以下说法正确的有

A 当动态创建的对象被多处引用，可以使用shared_ptr自动的管理该对象的销毁

B ``shared_ptr``\``weak_ptr``\``unique_ptr`` 都使用了引用计数的方法，可以通过``use_count``函数访问当前指针的引用计数数量

C ``shared_ptr``可以复制构造、移动构造，但``weak_ptr``和``unique_ptr``只能移动构造，不能复制构造

D 对于会产生引用循环的情况，只要全部使用``weak_ptr``就能解决问题。