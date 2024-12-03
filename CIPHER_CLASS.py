global L2I,I2L,NUMB_FORWARD,NUMB_REVERSE
class CIPHER:
   
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))
    I2L = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    NUMB_FORWARD = dict(zip("1234567890", range(10)))
    NUMB_REVERSE = dict(zip(range(10), "1234567890"))
   
    def __init__(self, UserInput, Key):
        self.UserInput = UserInput
        self.Key = Key

    def ENCRYPT(self):

        ciphertext2 = ""
        for c in self.UserInput.upper():
            if c.isalpha():
                ciphertext2 += self.I2L[(self.L2I[c]+self.Key) % 26]
            else:
                ciphertext2 += c
        ciphertextwithnum2 = ""
        for d in ciphertext2.upper():
            if d.isnumeric():
                ciphertextwithnum2 += NUMB_REVERSE[(NUMB_FORWARD[d]+self.Key) % 10]
            else:
                ciphertextwithnum2 += d
            
        return ciphertextwithnum2

    def DECRYPT(self):
  
        ciphertext2 = ""
        for c in self.UserInput.upper():
            if c.isalpha():
                ciphertext2 += self.I2L[(self.L2I[c]-self.Key) % 26]
            else:
                ciphertext2 += c
        ciphertextwithnum2 = ""
        for d in ciphertext2.upper():
            if d.isnumeric():
                ciphertextwithnum2 += NUMB_REVERSE[(
                    NUMB_FORWARD[d]-self.Key) % 10]
            else:
                ciphertextwithnum2 += d
           
        return ciphertextwithnum2
    def READFILE(self):
        text=""
        with open(self.UserInput) as my_file:
            text=my_file.read()
            text=text.replace("\n"," ")
        return text
        

"""cipher=CIPHER("sample.txt")
x=cipher.READFILE()
print(x)

cipher=CIPHER(x,3)
print(cipher.ENCRYPT())"""