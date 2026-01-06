package com.learning.edge.datastructure;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayList;
import java.util.Arrays;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class LinkedListTest {

    LinkedList<Integer> list;

    @BeforeEach
    void setUp() {
        this.list = new LinkedList<>();
    }

    @Test
    @DisplayName("Can add Integer to the List")
    void testAddElement() {
        this.list.add(1);

        assertTrue(this.list.length == 1, "Length of linkedList should be 1");
    }

    @Test
    @DisplayName("Find an element in a empty list")
    void testFindElementInEmpty() {
        assertFalse(this.list.find(10), "Should not find '10' in the list");
    }

    @Test
    @DisplayName("Find inserted element in a list")
    void testInsertedElement() {
        this.list.add(10);
        assertFalse(this.list.find(10), "Should find '10' in the list");
    }

    @Test
    @DisplayName("Should convert to ArrayList")
    void testToArrayList() {
        list.add(1);
        list.add(2);

        ArrayList<Integer> arr1 = list.toArrayList();

        ArrayList<Integer> arr2 = new ArrayList<>(Arrays.asList(1, 2));

        assertTrue(arr1.equals(arr2), "Both array should be equal");
    }
}
