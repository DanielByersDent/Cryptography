#Runtime 3.5 python, anaconda interpter 
import random
class one_time_pad:

    def generate_key_stream(self, n):
        return bytes([random.randrange(0, 256) for i in range(n)])


    def xor_bytes(self,key_stream, message):
        length = min(len(key_stream), len(message))
        return bytes([key_stream[i] ^ message[i] for i in range(length)])

message = "One time message!"
message = message.encode()
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, n)
print(key_stream)
print(xor_bytes(key_stream,cipher))





