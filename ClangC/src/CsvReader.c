#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "CsvReader.h"

#define NEW_LINE_ASCII 10
#define BUFFER_SIZE 64
#define NUM_VALUES 2

RETURN_CODES line_count(const char *const file_path, unsigned int *const num_lines)
{
    FILE *fp = fopen(file_path, "r");

    if (fp == NULL)
    {
        int errornum = errno;
        fprintf(stderr, "Error in opening file: %s\n", strerror(errornum));
        return FAILURE;
    }

    unsigned int count = 1;
    char temp = 0;

    while (fscanf(fp, "%c", &temp) != EOF)
    {
        if (temp == NEW_LINE_ASCII)
        {
            count++;
        }
    }

    *num_lines = count;

    int return_close = fclose(fp);
    fp = NULL;

    if (return_close == EOF)
    {
        return FAILURE;
    }

    return SUCCESS;
}

RETURN_CODES read_simple_csv(const char *const file_path, records_t *const records)
{
    FILE *fp = fopen(file_path, "r");

    if (fp == NULL)
    {
        int errornum = errno;
        fprintf(stderr, "Error in opening file: %s\n", strerror(errornum));
        return FAILURE;
    }

    unsigned int num_lines = 0;
    RETURN_CODES return_code = line_count(file_path, &num_lines);

    if (return_code != SUCCESS)
    {
        fclose(fp);
        return return_code;
    }

    entry_t *entries = create_entries(num_lines);

    if (entries == NULL)
    {
        fclose(fp);
        return FAILURE;
    }

    for (unsigned int i = 0; i < num_lines; i++)
    {
        char buffer[BUFFER_SIZE] = {'\0'};
        fgets(buffer, BUFFER_SIZE, fp);
        buffer[strcspn(buffer, "\r\n")] = '\0';

        int scanned_arguments = sscanf(buffer, "%c,%d", &entries[i].letter, &entries[i].value);

        if (scanned_arguments != NUM_VALUES)
        {
            num_lines = i;
            break;
        }
    }

    int return_close = fclose(fp);
    fp = NULL;

    if (return_close == EOF)
    {
        return FAILURE;
    }

    return_code = fill_records(records, entries, num_lines);

    if (return_code != SUCCESS)
    {
        return return_code;
    }

    return SUCCESS;
}

RETURN_CODES write_simple_csv(const char *const file_path, const records_t *const records)
{
    FILE *fp = fopen(file_path, "w");

    if (fp == NULL)
    {
        int errornum = errno;
        fprintf(stderr, "Error in opening file: %s\n", strerror(errornum));
        return FAILURE;
    }

    for (unsigned int i = 0; i < records->length; i++)
    {
        const entry_t *const entry = &records->entries[i];
        int printed_caracters = fprintf(fp, "%c,%d\n", entry->letter, entry->value);

        if (printed_caracters < NUM_VALUES)
        {
            break;
        }
    }

    int return_close = fclose(fp);
    fp = NULL;

    if (return_close == EOF)
    {
        return FAILURE;
    }

    return SUCCESS;
}
