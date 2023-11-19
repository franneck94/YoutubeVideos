/*********************************************************************/
/*                       INCLUDES AND DEFINES                        */
/*********************************************************************/

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <chrono>
#include <string>
#include <omp.h>

#include "Helper.hpp"
#include "AES.hpp"

using std::cout;
using std::endl;
using std::vector;
using std::string;

int main()
{
	string file_path_messages = "C:/Users/Jan/OneDrive//Kryptographie/AES/text.txt";
	string file_path_encrypted = "C:/Users/Jan/OneDrive//Kryptographie/AES/encrypted.txt";

	ByteArray key = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
					0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
	vector<ByteArray> messages = read_datafile(file_path_messages);

	AES *aes = new AES(key);
	vector<ByteArray> decrypted_solution(messages.size(), ByteArray(KEY_BLOCK, 0x00));
	vector<ByteArray> encrypted_solution(messages.size(), ByteArray(KEY_BLOCK, 0x00));

	for (int i = 0; i != messages.size(); ++i)
	{
		encrypted_solution[i] = aes->encrypt(messages[i]);
	}

	write_datafile(file_path_encrypted, encrypted_solution);

	for (int i = 0; i != encrypted_solution.size(); ++i)
	{
		decrypted_solution[i] = aes->decrypt(encrypted_solution[i]);
	}

	cout << endl << "Legit solution: " << check_vector_of_byte_arrays(decrypted_solution, messages) << endl;

	delete aes;
	aes = nullptr;
	getchar();
}
