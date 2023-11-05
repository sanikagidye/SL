def vigenere_encrypt_with_steps(plaintext, keyword): 
    encrypted_text = ""     
    keyword = keyword.upper()     
    keyword_index = 0 
    encryption_steps = [] 
 
    for char in plaintext:         
        if char.isalpha():             
            key_shift = ord(keyword[keyword_index]) - ord('A')             
            if char.islower():                 
                base = ord('a')             
            else: 
                base = ord('A') 
            encrypted_char = chr((ord(char) - base + key_shift) % 26 + base)
            encryption_steps.append((char, keyword[keyword_index], key_shift, encrypted_char))             
            keyword_index = (keyword_index + 1) % len(keyword)         
        else: 
            encrypted_char = char 
        encrypted_text += encrypted_char 
     
    return encrypted_text, encryption_steps 
 
def main():     
    plaintext = input("Enter the plaintext: ")     
    keyword = input("Enter the keyword: ") 
     
    encrypted, steps = vigenere_encrypt_with_steps(plaintext, keyword) 
     
    print("\nEncryption Steps:")     
    print("Char | Key | Shift | Encrypted") 
    print("-" * 31)     
    for step in steps: 
        print(f"{step[0]}     | {step[1]}   | {step[2]:<5} | {step[3]}") 
 
    print("\nPlaintext:", plaintext)     
    print("Keyword:", keyword) 
    print("Encrypted:", encrypted) 
 
if __name__ == "__main__":     
    main() 
