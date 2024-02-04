def romanToInt(A):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in reversed(A):
        current_value = roman_numerals[char]
        
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result

# Example usage:
input_1 = "XIV"
input_2 = "XX"

output_1 = romanToInt(input_1)
output_2 = romanToInt(input_2)

print("Output 1:", output_1)
print("Output 2:", output_2)
