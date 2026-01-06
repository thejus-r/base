package com.learning.edge.datastructure;

class TrieNode {

    TrieNode[] children;
    boolean isLeaf;

    TrieNode() {
        this.children = new TrieNode[26];
        this.isLeaf = false;
    }
}

public class Trie {

    private TrieNode root;

    Trie() {
        this.root = new TrieNode();
    }

    public void insert(String key) {
        TrieNode curr = this.root;

        for (char c : key.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new TrieNode();
            }
            curr = curr.children[c - 'a'];
        }

        curr.isLeaf = true;
    }

    public boolean search(String key) {
        TrieNode curr = this.root;

        for (char c : key.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                return false;
            }

            curr = curr.children[c - 'a'];
        }

        return curr.isLeaf;
    }

    public boolean hasPrefix(String prefix) {
        TrieNode curr = this.root;

        for (char c : prefix.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                return false;
            }

            curr = curr.children[c - 'a'];
        }

        return true;
    }
}
