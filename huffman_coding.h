#ifndef HUFFMAN_CODING_HUFFMAN_CODING_H
#define HUFFMAN_CODING_HUFFMAN_CODING_H
#include <iostream>
#include"queue.h"
#include <fstream>
#include <bitset>
#include <vector>
#include<sstream>
#include"huffman_tree.h"
using namespace std;
class huffman_coding {

        node *head;
        node *root ;
        string phrase;
        string encoded="";

    public:
        huffman_coding();
        huffman_coding(string);
        node* getroot();
        node *find_in_list(string );
        void make_table() ;
//        node * make_huffman_tree();
        void generateCodes(node*, string);
        void encode();

        void saveCompressedTextFile(string  ,const string& );
        void loadTextFile(const string& );
        void saveBinaryDataToFile(const string& , const string&);
        string readBinaryDataFromFile(const string& );

        string decode(node* , const string& );
        string get_encoded();



};


#endif
