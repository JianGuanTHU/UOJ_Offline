#include <iostream>

#include "MyList.h"

int main()
{

	MyList x;

#ifdef SUBTASK1
	//subtask 1
	std::cout << x << std::endl;
	for(int i = 0; i < 5; i++)
		x.append(i);
	std::cout << x[0] << std::endl;
	std::cout << x << std::endl;
#endif

#ifdef SUBTASK2
	//subtask 2
	MyList y = x;
	y[0] += 5;
	std::cout << x << std::endl;
#endif

#ifdef SUBTASK3
	//subtask 3
	MyList z = x(1, 3);
	std::cout << z << std::endl;
	z[1] += 5;
	std::cout << z << std::endl;
	std::cout << x << std::endl;
#endif

#ifdef SUBTASK4
	//subtask 4
	MyList r = x(2, 4);
	std::cout << r << std::endl;
	r.append(-1);
	std::cout << r << std::endl;
	std::cout << x << std::endl;
#endif

	return 0;
}
