/*********************************************************************/
/*                       INCLUDES AND DEFINES                        */
/*********************************************************************/

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <random>

#include "Helper.hpp"

using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::ifstream;

/*********************************************************************/
/*                          HELPER FUNCTIONS                         */
/*********************************************************************/

// Read-In Datafile in Hex-Format and Vector of ByteArrays
const vector<ByteArray> read_datafile(const string &file_path)
{
	vector<ByteArray> data;
	char act_char;
	unsigned int counter = 0;
	ByteArray next_byte_array;
	ifstream infile;

	infile.open(file_path);

	while (!infile.eof())
	{
		if (counter < KEY_BLOCK)
		{
			infile.get(act_char);
			next_byte_array.push_back(act_char);
			counter++;
		}
		else
		{
			data.push_back(next_byte_array);
			next_byte_array = {};
			counter = 0;
		}
	}

	infile.close();
	return data;
}

// Write-In Datafile in Hex-Format and Vector of ByteArrays
void write_datafile(const string &file_path, const vector<ByteArray> &encrypted)
{
	std::ofstream outfile;

	outfile.open(file_path);

	for (int i = 0; i != encrypted.size(); ++i)
	{
		for (int j = 0; j != encrypted[i].size(); ++j)
		{
			outfile << encrypted[i][j];
		}
	}

	outfile.close();
}

// Read-In Key Datafile in Hex-Format
const ByteArray read_key(const string &file_path)
{
	ByteArray data;
	char act_char;
	unsigned int counter = 0;
	ifstream infile;

	infile.open(file_path);

	while (!infile.eof() && counter < KEY_BLOCK)
	{
		infile.get(act_char);
		data.push_back(act_char);
		counter++;
	}

	infile.close();
	return data;
}

// Generate IV-Vector for Counter Mode
const ByteArray random_byte_array(const unsigned int &length)
{
	ByteArray byte_array(length);

	std::random_device rd;
	std::mt19937 generator(rd());
	std::uniform_int_distribution<int> distribution(0, 15);

	for (size_t i = 0; i != byte_array.size(); ++i)
	{
		byte_array[i] = (unsigned char)distribution(generator);
	}

	return byte_array;
}


// Cout whole ByteArray
void print_byte_array(ByteArray &arr)
{
	for (size_t i = 0; i != arr.size(); ++i)
	{
		cout << std::hex << (int)arr[i] << "\t";
	}
	cout << endl << endl;
}

// Checks if two Vector of ByteArrays has same values
bool check_vector_of_byte_arrays(const vector<ByteArray> &arr1, const vector<ByteArray> &arr2)
{
	bool check = true;

	if (arr1.size() != arr2.size())
		return false;

	for (size_t i = 0; i != arr1.size(); ++i)
	{
		if (arr1[i] != arr2[i])
			check = check_byte_arrays(arr1[i], arr2[i]);
		if (!check)
		{
			cout << endl << "Error at index i = " << i << endl;
			return false;
		}
	}

	return true;
}

// Checks if two ByteArrays has same values
bool check_byte_arrays(const ByteArray &arr1, const ByteArray &arr2)
{
	if (arr1.size() != arr2.size())
		return false;

	for (size_t i = 0; i != arr1.size(); ++i)
	{
		if (arr1[i] != arr2[i])
		{
			cout << endl << "Error at index i2 = " << i << endl;
			return false;
		}
	}

	return true;
}

// Cout hex byte
void print_byte(const unsigned char &byte)
{
	cout << endl << "Byte: " << std::hex << (int)byte;
}

// XOR for ByteArray
ByteArray XOR(const ByteArray &arr1, const ByteArray &arr2)
{
	ByteArray res(arr1.size(), 0x00);

	for (size_t i = 0; i != arr1.size(); ++i)
	{
		res[i] = arr1[i] ^ arr2[i];
	}

	return res;
}

// XOR for ByteArray
void XOR(ByteArray &arr1, const ByteArray &arr2, const unsigned int &length)
{
	register int i = 0;

	for (i; i != length; ++i)
	{
		arr1[i] = arr1[i] ^ arr2[i];
	}
}