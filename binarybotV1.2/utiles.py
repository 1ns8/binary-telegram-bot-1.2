class binary():
    def __init__(self) -> None:
        pass
    def into_binary(self, text):
        binary_string = ' '.join(format(ord(char), '08b') for char in text)
        return binary_string

    # Create a function to turn binary code into a text message
    def binary_to_string(self, binary_string):
        binary_values = binary_string.split()
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        original_string = ''.join(ascii_characters)
        return original_string
