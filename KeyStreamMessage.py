#Runtime 3.5 python, anaconda interpter 

class KeyStream:

    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256


def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def encryptTwo(encrypt(key, message)):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def transmit(cipher):
 #Gobal Variables & Message
  key = KeyStream(10)
  message = "This is my message".encode()
  cipher = encrypt(key, message)
  cipher = transmit(cipher)

  print(message)
  