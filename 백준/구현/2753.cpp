#include <iostream>
using namespace std;

// 2753 윤년
// https://www.acmicpc.net/problem/2753

int main(void) {
	int N = 0;
	cin >> N;
	
	if (N % 4 == 0) {
		// 4의 배수이면
		if (N % 100 != 0 || N % 400 == 0) {
			// 100의 배수가 아니거나, 400의 배수일때
			cout << 1 << endl;
			return 0;
		}
		cout << 0 << endl;
		return 0;
	}
	cout << 0 << endl;

	return 0;



}
