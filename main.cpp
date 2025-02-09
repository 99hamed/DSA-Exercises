#include <iostream>
#include "queue.h"
#include <bitset>
#include "huffman_coding.h"
using namespace std;
/*
//CLASSES==========================================================================================================
class huffman_coding {
    node *head;
    node *root ;
    string phrase;
    string encoded="";

    public:

    huffman_coding(string w = "") : phrase(w), head(nullptr),root(nullptr) {}

    node* getroot(){
        return root;
    }
    node *find_in_list(string a) {

        node *temp = head;
        while (temp != nullptr) {
            if (temp->character == a)
                return temp;
            temp = temp->next;
        }

        return nullptr;
    }


    void make_table() {

        for (char c: phrase) {
            node *q = find_in_list(string(1, c));

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

            root = new node(b->character + a->character, a->count + b->count);

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
            cout<<p->character<<"    "<<p->code<<endl;
            p=p->next;
        }
    }
    void encode(){
        make_table();
        node *q = make_huffman_tree();
        generateCodes(q, "");


        for (char c: phrase){
            encoded+= (find_in_list(string(1,c))->code);
        }
    }
    void saveCompressedTextFile(string phrase ,const string& filename) {
        ofstream outFile(filename);
        if (!outFile) {
            cerr << "Error opening file for writing!\n";
            return;
        }

        outFile << phrase<< endl;

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


    void saveBinaryDataToFile(const string& binaryString, const string& filename) {
        if (binaryString.empty()) {
            cerr << "Error: Binary string is empty!" << endl;
            return;
        }

        ofstream outFile(filename, ios::binary);
        if (!outFile) {
            cerr << "Error: Failed to open file!" << endl;
            return;
        }

        size_t totalBits = binaryString.size();
        size_t fullBytesCount = totalBits / 8;
        size_t remainingBits = totalBits % 8;
        unsigned char paddingBits = (remainingBits == 0) ? 0 : (8 - remainingBits);





        for (size_t i = 0; i < fullBytesCount * 8; i += 8) {
            string byteChunk = binaryString.substr(i, 8);
            unsigned char byte = static_cast<unsigned char>(bitset<8>(byteChunk).to_ulong());
            outFile.write(reinterpret_cast<const char*>(&byte), 1);
        }


        if (remainingBits > 0) {
            string lastByteChunk = binaryString.substr(fullBytesCount * 8, remainingBits);
            lastByteChunk.append(paddingBits, '0');

            unsigned char lastByte = static_cast<unsigned char>(bitset<8>(lastByteChunk).to_ulong());
            outFile.write(reinterpret_cast<const char*>(&lastByte), 1);
        }
        outFile.write(reinterpret_cast<const char*>(&paddingBits), 1);

        outFile.close();
        cout << "File saved successfully: " << filename << endl;
    }



    string readBinaryDataFromFile(const string& filename) {
        ifstream inFile(filename, ios::binary);
        if (!inFile) {
            cerr << "Error: Failed to open file!" << endl;
            return "";
        }


        string binaryData;
        vector<char> fileBuffer((istreambuf_iterator<char>(inFile)), istreambuf_iterator<char>());
        inFile.close();

        if (fileBuffer.empty()) {
            cerr << "Error: File is empty!" << endl;
            return "";
        }


        unsigned char paddingBits = static_cast<unsigned char>(fileBuffer.back());
        fileBuffer.pop_back();


        for (char byte : fileBuffer) {
            binaryData += bitset<8>(static_cast<unsigned char>(byte)).to_string();
        }


        if (paddingBits > 0 && paddingBits < 8) {
            binaryData.erase(binaryData.size() - paddingBits);
        }

        return binaryData;
    }


    string decode(node* root, const string& encodedStr) {
        string decodedText = "";
        node* current = root;

        for (char bit : encodedStr) {
            if (bit == '0') {
                current = current->left;
            } else {
                current = current->right;
            }


            if (0==current->left && current->right==0) {
                decodedText += current->character;
                current = root;
            }
        }

        return decodedText;
    }

    string getstr(){
        return encoded;
    }

};
*/


    int main() {


        huffman_coding f;
        int choise;
        bool over=false;
        cout << "welcome to huffman encoding" << endl;
        while(!over) {
            cout << "1.encoding \n2.decoding \n3.exit" << endl;
            cout << "enter your choise :";
            cin >> choise;

            if (choise == 1) {
                f.loadTextFile("test.txt");
                f.encode();
                f.saveBinaryDataToFile(f.getstr(), "compressed");
                f.saveCompressedTextFile(f.getstr(), "encoded.txt");
            } else if (choise == 2) {
                string binaryString = f.readBinaryDataFromFile("compressed");
                string phrase = f.decode(f.getroot(), binaryString);
                f.saveCompressedTextFile(phrase, "decoded.txt");
            }
            else if(choise==3){
                cout<<"hope you enjoy";
                over=true;}
        }

        return 0;
    }

