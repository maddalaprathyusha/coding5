def lengthOfLastWord(s):
    length = 0
    found_last_word = False
    
    for char in reversed(s):
        if char.isalpha():
            length += 1
            found_last_word = True
        elif found_last_word:
            break
    
    return length

# Example usage:
input_str = "Hello World"
output = lengthOfLastWord(input_str)

print("Output:", output)
