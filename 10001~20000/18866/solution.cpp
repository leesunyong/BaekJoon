# include <iostream>
# include <vector>
# include <map>

using namespace std;

int main (void) {

    int N;
    cin >> N;

    vector<int> happiness, piro;

    for (int i = 0; i < N; i++) {
        int h, p;
        cin >> h >> p;

        happiness.push_back(h);
        piro.push_back(p);
    }

    int h_max = -1;
    int h_min = 1000000001;
    for (int i = 0; i < N; i++) {
        if (happiness[i] != 0) {
            if (h_min > happiness[i]) {
                h_min = happiness[i];
            } else if (h_min < happiness[i]) {
                if (h_max < happiness[i]) {
                    h_max = happiness[i];
                } else if (h_max > happiness[i]) {
                    break;
                }
            }
        }
    }

    int p_max = -1;
    int p_min = 1000000001;
    for (int i = 0; i < N; i++) {
        if (piro[i] != 0) {
            if (p_max < piro[i]) {
                p_max = piro[i];
            } else if (p_max > piro[i]) {
                if (p_min > piro[i]) {
                    p_min = piro[i];
                } else if (p_min > piro[i]) {
                    break;
                }
            }
        }
    }

    int K_h = N - 1, K_p = N - 1;

    for (int i = 0; i < N; i++) {
        if (happiness[i] < h_max) {
            K_h = i;
            break;
        }

        if (piro[i] > p_min) {
            K_p = i;
            break;
        }
    }

    int solution = min(K_h, K_p);

    if (solution == 0) {
        cout << -1 << endl;
    } else {
        cout << solution << endl;
    }

    return 0;
}