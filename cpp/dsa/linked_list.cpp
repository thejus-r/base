

using namespace std;

class Node {
    public:
    int data;
    Node* next;

    Node() {
        data = 0;
        next = nullptr;
    }

    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
    private:
    Node *head;

    public:
    LinkedList() {
        head = nullptr;
    }

    void insert_front(int data) {
        Node *newNode = new Node(data);

        if (head == nullptr) {
            head = newNode;
            return;
        }

        newNode->next = this->head;
        this->head = newNode;
    }
};
