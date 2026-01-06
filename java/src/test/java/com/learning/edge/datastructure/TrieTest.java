package com.learning.edge.datastructure;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class TrieTest {

    private Trie trie;

    @BeforeEach
    void setUp() {
        trie = new Trie();
    }

    @Test
    @DisplayName("Should successfully insert and search for a valid word")
    void testInsertAndSearch() {
        trie.insert("hello");
        assertTrue(
            trie.search("hello"),
            "The word 'hello' should be found after insertion."
        );
    }

    @Test
    @DisplayName("Should return false for words that have not been inserted")
    void testSearchForAbsentWord() {
        trie.insert("world");
        assertFalse(
            trie.search("hello"),
            "Search should fail for a word that was never inserted."
        );
    }

    @Test
    @DisplayName("Should distinguish between a prefix and a complete word")
    void testPrefixVsCompleteWord() {
        trie.insert("apple");
        assertTrue(trie.hasPrefix("app"), "Prefix 'app' should exist.");
        assertFalse(
            trie.search("app"),
            "Word 'app' should not be found (only 'apple' was inserted)."
        );
    }

    @Test
    @DisplayName("Should handle overlapping words correctly.")
    void testOverlappingWords() {
        trie.insert("car");
        trie.insert("card");

        assertTrue(trie.search("car"), "Should find 'car'");
        assertTrue(trie.search("card"), "Should find 'card'");
        assertTrue(trie.hasPrefix("ca"), "Should find prefix 'ca'.");
    }

    @Test
    @DisplayName("Should handle independent branches correctly.")
    void testIndependentBranches() {
        trie.insert("cat");
        trie.insert("dog");

        assertTrue(trie.search("cat"));
        assertTrue(trie.search("dog"));
        assertFalse(trie.search("bird"), "Should not be able to find 'bird'");
    }

    @Test
    @DisplayName("Should handle empty strings correctly.")
    void testEmptyStrings() {
        trie.insert("");
        assertTrue(trie.search(""), "Should find empty string.");
        assertTrue(trie.hasPrefix(""), "Should find empty prefix.");
    }

    @Test
    @DisplayName("Should return false for prefix that does not exist")
    void testNonExisitingPrefix() {
        trie.insert("banana");
        assertFalse(trie.hasPrefix("nana"), "Prefix 'nana' should not exists.");
        assertFalse(trie.hasPrefix("band"), "Prefix 'band' should not exists.");
    }
}
