/*********************************************************************/
/*                       INCLUDES AND DEFINES                        */
/*********************************************************************/

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>

#include "AES.hpp"
#include "Helper.hpp"

using std::cout;
using std::endl;
using std::vector;

ByteArray AES::encrypt(const ByteArray &m_message)
{
	register int i = 0, round = 0;
	ByteArray message = m_message;

	// Key-Add before round 1 (R0)
	key_addition(message, round);
	round = 1;

	// Round 1 to NUM_ROUNDS - 1 (R1 to R9)
	for (round; round != NUM_ROUNDS; ++round)
	{
		byte_sub(message);
		shift_rows(message);
		mix_columns(message);
		key_addition(message, round);
	}

	// Last round without Mix-Column (RNUM_ROUNDS)
	round = NUM_ROUNDS;
	byte_sub(message);
	shift_rows(message);
	key_addition(message, round);

	return message;
}