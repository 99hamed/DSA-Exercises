#include <iostream>
#include "queue.h"
using namespace std;

//struct tree_node {
//    string word;
//    int count;
//    tree_node* left;
//    tree_node* right;
//    tree_node(string w="", int a=0) : word(w), count(a), left(nullptr), right(nullptr) {}
//};

class huffman_coding {
    node* head;
    string phrase;
public:
    huffman_coding(string w="") :phrase(w), head(nullptr) {}

    node* in_list(string a) {
        node* p = head;
        while (p != nullptr) {
            if (a == p->word) {
                return p;
            }
            p = p->next;
        }
        return nullptr;
    }

    node* getter() {
        return head;
    }

    void make_table() {
        int size = phrase.size();
        for (int i = 0; i < size; i++) {
            node* q = in_list(string(1, phrase[i]));
            if (q != nullptr) {
                q->count++;
            } else {
               node* p = new node(string(1, phrase[i]));
                if (head == nullptr) {
                    head = p;
                } else {
                    node* temp = head;
                    while (temp->next != nullptr) {
                        temp = temp->next;
                    }
                    temp->next = p;
                }
            }
        }
    }
    void huffman_tree(){
        pr_queue q;
        node* p = head;
        node* root=nullptr;
        while (p != nullptr) {
            q.enqueue(p);
            p = p->next;
        }
        node* temp=0;
        while (!q.isempty()){
            node* a=q.dequeue();
            node* b=q.dequeue();
            if(b== nullptr){
                root=a;
                break;
            }
            root=new node(b->word+a->word,a->count+b->count);

            root->left=a;
            root->right=b;

            q.enqueue(root);

        }

        head = root;

        // چاپ مقادیر
        cout << "Root: " << head->word << "          " << head->count << endl;

        if (head->left != nullptr)
            cout << "Left: " << head->left->word << "          " << head->left->count << endl;

        if (head->right != nullptr)
            cout << "Right: " << head->right->word << "          " << head->right->count << endl;


    }
};

int main() {
//    string name = "aaaaagfaassddffa";

    huffman_coding f("aaaaagfaassddffa");
    f.make_table();
    f.huffman_tree();


    return 0;
}

