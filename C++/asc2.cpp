#include <iostream>
using namespace std;

int main(){
	int n;
	char c;
	for(n = 32; n < 127; n++){
		c = char(n);
		cout<< n << "=" << c << " ";
		if (n % 10 == 0)cout<<"\n";
		
	}
	return 0;
}
// I dont remember what this program does 
