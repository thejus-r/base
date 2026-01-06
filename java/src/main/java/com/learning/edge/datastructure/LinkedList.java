package com.learning.edge.datastructure;

import java.util.ArrayList;

class ListNode<T> {

    T data;
    ListNode<T> next;

    ListNode(T data) {
        this.data = data;
        this.next = null;
    }
}

public class LinkedList<T> {

    private ListNode<T> head;
    public int length = 0;

    public void add(T data) {
        ListNode<T> newNode = new ListNode<>(data);
        if (head == null) {
            head = newNode;
        } else {
            ListNode<T> current = head;

            while (current.next != null) {
                current = current.next;
            }

            current.next = newNode;
        }

        length++;
    }

    public boolean find(T data) {
        if (head == null) {
            return false;
        }

        ListNode<T> current = head;
        while (current.next != null) {
            if (current.data == data) {
                return true;
            }
        }

        return false;
    }

    public ArrayList<T> toArrayList() {
        ArrayList<T> list = new ArrayList<>();

        ListNode<T> current = head;

        while (current != null) {
            list.add(current.data);
            current = current.next;
        }

        return list;
    }
}
