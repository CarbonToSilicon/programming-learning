#include <iostream>

int main(int argc, char *argv[])
{
	long long sum = 0;
	int numbers = 5;
	for (int i = 1; i <= numbers; i ++)
	{
	    sum += i;
	}
	std::cout << "Sum = " << sum;
	
	long long sum1 = 0;
	int i = 1;
	while (i <= numbers)
	{
	    sum1 += i;
	    i++;
	}
	std::cout << "\nSum = " << sum1;
}