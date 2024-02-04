def reverseWords(A):
    words = A.split()  # Split the input string into a list of words
    reversed_words = reversed(words)  # Reverse the list of words
    result = ' '.join(reversed_words)  # Join the reversed words into a string
    
    return result

# Example usage:
input_1 = "the sky is blue"
input_2 = "this is ib"

output_1 = reverseWords(input_1)
output_2 = reverseWords(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
