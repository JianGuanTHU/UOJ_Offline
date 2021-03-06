#include <iostream>

#include "MyList.h"

int main()
{

	MyList x;

#ifdef SUBTASK1
	//subtask 1
	std::cout << x << std::endl;
	for(int i = 0; i < 100; i++)
		x.append(i);
	for(int i = 0; i < 100; i++)
		std::cout << x[i] << std::endl;
	std::cout << x << std::endl;
#endif

#ifdef SUBTASK2
	//subtask 2
	MyList y = x;
	for(int i = 0; i < 10; i++){
		y[i] += i * 100;
		std::cout << x << std::endl;
	}
#endif

#ifdef SUBTASK3
	//subtask 3
	for(int i = 1; i < 10; i++){
		MyList z = x(i * 10, i * 11 + 1);
		std::cout << z << std::endl;
		for(int j = 0; j <= i; j++){
			z[i] += j;
		}
		std::cout << x << std::endl;
	}
#endif

#ifdef SUBTASK4
	//subtask 4
	for(int i = 1; i < 10; i++){
		MyList r = x(i * 10, i * 11 + 1);
		std::cout << r << std::endl;
		r.append(i);
		std::cout << x << std::endl;
	}
#endif

	return 0;
}
