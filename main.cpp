#include <iostream>
#include "queue.h"
#include <fstream>
#include <bitset>
#include <cstring>
using namespace std;

//CLASSES==========================================================================================================
class huffman_coding {
    node *head;
   node *root = nullptr;
    string phrase;
    string encoded="";

    public:

    huffman_coding(string w = "") : phrase(w), head(nullptr) {}

    node* getroot(){
        return root;
    }
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
//       node *root = nullptr;
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
    void encoding(){
        for (char c: phrase){
            encoded+= (in_list(string(1,c))->code);
        }
    }
    node *getter() {
        return head;
    }

    void saveCompressedTextFile(const string& filename) {
        ofstream outFile(filename);
        if (!outFile) {
            cerr << "Error opening file for writing!\n";
            return;
        }

        outFile << encoded << endl;

        outFile.close();
        cout << "Compressed text file saved as " << filename << endl;

    }



    void loadTextFile(const string& filename) {
        ifstream inFile(filename);
        if (!inFile) {
            cerr << "eror in open file!\n";
            return;
        }
        phrase= "";
        inFile >> phrase;
        inFile.close();
        cout << "file text read!\n";
    }


    void saveStringAsBinaryFile(const string& binaryString, const string& filename) {
        ofstream outFile(filename, ios::binary);
        if (!outFile) {
            cerr << "eror occurred!\n";
            return;
        }


        for (size_t i = 0; i < binaryString.size(); i += 8) {
            string byteChunk = binaryString.substr(i, 8);


            while (byteChunk.length() < 8) {
                byteChunk += "0";
            }

            unsigned char byte = bitset<8>(byteChunk).to_ulong();
            outFile.write(reinterpret_cast<const char*>(&byte), 1);
        }

        outFile.close();
        cout << "file saved successfully " << filename << endl;
    }

    string readBinaryFileAsString(const string& filename) {
        ifstream inFile(filename, ios::binary);
        if (!inFile) {
            cerr << "eror in opening file\n";
            return "";
        }

        string binaryData = "";
        char byteChar;
        while (inFile.read(&byteChar, sizeof(byteChar))) {
            bitset<8> byte((unsigned char)byteChar);
            binaryData += byte.to_string();
        }

        inFile.close();
        return binaryData.substr(0,encoded.size());
    }
    string decodeHuffman(node* root, const string& encodedStr) {
        string decodedText = "";
        node* current = root;

        for (char bit : encodedStr) {
            if (bit == '0') {
                current = current->left;
            } else {
                current = current->right;
            }


            if (0==current->left && current->right==0) {
                decodedText += current->word;
                current = root;
            }
        }

        return decodedText;
    }

    string getstr(){
        return encoded;
    }

};



    int main() {
//    string name = "aaaaagfaassddffa";

        huffman_coding f("abhdhhhhjhjjjjjhhdgf");
//      f.loadTextFile("c23.txt");
        cout<<"abhdhhhhjhjjjjjhhdgdf"<<endl;
        f.make_table();
        node *p = f.getter();
        while (p != nullptr) {
            cout << p->word << "    " << p->count << endl;
            p = p->next;
        }

        node *q = f.make_huffman_tree();
        f.generateCodes(q, "");
        cout << "Root: " << q->word << "          " << q->count << endl;

        if (q->left != nullptr)
            cout << "Left: " << q->left->word << "          " << q->left->count << endl;

        if (q->right != nullptr)
            cout << "Right: " << q->right->word << "          " << q->right->count << endl;
        f.printHuffmanCodes();
        f.encoding();
        cout << f.getstr() << endl;
        f.saveStringAsBinaryFile(f.getstr(),"compressed.bin");



        string binaryString = f.readBinaryFileAsString("compressed.bin");
        cout<<binaryString<<endl;
        cout<<f.decodeHuffman(f.getroot(),binaryString);

        return 0;
    }

