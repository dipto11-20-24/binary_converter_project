
def text_to_binary(text):
    binary_output = " ".join(format(ord(char), "08b") for char in text)
    return binary_output

user_input = input("Enter a string:")
binary_result = text_to_binary(user_input)

print("Binary representation:", binary_result)
print(binary_result)





































