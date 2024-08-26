def count_chars(string):
    char_count = {}
    for char in string:
        if char.isalpha():
            char = char.lower() 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

string = 'Happiness'
print(count_chars(string))

string = 'smiles'
print(count_chars(string))

