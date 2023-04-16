import hashlib

def compute_SHA1_hash(string, encoding='utf-8'):
    encoded_string = string.encode(encoding)
    # print(encoded_string)
    hash_object = hashlib.sha1(encoded_string)
    sha_1_sign = hash_object.hexdigest()
    return sha_1_sign


count = 0
with open("passwords.txt") as passwords:
    with open("hashes.txt", "w") as hashed:
        for line in passwords:
            count+=1
            filtered_line = line[:-1]
            hashed.write(compute_SHA1_hash(filtered_line)+"\n")
print(count)