#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int ws(const string& s) {
    int w = 0;
    for (int j = 0; j < s.size(); ++j) {
        w += ((j % 2 == 0 ? 1 : -1) * (s[j] - 'a'));
    }
    return w;
}

int cws(string s) {
    int count = 0;
    sort(s.begin(), s.end());
    do {
        if (ws(s) > 0) {
            ++count;
        }
    } while (next_permutation(s.begin(), s.end()));
    return count;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        string s;
        cin >> s;
        cout << cws(s) << endl;
    }
    return 0;
}
