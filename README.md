# Jane the Ripper
- A simple MD5 hash cracking dictionary attacker.

## Installation
- Simply clone the repo,
```sh
git clone https://github.com/WTCSC/jane-the-ripper-TimoS256.git
```
- Navigate to the new directory
```sh
cd jane-the-ripper-TimoS256
```
- Run the file
```sh
python3 jane.py
```
### Usage
You will need 2 things:
- A file with your hashes
- A file with a bunch of words to check the hashes for. 
- The program will ask you for both of these filenames, called the hash file and the word file. Type in these files, and if you typed a valid path, the hashes will be cracked!

## Requirements
- Python 3
- A file with "your" hashes to crack.
- A wordlist file
