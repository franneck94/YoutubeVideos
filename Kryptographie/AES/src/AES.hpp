#pragma once

/*********************************************************************/
/*                       INCLUDES AND DEFINES                        */
/*********************************************************************/

#include <vector>
#include <iostream>

#include "Table.hpp"

#define AES_BITS 128
#define NUM_ROUNDS 10
#define SUB_KEYS (NUM_ROUNDS + 1)
#define KEY_BLOCK 16

typedef std::vector<unsigned char> ByteArray;
using std::vector;

/*********************************************************************/
/*                         CLASS DEFINITION                          */
/*********************************************************************/

class AES
{

public:
	// Constructor
	AES(const ByteArray &key);
	// Main functions of AES
	ByteArray encrypt(const ByteArray &m_message);
	ByteArray decrypt(const ByteArray &m_message);

private:
	// Member vairables
	ByteArray m_key;
	vector<ByteArray> m_subkeys;

	// Key schedule functions
	void key_schedule();
	ByteArray sub_key128(ByteArray &prev_subkey, const int &r);

	// Sub-Layers of AES round
	// Byte-Sub
	void byte_sub(ByteArray &message);
	void byte_sub_inv(ByteArray &message);
	// SHift-Rows
	void shift_rows(ByteArray &message);
	void shift_rows_inv(ByteArray &message);
	// Mix-Col
	void mix_columns(ByteArray &message);
	void mix_columns_inv(ByteArray &message);
	// Key-Add
	void key_addition(ByteArray &message, const int &r);
};