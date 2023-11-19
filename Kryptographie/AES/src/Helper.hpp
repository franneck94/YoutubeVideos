#pragma once

/*********************************************************************/
/*                       INCLUDES AND DEFINES                        */
/*********************************************************************/

#include <vector>
#include <iostream>
#include <bitset>

#include "AES.hpp"

using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::ifstream;

/*********************************************************************/
/*                          HELPER FUNCTIONS                         */
/*********************************************************************/

// Read-In Datafile in Hex-Format and Vector of ByteArrays
const vector<ByteArray> read_datafile(const string &file_path);

// Write-In Datafile in Hex-Format and Vector of ByteArrays
void write_datafile(const string &file_path, const vector<ByteArray> &encrypted);

// Read-In Key Datafile in Hex-Format
const ByteArray read_key(const string &file_path);

// Generate IV-Vector for Counter Mode
const ByteArray random_byte_array(const unsigned int &length);

// Cout whole ByteArray
void print_byte_array(ByteArray &arr);

// Checks if two ByteArrays has same values
bool check_byte_arrays(const ByteArray &arr1, const ByteArray &arr2);

// Checks if two Vector of ByteArrays has same values
bool check_vector_of_byte_arrays(const vector<ByteArray> &arr1, const vector<ByteArray> &arr2);

// Cout hex byte
void print_byte(const unsigned char &byte);

// XOR for ByteArray
ByteArray XOR(const ByteArray &arr1, const ByteArray &arr2);

// XOR for ByteArray
void XOR(ByteArray &arr1, const ByteArray &arr2, const unsigned int &length);