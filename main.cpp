#include <iostream>
#include "queue.h"
#include <map>
using namespace std;


class huffman_coding {
    node *head;
    string phrase;


public:

    huffman_coding(string w = "") : phrase(w), head(nullptr) {}

    node *in_list(string a) {

        node *temp = head;
        while (temp != nullptr) {
            if (temp->word == a)
                return temp;
            temp = temp->next;
        }

        return nullptr;
    }


    void make_table() {

        for (char c: phrase) {
            node *q = in_list(string(1, c));

            if (q != nullptr) {
                q->count++;
            } else {
                node *p = new node(string(1, c), 1);
                p->next = head;
                head = p;
            }
        }
    }


    node * make_huffman_tree() {
        pr_queue q;
        node *p = head;
        node *root = nullptr;
        while (p != nullptr) {
            q.enqueue(p);
            p = p->next;
        }
        node *temp = 0;
        while (!q.isempty()) {
            node *a = q.dequeue();
            if (q.isempty()) {
                root = a;
                break;
            }
            node *b = q.dequeue();

            root = new node(b->word + a->word, a->count + b->count);

            root->left = a;
            root->right = b;

            q.enqueue(root);
        }


        return root;

    }


    void generateCodes(node *root, string code) {
        if (!root) return;


        if (!root->left && !root->right) {
            root->code = code;
        }

        generateCodes(root->left, code + "0");
        generateCodes(root->right, code + "1");
    }

    void printHuffmanCodes() {
        cout << "Huffman Codes:\n";
        node* p=head;

        while(p!= nullptr){
            cout<<p->word<<"    "<<p->code<<endl;
            p=p->next;
        }
    }

    node *getter() {
        return head;
    }



};
    int main() {
//    string name = "aaaaagfaassddffa";

        huffman_coding f("aaaaagfaassddffa");
        f.make_table();
        node *p = f.getter();
        while (p != nullptr) {
            cout << p->word << "    " << p->count << endl;
            p = p->next;
        }

        node *q = f.make_huffman_tree();
        f.generateCodes(q,"");
        cout << "Root: " << q->word << "          " << q->count << endl;

        if (q->left != nullptr)
            cout << "Left: " << q->left->word << "          " << q->left->count << endl;

        if (q->right != nullptr)
            cout << "Right: " << q->right->word << "          " << q->right->count << endl;
        f.printHuffmanCodes();

        return 0;
    }

