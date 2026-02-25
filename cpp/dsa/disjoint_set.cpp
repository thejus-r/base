
#include <utility>
#include <vector>
#include <print>

using namespace std;

class DisjointSet {
    private:
    int size;
    vector<int> rank;

    public:
    vector<int> parent;
    // init DisjointSet, parent[i] = i & rank[i] = 0
    DisjointSet(int size) {
        this->size = size;
        parent.resize(size);

        rank.resize(size, 0);

        for (int i = 0; i < size; i ++) {
            parent[i] = i;
        }
    }

    // Path compression
    int ufind(int node) {
        if (node == parent[node]) {
            return node;
        }
        return parent[node] = ufind(parent[node]);
    }

    // Union by Rank
    void uunion(int a, int b) {
        a = ufind(a);
        b = ufind(b);

        if (a != b) {
            if (rank[a] < rank[a])
                swap(a, b);
            parent[b] = a;
            if (rank[a] == rank[b])
                rank[a]++;
        }
        return;
    }
};

int main() {

    DisjointSet uf(10);

    uf.uunion(0, 1);
    uf.uunion(1, 2);
    uf.uunion(2, 3);
    uf.uunion(3, 4);

    println("Parent, {}", uf.parent);

    return 0;
}
