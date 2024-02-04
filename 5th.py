def addBinary(a, b):
    result = ""
    carry = 0
    
    len_a, len_b = len(a), len(b)
    max_len = max(len_a, len_b)
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
    
    if carry:
        result = "1" + result
    
    return result

# Example usage:
a = "100"
b = "11"

result = addBinary(a, b)

print("Result:", result)
