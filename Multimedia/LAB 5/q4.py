# Implement run length encoding.
def run_length_encoding(data):
    encoding = []
    prev_char = ""
    count = 1

    if not data: return []

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding.append((prev_char, count))
            count = 1
            prev_char = char
        else:
            count += 1
    encoding.append((prev_char, count))
    return encoding

# Example usage
data = "AAAABBBCCDAA"
encoded_data = run_length_encoding(data)
print(encoded_data)
