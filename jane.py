import hashlib

def crack(hash_file,word_file):
    hashes = {}
    with open(hash_file, 'r') as h:
        for line in h:
            hashes.add(line.strip())
    hash_obj = hashlib.md5(word.encode())
    hash_hex = hash_obj.hexdigest()
    if
def main():


