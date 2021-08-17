import string 

# Remove punctuation:
def remove_punctuation(text):
    for punctuation in string.punctuation:
        text = text.str.replace(punctuation, '') 
    return text

# All lower case:
def lower_all(text):
    return text.str.lower()

# Remove numbers:
def remove_numbers(text):
    return text.str.replace('\d+', '')