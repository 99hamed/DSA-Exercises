cmake_minimum_required(VERSION 3.28)
project(huffman_coding)

set(CMAKE_CXX_STANDARD 17)

add_executable(huffman_coding main.cpp
        queue.h
        huffman_coding.cpp
        huffman_tree.h)
