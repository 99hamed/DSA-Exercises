//
// Created by Hamed on 1/27/2025.
//



#ifndef HUFFMAN_CODING_QUEUE_H
#define HUFFMAN_CODING_QUEUE_H
using namespace std;
struct node {
    int count;
    string word;
    node* next;
    node* data;
    node* right;
    node* left;
    node(string w = " ", int c = 1) : word(w), count(c), next(nullptr),right(nullptr),left(nullptr),data(nullptr) {}
    node(node* d):data(d), next(nullptr),right(nullptr),left(nullptr){}
};

class pr_queue {
    node* head=0;
    public:

    void enqueue(node* a){
//        node* c=new node(a->word,a->count);// copy of node
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
//            std::cout << "the queue is empty";
            return nullptr;
        }

        node* min = head;
        node* premin = nullptr;
        node* p = head;

        // اگر صف فقط یک گره دارد
        if (head->next == nullptr) {
            node* temp = head->data;
            head = nullptr; // صف خالی می‌شود
            return temp;
        }

        // پیدا کردن گره با کمترین مقدار count
        while (p->next != nullptr) {
            if (p->next->data->count < min->data->count) {
                premin = p;
                min = p->next;
            }
            p = p->next;
        }

        // حذف گره از صف
        if (min == head) {
            head = head->next; // حذف گره سر
        } else {
            premin->next = min->next; // حذف گره از وسط یا انتها
        }

        min->next = nullptr; // قطع اتصال گره حذف‌شده
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