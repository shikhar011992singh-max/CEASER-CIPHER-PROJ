# CEASER CIPHER PROJ...

def encrypt(message, key):#encypt== to make statemnt unreadable//codeble form..
      result = ""
      for char in message:
            if char.isalpha():

                 base = ord('A') if char.isupper() else ord('a')
                 shifted = (ord(char) - base + key) % 26 + base
                 result += chr(shifted)

            else:
                 result += char
      return result

def decrypt(message, key): #DECRYPT == TO MAKE FILES DECODE//READABLE..
      return encrypt(message, -key)

print("secret message")
choice = input("do you want E or D").strip().lower()

if choice == "e":
      text = input("enter your message: \n")
      try:
            key = int(input("enter number between 1 and 25: "))
            encrypted = encrypt(text, key)
            print("encryted message: ")
            print(encrypted)
      except ValueError:
            print("invalid key")
elif choice == 'd':
      text = input("enter your message: \n")
      try:
            key = int(input("enter number between 1 and 25: "))
            decrypted = decrypt(text, key)
            print("decryted message: ")
            print(decrypted)
      except ValueError:
            print("invalid key")
else:
      print("invalid choice")