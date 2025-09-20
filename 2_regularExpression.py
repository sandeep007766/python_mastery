import re

#Find all
text = "The quick brown fox found brownie"
pattern = r"brown"

findall = re.findall(pattern, text) #Returns a list of all matches (strings) found in the input
if findall:
    print("Pattern found:", findall)
else:
    print("Pattern not found")

#Match
text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text) #Searches only at the beginning of the string
if match:
    print("Match found:", match.group())
else:
    print("No match")

#Replace
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text) #replace parts of a string
print("Modified text:", new_text)

#Search
text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text) #Searches throughout the entire string
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


#Split
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text) #Split the words in string using ','
print("Split result:", split_result)
