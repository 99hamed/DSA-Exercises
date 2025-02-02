

#ifndef HUFFMAN_CODING_QUEUE_H
#define HUFFMAN_CODING_QUEUE_H
using namespace std;
struct node {
    int count;
    string word;
    string code;
    node* next;
    node* data;
    node* right;
    node* left;
    node(string w = "", int c =0) : word(w), count(c), next(nullptr),right(nullptr),left(nullptr),data(nullptr) {}
    node(node* d):data(d), next(nullptr),right(nullptr),left(nullptr){}
    node(string w,string c): word(w),code(c){}
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
            node* temp = head->data;
            head = nullptr;
            return temp;
        }


        while (p->next != nullptr) {
            if (p->next->data->count < min->data->count) {
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
        return min->data;
    }

    bool isempty() {
        if (head == nullptr)
            return true;
        else
            return false;
    }



};

#endif