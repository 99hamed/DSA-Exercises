

#ifndef HUFFMAN_CODING_QUEUE_H
#define HUFFMAN_CODING_QUEUE_H
using namespace std;
struct node {
    int count;
    string character;
    string code;
    node* next;
    node* tree_node;
    node* right;
    node* left;
    node(string w = "", int c =0) : character(w), count(c), next(nullptr),right(nullptr),left(nullptr),tree_node(nullptr) {}
    node(node* d):tree_node(d), next(nullptr),right(nullptr),left(nullptr){}

};

class pr_queue {
    node* head=0;
    public:

    void enqueue(node* a){

        if(head==0){
            head=new node(a);
            return;
        }

        node* p=head;
        while(p->next!= nullptr)
                p=p->next;
        node* temp=new node(a);
        p->next=temp;
        temp->next=0;


    }
    node* dequeue() {
        if (isempty()) {
            std::cout << "the queue is empty";
            return nullptr;
        }

        node* min = head;
        node* premin = nullptr;
        node* p = head;


        if (head->next == nullptr) {
            node* temp = head->tree_node;
            head = nullptr;
            return temp;
        }


        while (p->next != nullptr) {
            if (p->next->tree_node->count < min->tree_node->count) {
                premin = p;
                min = p->next;
            }
            p = p->next;
        }

        if (min == head) {
            head = head->next;
        } else {
            premin->next = min->next;
        }

        min->next = nullptr;
        return min->tree_node;
    }

    bool isempty() {
        if (head == nullptr)
            return true;
        else
            return false;
    }




};

#endif