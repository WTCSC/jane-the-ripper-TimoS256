import hashlib
import os

def crack(hash_file,word_file):
    hashes = {}
    with open(hash_file, 'r') as h:
        for line in h:
            hashes[line.strip()] = None
    with open(word_file, 'r') as w:
        for line in w:
            line = line.strip()
            hash_obj = hashlib.md5(line.encode())
            hash_hex = hash_obj.hexdigest()
            if hash_hex in hashes:
                print(f'< + > -Cracked! {line.strip()} <-- {hash_hex}')
                hashes.update({hash_hex:line.strip()})
        for x in hashes:
            if hashes[x] == None:
                print(f'< x > -Failed! Could not find hash in words file. {hash_hex}')
                hashes.update({x:'Failed!'})
        print(hashes)
        print(len(hashes))
        return hashes
def main():
    print('--- Jane the Ripper ---')
    while True:
        hash_path = input('Path to hash file:')
        if not os.path.exists(hash_path):
            print("Hash path invalid!")
            main()
        word_path = input('Path to word file:')
        if not os.path.exists(word_path):
            print("Word file path invalid!")
            main()
        #hash_path = 'hashes.txt'
        #word_path = 'wordlist.txt'

        conf = input(f'-- You"ve entered \n Hash file: {hash_path} \n Word file: {word_path} \n Is this correct? (y/n) >')
        if conf == 'y' or conf == '':
            crack(hash_path, word_path)
            break
if __name__ == "__main__":
    main()