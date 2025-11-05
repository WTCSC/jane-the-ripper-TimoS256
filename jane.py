import hashlib

def crack(hash_file,word_file):
    hashes = {}
    output = set()
    with open(hash_file, 'r') as h:
        for line in h:
            hashes.update({line.strip(),''})
    with open(word_file, 'r') as w:
        for line in w:
            line = line.strip()
            hash_obj = hashlib.md5(line.encode())
            hash_hex = hash_obj.hexdigest()
            if hash_hex in hashes:
                print(f'< + > -Cracked! {hash_hex} --> {line.strip}')
                hashes.update({hash_hex,line.strip()})
            else:
                print(f'< x > -Failed! Could not find hash in words file. {hash_hex}')
                hashes.update({hash_hex,'fail'})
        print(output)
        print(len(output))
        return output
def main():
    print('--- Jane the Ripper ---')
    while True:
        #hash_path = input('Path to hash file:')
        #word_path = input('Path to word file:')

        hash_path = 'hashes.txt'
        word_path = 'wordlist.txt'

        conf = input(f'-- You"ve entered \n Hash file: {hash_path} \n Word file: {word_path} \n Is this correct? (y/n) >')
        if conf == 'y' or conf == '':
            crack(hash_path, word_path)
            break
main()