#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
using namespace std;

const int INF = 1 << 30;
const int DEPTH = 13;
const int dx[] = {0, 0, 1, -1};
const int dy[] = {-1, 1, 0, 0};

class Point {
public:
  int x, y;
  Point() {}
  Point(int x, int y) {
    this->x = x;
    this->y = y;
  }
};

class State {
public:
  Point p;
  vector<int> move;
  State(Point p, vector<int> move) {
    this->p = p;
    this->move = move;
  }
};

void print_stage(const int turn, const int X, const int Y, const vector<vector<int> >& stage) {
  cerr << "turn: " << turn << endl;
  for (int y = 0; y < Y; ++y) {
    for (int x = 0; x < X; ++x) {
      if (stage[y][x] == 0) {
        cerr << " ";
      } else if (stage[y][x] == 1) {
        cerr << "A";
      } else if (stage[y][x] == 2) {
        cerr << "#";
      } else if (stage[y][x] == 3) {
        cerr << "p";
      } else {
        cerr << "e";
      }
    }
    cerr << endl;
  }
}

vector<vector<int> > merge_stage(const int X, const int Y, const vector<vector<int> >& stage, const vector<Point>& player, const vector<Point>& enemy) {
  vector<vector<int> > merge_stage = stage;

  for (int i = 0; i < player.size(); ++i) {
    merge_stage[player[i].y][player[i].x] = 3;
  }
  for (int i = 0; i < enemy.size(); ++i) {
    merge_stage[enemy[i].y][enemy[i].x] = 4;
  }
  
  return merge_stage;
}

bool movable(const int X, const int Y, const vector<vector<int> >&stage, int x, int y) {
  if (x < 0 || x >= X || y < 0 || y >= Y || stage[y][x] > 1) {
    return false;
  }
  return true;
}

int greedy(const int X, const int Y, const vector<vector<int> >& stage, int x, int y) {
  queue<State> q;
  q.push(State(Point(x, y), vector<int>()));

  vector<vector<int> > visited(Y, vector<int>(X, 0));
  while (!q.empty()) {
    State st = q.front();
    q.pop();

    visited[st.p.y][st.p.x] = 1;
    if (stage[st.p.y][st.p.x] == 1) {
      return st.move[0];
    }

    for (int d = 0; d < 4; ++d) {
      int xx = st.p.x + dx[d];
      int yy = st.p.y + dy[d];
      if (!movable(X, Y, stage, xx, yy) || visited[yy][xx]) {
        continue;
      }

      State next_state = st;
      next_state.p.x = xx;
      next_state.p.y = yy;
      next_state.move.push_back(d);
      q.push(next_state);
    }
  }
  return -1;
}

int calc_movable_count(const int X, const int Y, const vector<vector<int> >& stage, const int x, int y) {
  queue<Point> q;
  q.push(Point(x, y));
  vector<vector<int> > visited(Y, vector<int>(X, 0));

  int movable_count = 0;
  while (!q.empty()) {
    Point p = q.front();
    q.pop();

    if (visited[p.y][p.x]) {
      continue;
    }
    visited[p.y][p.x] = 1;
    ++movable_count;
    for (int d = 0; d < 4; ++d) {
      int xx = p.x + dx[d];
      int yy = p.y + dy[d];
      if (!movable(X, Y, stage, xx, yy)) {
        continue;
      }
      q.push(Point(xx, yy));
    }
  }
  return movable_count;
}

pair<int, int> evaluate(const int turn, const int X, const int Y, const vector<vector<int> >& org_stage, const vector<Point>& player, const vector<Point>& enemy) {
  vector<vector<int> > stage = merge_stage(X, Y, org_stage, player, enemy);

  int p_ev = calc_movable_count(X, Y, stage, player[0].x, player[0].y);
  int p_size = player.size();

  int e_ev = calc_movable_count(X, Y, stage, enemy[0].x, enemy[0].y);
  int e_size = enemy.size();

  if (turn >= 80) {
    return make_pair<int, int>(-1 * (p_size - e_size), p_ev - e_ev);
  }

  if (p_size - e_size >= 10) {
    return make_pair<int, int>(p_ev - e_ev, p_size - e_size);
  } else {
    return make_pair<int, int>(p_size - e_size, p_ev - e_ev);
  }
}

pair<int, int> rev_score(const pair<int ,int>& p) {
  return make_pair<int, int>(-p.first, -p.second);
}

