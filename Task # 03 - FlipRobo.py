#!/usr/bin/env python
# coding: utf-8

# # Regular Expressions - Assessment

# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:

# In[8]:


import re
#Sample Text- 
text = 'Python Exercises, PHP exercises.'
#We can use re.sub() to replace the space, comma, or dot with a colon.
ExpectedOutput = re.sub(r'[ ,.]', ':', text)
print(ExpectedOutput)


# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six

# In[11]:


import pandas as pd
import re
#Given Dictionary
Dictionary={'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df = pd.DataFrame(Dictionary)
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\bXXXXX\b', '', text)
    text = text.strip()
    return text
df['SUMMARY'] = df['SUMMARY'].apply(clean_text)
print(df)


# As in the above output the Summary word is not to be shown that can only be possible if we rename the word with an empty string. 

# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.            

# In[14]:


import re
def find_long_words(Example):
    pattern = re.compile(r'\b\w{4,}\b')
    long_words = pattern.findall(Example)
    return long_words
Example = "Using Anaconda platform is easy and helpful"
result = find_long_words(Example)
print(result)


# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# 

# In[16]:


import re

def find_specific_length_words(Example):
    pattern = re.compile(r'\b\w{3,5}\b')
    matching_words = pattern.findall(Example)
    return matching_words
Example = "The dogs usually runs fast but stays calm on their trainer"
output = find_specific_length_words(Example)
print(output)


# Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientist
# 

# In[32]:


import re
def remove_parentheses(strings):
    pattern = re.compile(r'\s*\(.*?\)\s*')
    pattern = re.compile(r' \(|\)')
    cleaned_strings = []
    for string in strings:
        cleaned_string = pattern.sub('', string)
        cleaned_strings.append(cleaned_string.strip())  # strip() removes any leading/trailing spaces
    return cleaned_strings
Example = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
result = remove_parentheses(Example)
for r in result:
    print(r)


# Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 

# In[41]:


import re
def remove_parentheses_from_file(Path_File):
    with open(Path_File, 'r') as file:
        content = file.readlines()
    pattern = re.compile(r'\s*\(.*?\)\s*')
    cleaned_lines = []
    for line in content:
        cleaned_line = pattern.sub('', line).strip()
        cleaned_lines.append(cleaned_line)
    for cleaned_line in cleaned_lines:
        print(cleaned_line)
Example = ["example (.com)\n", 
    "hr@fliprobo (.com)\n", 
    "github (.com)\n", 
    "Hello (Data Science World)\n", 
    "Data (Scientist)\n"]
Path_File = 'sample_text.txt'
with open(Path_File, 'w') as file:
    file.writelines(sample_text)
remove_parentheses_from_file(Path_File)


# Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[46]:


import re
def split_by_uppercase(example):
    pattern = re.compile(r'[A-Z][a-z]*')
    words = pattern.findall(example)
    return words
example = "ImportanceOfRegularExpressionsInPython"
output = split_by_uppercase(example)
print(output)


# Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[60]:


import re
def insert_spaces(example):
    pattern = re.compile(r'(\d)([A-Z])')
    spaced_text = pattern.sub(r' \1\2', example)
    return spaced_text
example = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(example)
print(output)


# Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[61]:


import re
def insert_spaces(question):
    pattern = re.compile(r'(?<=[a-z0-9])(?=[A-Z0-9])')
    spaced_text = pattern.sub(' ', question)
    return spaced_text
question = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(question)
print(output)


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[62]:


import pandas as pd
githublink = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'
df = pd.read_csv(githublink)
print("Original DataFrame:")
print(df.head())
if 'Country' in df.columns:
    df['first_six_letters'] = df['Country'].apply(lambda x: x[:6])
    print("\nUpdated DataFrame with 'first_six_letters':")
    print(df.head())
else:
    print("The 'Country' column is not present in the DataFrame.")


# Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[4]:


import re
def string_match(s):
    pattern = r'^[A-Za-z0-9_]+$'
    if re.match(pattern, s):
        return "Valid string"
    else:
        return "Invalid string"
sample_string = "DATA TRAINED IS A GOOD EDUCATIONAL institute"
print(string_match(sample_string))


# Question 12- Write a Python program where a string will start with a specific number. 

# In[7]:


import re
def match_opening_number(s, number):
    pattern = f'^{number}.*'
    if re.match(pattern, s):
        return f"String starts with {number}"
    else:
        return f"String does not start with {number}"
sample_string = "965THE Union"
numbertomatch = 965
print(match_opening_number(sample_string, numbertomatch))
sample_string = "785The Union"
numbertomatch = 965
print(match_opening_number(sample_string, numbertomatch))


# Question 13- Write a Python program to remove leading zeros from an IP address

# In[9]:


def delete_zeros(ip):
    parts = ip.split('.')
    clean_parts = [str(int(part)) for part in parts]
    clean_ip = '.'.join(clean_parts)
    return clean_ip
ip_add = "232.132.009.008"
print(delete_zeros(ip_add))

ip_add = "050.090.060.090"
print(delete_zeros(ip_add))


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[12]:


import re
example_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'
with open('example.txt', 'w') as file:
    file.write(example_text)
with open('example.txt', 'r') as file:
    text = file.read()
date_pattern = r'\b([A-Z][a-z]+) (\d{1,2}(?:st|nd|rd|th)?) (\d{4})\b'
match = re.search(date_pattern, text)
if match:
    print("-", match.group())
else:
    print("No date found in the text.")


# Question 15- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[13]:


def search_words(text, words):
    for word in words:
        if word in text:
            print(f"'{word}' found in the text!")
        else:
            print(f"'{word}' not found in the text.")
example = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
search_words(example, searched_words)


# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[14]:


def search_and_find_location(text, word):
    index = text.find(word)
    if index != -1:
        print(f"'{word}' found in the text at index {index}.")
    else:
        print(f"'{word}' not found in the text.")
example = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'
search_and_find_location(example, searched_word)


# Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[15]:


import re
def find_substrings(text, pattern):
    matches = re.finditer(pattern, text)
    for match in matches:
        start_index = match.start()
        end_index = match.end()
        print(f"'{pattern}' found from index {start_index} to {end_index}.")
example = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
find_substrings(example, pattern)


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string. Using the same example as in Question 17.

# In[16]:


import re
def find_occurrences_and_positions(text, pattern):
    matches = re.finditer(pattern, text)
    for match in matches:
        start_index = match.start()
        end_index = match.end()
        print(f"'{pattern}' found at position {start_index}-{end_index-1}.")
example = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
find_occurrences_and_positions(example, pattern)


# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[17]:


def convert_date_format(date_str):
    year, month, day = date_str.split('-')
    converted_date = f"{day}-{month}-{year}"
    return converted_date
date_str = '2023-07-15'
print("Original date:", date_str)
print("Converted date:", convert_date_format(date_str))


# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[18]:


import re
def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    matches = pattern.findall(text)
    return matches
text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
print(find_decimal_numbers(text))


# Question 21- Write a Python program to separate and print the numbers and their position of a given string

# In[20]:


import re
def find_numbers_and_positions(text):
    pattern = re.compile(r'\d+')
    matches = pattern.finditer(text)
    for match in matches:
        number = match.group()
        start_index = match.start()
        end_index = match.end()
        print(f"Number: {number}, Position: {start_index}-{end_index-1}")
example = "The Amazing Spider man jumps over 123 the Naughty Iron Man 456 and 7890."
find_numbers_and_positions(example)


# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950
# 

# In[22]:


import re
def extract_max_numeric_value(text):
    pattern = re.compile(r'\d+')
    matches = pattern.findall(text)
    numbers = [int(match) for match in matches]
    if numbers:
        max_number = max(numbers)
        return max_number
    else:
        return None
example = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
print("Maximum numeric value:", extract_max_numeric_value(example))


# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[25]:


import re
def insert_spaces(text):
    pattern = re.compile(r'(?<=[a-z])(?=[A-Z])')
    spaced_text = pattern.sub(' ', text)
    return spaced_text
example = "RegularExpressionIsAnImportantTopicInPython"
print(" ", insert_spaces(example))


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[28]:


import re
def find_ufbl(text):
    pattern = re.compile(r'[A-Z][a-z]+')
    matches = pattern.findall(text)
    return matches
example = 'Here Is an Example Using Words Like Regex and Python'
print("Matches:", find_ufbl(example))


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 

# In[30]:


import re
def remove_c_dup(text):
    pattern = re.compile(r'\b(\w+)\s+\1\b', re.IGNORECASE)
    result = pattern.sub(r'\1', text)
    return result
example = "Hello hello world world"
output = remove_c_dup(example)
print(output)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




