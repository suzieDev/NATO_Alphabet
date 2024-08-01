student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}


#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(f"{key}, {value}")
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(f"index: {index}, row data: {row["student"]}, {row["score"]}")
    pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
"""
When you use iterrows() to iterate over a DataFrame in pandas, it returns each row 
as a tuple containing the row index and a Series object representing the row’s data. 
This behavior is defined by the iterrows() method itself."""
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter your name: ").upper()
# 	For letter='A': phonetic_dict['A'] returns 'Alfa'
output = [phonetic_dict[letter] for letter in word]
print(output)
