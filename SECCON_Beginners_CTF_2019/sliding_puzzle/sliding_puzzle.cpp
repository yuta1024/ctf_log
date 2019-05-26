#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

const int SIZE = 3;
const int dx[] = {0, 1, 0, -1};
const int dy[] = {-1, 0, 1, 0};
const int dm[] = {0, 1, 2, 3};

class State {
 public:
  int pos;
  vector<vector<int> > p;
  vector<int> move;

  State(int pos, vector<vector<int> > p, vector<int> move) {
    this->pos = pos;
    this->p = p;
    this->move = move;
  }
};

bool validate(const vector<vector<int> >& p) {
  int prev = -1;
  for (int i = 0; i < SIZE; ++i) {
    for (int j = 0; j < SIZE; ++j) {
      if (prev > p[i][j]) {
        return false;
      }
      prev = p[i][j];
    }
  }
  return true;
}

vector<int> solve(const vector<vector<int> >& p, int pos) {
  queue<State> q;
  q.push(State(pos, p, vector<int>()));

  set<vector<vector<int> > > visited;
  while (!q.empty()) {
    const State s = q.front();
    q.pop();
    visited.insert(s.p);
    if (validate(s.p)) {
      return s.move;
    }

    for (int d = 0; d < 4; ++d) {
      int xx = s.pos % SIZE + dx[d];
      int yy = s.pos / SIZE + dy[d];
      if (xx < 0 || xx >= SIZE || yy < 0 || yy >= SIZE) {
        continue;
      }

      vector<vector<int> > pp = s.p;
      swap(pp[s.pos / SIZE][s.pos % SIZE], pp[yy][xx]);
      if (visited.find(pp) == visited.end()) {
        vector<int> mm = s.move;
        mm.push_back(dm[d]);
        int new_pos = yy * SIZE + xx;
        q.push(State(new_pos, pp, mm));
      }
    }
  }
}

int main() {
  int pos = -1;
  vector<vector<int> > p(SIZE, vector<int>(SIZE));
  ifstream ifs("in.txt");
  cin.rdbuf(ifs.rdbuf());
  for (int i = 0; i < SIZE; ++i) {
    for (int j = 0; j < SIZE; ++j) {
      cin >> p[i][j];
      if (p[i][j] == 0) {
        pos = i * SIZE + j;
      }
    }
  }

  vector<int> ans = solve(p, pos);
  for (int i = 0; i < ans.size(); ++i) {
    cout << ans[i] << " ";
  }
  cout << endl;
  return 0;
}
