def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character by the specified amount
            char_code = ord(char)
            shifted_char = chr((char_code - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))
            
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result

# Example usage
plaintext = "Hello, World!"
shift_amount = 3
cipher_text = caesar_cipher(plaintext, shift_amount)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {cipher_text}")
