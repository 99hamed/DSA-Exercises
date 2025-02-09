// HAMED SAADATI
#include <iostream>
#include "queue.h"
#include <bitset>
#include "huffman_coding.h"
using namespace std;


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