pair<int, pair<int, int> > dfs(const int turn, const int depth, const int X, const int Y, vector<vector<int> > org_stage, vector<Point> player, vector<Point> enemy, pair<int, int> alpha, pair<int, int> beta) {
  if (turn == 0) {
    int p_size = player.size();
    int e_size = enemy.size();
    return make_pair(-1, make_pair(p_size - e_size, 0));
  }
  if (depth == 0) {
    return make_pair(-1, evaluate(turn, X, Y, org_stage, player, enemy));
  }

  int move = -1;
  pair<int, int> score = make_pair(-INF, -INF);
  vector<vector<int> > stage = merge_stage(X, Y, org_stage, player, enemy);
  for (int d = 0; d < 4; ++d) {
    int xx = player[0].x + dx[d];
    int yy = player[0].y + dy[d];
    if (!movable(X, Y, stage, xx, yy)) {
      continue;
    }

    vector<Point> next_player;
    next_player.push_back(Point(xx, yy));
    if (stage[yy][xx] == 1) {
      org_stage[yy][xx] = 0;
      for (int i = 0; i < player.size(); ++i) {
        next_player.push_back(player[i]);
      }
    } else {
      for (int i = 0; i < player.size() - 1; ++i) {
        next_player.push_back(player[i]);
      }
    }
    pair<int, pair<int, int> > ret = dfs(turn - 1, depth - 1, X, Y, org_stage, enemy, next_player, rev_score(beta), rev_score(alpha));

    if (stage[yy][xx] == 1) {
      org_stage[yy][xx] = 1;
    }
    if (ret.second.first * -1 > score.first ||
       (ret.second.first * -1 == score.first && ret.second.second * -1 > score.    second)) {
      move = d;
      score.first = ret.second.first * -1;
      score.second = ret.second.second * -1;
    }

    alpha = score;
    if (alpha.first > beta.first ||
        (alpha.first == beta.first && alpha.second >= beta.second)) {
      break;
    }
  }
  return make_pair(move, score);
}

void solve(const int turn, const int X, const int Y, vector<vector<int> > org_stage, vector<Point> player, vector<Point> enemy) {
  vector<vector<int> > stage = merge_stage(X, Y, org_stage, player, enemy);
  if (player.size() == 1) {
    int move = greedy(X, Y, stage, player[0].x, player[0].y);
    cout << move << endl;
  } else {
    pair<int, int> alpha = make_pair(-INF, -INF);
    pair<int, int> beta = make_pair(INF, INF);
    pair<int, pair<int, int> > ret = dfs(turn, DEPTH, X, Y, org_stage, player, enemy, alpha, beta);
    vector<int> move_cand;
    if (ret.first == -1) {
      for (int d = 0; d < 4; ++d) {
        int xx = player[0].x + dx[d];
        int yy = player[0].y + dy[d];
        if (!movable(X, Y, stage, xx, yy)) {
          continue;
        }
        move_cand.push_back(d);
      }
      if (move_cand.size() != 0) {
        ret.first = move_cand[rand() % move_cand.size()];
      }
    }
    cout << ret.first << endl;
    cerr << ret.second.first << endl;
    print_stage(turn, X, Y, stage);
  }
}

int main() {
  ifstream ifs("input.txt");
  cin.rdbuf(ifs.rdbuf());

  int turn;
  cin >> turn;

  int Y, X;
  cin >> Y >> X;

  vector<vector<int> > stage(Y, vector<int>(X));
  for (int y = 0; y < Y; ++y) {
    for (int x = 0; x < X; ++x) {
      string s;
      cin >> s;
      if (s == "EMPTY" || s == "HEAD" || s == "BODY") {
        stage[y][x] = 0;
      } else if (s == "APPLE") {
        stage[y][x] = 1;
      } else {
        stage[y][x] = 2;
      }
    }
  }

  int n;
  cin >> n;
  vector<Point> player;
  for (int i = 0; i < n; ++i) {
    int x, y;
    cin >> x >> y;
    player.push_back(Point(x, y));
  }

  cin >> n;
  vector<Point> enemy;
  for (int i = 0; i < n; ++i) {
    int x, y;
    cin >> x >> y;
    enemy.push_back(Point(x, y));
  }

  solve(turn * 2, X, Y, stage, player, enemy);

  return 0;
}
