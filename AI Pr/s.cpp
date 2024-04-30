#include <iostream>
#include <vector>

using namespace std;

class NQueens {
private:
    int n;
    vector<vector<int>> board;
    vector<vector<int>> solutions;

    bool isSafe(int row, int col) {
        // Check if no queens are attacking each other in the same column
        for (int i = 0; i < row; ++i) {
            if (board[i][col] == 1)
                return false;
        }

        // Check upper left diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; --i, --j) {
            if (board[i][j] == 1)
                return false;
        }

        // Check upper right diagonal
        for (int i = row, j = col; i >= 0 && j < n; --i, ++j) {
            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    void solveBacktracking(int row) {
        if (row == n) {
            solutions.push_back(board);
            return;
        }

        for (int col = 0; col < n; ++col) {
            if (isSafe(row, col)) {
                board[row][col] = 1;
                solveBacktracking(row + 1);
                board[row][col] = 0;  // Backtrack
            }
        }
    }

public:
    NQueens(int size) : n(size) {
        board.resize(n, vector<int>(n, 0));
    }

    vector<vector<int>> solve() {
        solveBacktracking(0);
        return solutions;
    }
};

int main() {
    int n = 8;  // Change the value of n as needed
    NQueens nQueens(n);
    vector<vector<int>> solutions = nQueens.solve();
    for (const auto& solution : solutions) {
        for (const auto& row : solution) {
            for (int cell : row)
                cout << (cell == 1 ? "Q" : "-") << " ";
            cout << endl;
        }
        cout << endl;
    }
    return 0;
}
