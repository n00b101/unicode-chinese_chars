# Ask the user to input a Unicode escape string
unicode_string = input("Enter a Unicode string with escape sequences (e.g., \\u300a\\u5730\\u7403\\u98de\\u884c): ")

# Convert and print the corresponding characters
decoded_string = unicode_string.encode('utf-8').decode('unicode_escape')

# Display the result
print("Decoded string:", decoded_string)
