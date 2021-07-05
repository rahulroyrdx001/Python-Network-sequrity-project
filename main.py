
import hashlib

string_data = "Rahul Roy"


result = hashlib.md5(string_data.encode())


print("The hexadecimal equivalent of hash is : ", end ="")

print(result.hexdigest())
