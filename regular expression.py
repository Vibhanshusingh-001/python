import re

# Define a text string
text = "The quick brown fox jumps over the lazy dog."

# Define a regular expression pattern to search for words containing 'o'
pattern = r'\b\w*o\w*\b'

# Use re.findall() to find all matches of the pattern in the text
matches = re.findall(pattern, text)

# Print the matches
print("Words containing 'o':", matches)
