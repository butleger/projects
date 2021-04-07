#include <iostream>
#include <iterator>
#include <algorithm>
#include <boost/lambda/lambda.hpp>
using namespace std;

int main()
{
	using namespace boost::lambda;
	typedef std::istream_iterator<int> in;
	std::for_each( in(std::cin), in(), std::cout << (_1 * 3) << " " );
}
