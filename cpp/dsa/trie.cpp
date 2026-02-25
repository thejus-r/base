// Trie Data Structure

#include <string>

using namespace std;

class TrieNode {
    TrieNode* children[26];
    bool endOfWord;

    public:
    TrieNode() {
        endOfWord = false;
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
    }
};

class Trie {
    private:
    TrieNode* root;

    public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string str) {
        TrieNode* node = root;
        for (char c: str) {

        }
    }
};
