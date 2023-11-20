def atbash_cipher(text):
    result = ""
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Convert the character to its ASCII value
            char_ascii = ord(char.lower())

            # Calculate the mirrored ASCII value
            mirrored_ascii = ord('a') + (ord('z') - char_ascii)

            # If the character was originally uppercase, convert back to uppercase
            if char.isupper():
                result += chr(mirrored_ascii).upper()
            else:
                result += chr(mirrored_ascii)
        else:
            # If the character is not a letter, keep it unchanged
            result += char

    return result


print(atbash_cipher("apple"))
