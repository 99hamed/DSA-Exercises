#include <iostream>
using namespace std;

struct tree_node {
    string word;
    int number;
    tree_node* left;
    tree_node* right;
    tree_node(string w, int a) : word(w), number(a), left(nullptr), right(nullptr) {}
};

struct link_node {
    int count;
    char word;
    link_node* next;
    link_node(char w = ' ', int c = 1) : word(w), count(c), next(nullptr) {}
};

class huffman_coding {
    link_node* head;

public:
    huffman_coding() : head(nullptr) {} // مقداردهی اولیه head

    link_node* in_list(char a) {
        link_node* p = head;
        while (p != nullptr) {
            if (a == p->word) {
                return p;
            }
            p = p->next;
        }
        return nullptr;
    }

    link_node* getter() {
        return head;
    }

    void encode(string phrase) {
        int size = phrase.size(); // استفاده از size() برای طول رشته
        for (int i = 0; i < size; i++) {
            link_node* q = in_list(phrase[i]);
            if (q != nullptr) {
                q->count++;
            } else {
                link_node* p = new link_node(phrase[i]);
                if (head == nullptr) {
                    head = p;
                } else {
                    link_node* temp = head;
                    while (temp->next != nullptr) {
                        temp = temp->next;
                    }
                    temp->next = p;
                }
            }
        }
    }
};

int main() {
    string name = "aaaaagfaassddffa";

    huffman_coding f;
    f.encode(name);

    link_node* p = f.getter();
    while (p != nullptr) {
        cout << p->word << ": " << p->count << endl;
        p = p->next;
    }

    return 0;
}
