#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
 
using namespace std;
 
int divide(string arr, int k) {
    if (arr.length() < k) {
        return 0;
    }
     
    vector<int> check(26, 0);
     
    for (char c : arr) {
        check[c - 'a']++;
    }
         
    for (int i = 0; i < arr.length(); i++) {
        if (check[arr[i] - 'a'] < k) {
            int mid = i;
            return max(divide(arr.substr(0, mid), k), divide(arr.substr(mid+1), k));
        }
    }
     
    return arr.length();
}
 
int solve(string arr, int k) {
    return divide(arr, k);
}
 
int main() {
    int T;
    cin >> T;
    cin.ignore();
    for (int i = 0; i < T; i++) {
        string s;
        getline(cin, s);
        int k;
        cin >> k;
        cin.ignore();
         
        int maxLen = solve(s, k);
        cout << maxLen << endl;
    }
    return 0;
}