def encrypts(text, k, alp, new_alp):
    encrypted_text = ""
    for char in text:
        if char in alp:
            org_pos = alp[char]
            new_pos = (org_pos+ k) % 26 
            new_char = new_alp[new_pos]
            encrypted_text += new_char
            print(f"Character: {char}, Original Position: {org_pos}, New Character: {new_char}, New Position: {new_pos}")
        else:
            encrypted_text += char  
            print(f"Character: {char} is not an alphabet and remains unchanged.")
    print("Encrypted message:", encrypted_text)
def decrypts(text, k, alp, new_alp):
    decrypted_text = ""
    for char in text:
        if char in alp:
            org_pos = alp[char]
            new_pos = (org_pos - k ) % 26 
            new_char = new_alp[new_pos]
            decrypted_text += new_char
            print(f"Character: {char}, Original Position: {org_pos}, New Character: {new_char}, New Position: {new_pos}")
        else:
            decrypted_text += char  
            print(f"Character: {char} is not an alphabet and remains unchanged.")
    print("Decrypted message:", decrypted_text)
    
print("------------------____Ceaser Cipher Encryption Decryption_______-------------\n")
a = input("Enter a string: ").lower()
k = int(input("Enter key: "))
n = int(input("Enter choice\n 1. Encryption \n 2. Decryption\n"))
alp = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
}
new_alp = {v: k for k, v in alp.items()}
match n:
    case 1:
        encrypts(a, k, alp, new_alp)
    case 2:
        decrypts(a, k, alp, new_alp)
    case _:
        print("Invalid choice. Please enter 1 for Encryption or 2 for Decryption.")