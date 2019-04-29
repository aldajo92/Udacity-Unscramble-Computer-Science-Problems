"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

different_records = []


def element_exist_in_array(element, array):
    if element not in array:
        array.append(element)
    return array


for text in texts:
    element_exist_in_array(text[0], different_records)
    element_exist_in_array(text[1], different_records)
    # if text[0] not in different_records:
    #     different_records.append(text[0])
    # if text[1] not in different_records:
    #     different_records.append(text[1])

for call in calls:
    element_exist_in_array(call[0], different_records)
    element_exist_in_array(call[1], different_records)
    # if call[0] not in different_records:
    #     different_records.append(call[0])
    # if call[1] not in different_records:
    #     different_records.append(call[1])

print("There are {} different telephone numbers in the records.".format(len(different_records)))
