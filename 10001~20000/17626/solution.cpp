# include <iostream>
# include <vector>
# include <cmath>

using namespace std;

int solution(int N) {
    vector<int> four_squares(N + 1);
    int a = sqrt(N);
    for (int i = 0; i < a + 1; i++){
        four_squares[i * i] = 1;
        for (int j = i*i + 1; j < (i+1)*(i+1) && j < N + 1; j++) {
            int cnt = 3;
            for (int k = 1; k <= i; k++){
                int tmp = four_squares[j - k * k];
                cnt = tmp < cnt ? tmp : cnt;
            }

            four_squares[j] = cnt + 1;
        }
    }
    
    return four_squares[N];
}

int main(void) {
    int N;
    cin >> N;
    cout << solution(N) << endl;
}