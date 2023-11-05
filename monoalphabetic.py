alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(plain_text,key):
    cipher_text=""
    for char in plain_text:
        if char.isalpha():
            if char==" ":
                cipher_text+="#"
            else:
                is_upper=char.isupper()
                char=char.lower()
                index=alphabet.index(char)
                index=(index+key)%26
                if is_upper:
                    cipher_text+=alphabet[index].upper()
                else:
                    cipher_text+=alphabet[index]
        else:
            cipher_text+=char
    return cipher_text
   
def decrypt(cipher_text,key):
    plain_text=""
    for char in cipher_text:
        if char.isalpha():
            if char==" ":
                plain_text+="#"
            else:
                is_upper=char.isupper()
                char=char.lower()
                index=alphabet.index(char)
                index=(index-key)%26
                if is_upper:
                    plain_text+=alphabet[index].upper()
                else:
                    plain_text+=alphabet[index]
        else:
            plain_text+=char
    return plain_text
plain_text=input("Enter plain text:")
key=int(input("Enter the key:"))
cipher_text=encrypt(plain_text,key)
decrypted_text=decrypt(cipher_text,key)
print("Encrypted text: ",cipher_text)
print("Decrypted text: ",decrypted_text)
