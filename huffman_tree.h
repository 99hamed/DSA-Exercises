//
// Created by Hamed on 2/11/2025.
//

#ifndef HUFFMAN_CODING_HUFFMAN_TREE_H
#define HUFFMAN_CODING_HUFFMAN_TREE_H
#include "queue.h"

class huffman_tree {
public:
    node * make_huffman_tree(node* head) {
        pr_queue q;
        node *p = head;
        node* root=0;
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

            root = new node(b->character + a->character, a->count + b->count);

            root->left = a;
            root->right = b;

            q.enqueue(root);
        }


        return root;

    }
};


#endif //HUFFMAN_CODING_HUFFMAN_TREE_H
