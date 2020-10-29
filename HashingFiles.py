from __future__ import print_function
import argparse
import hashlib
import os

Editor = [" "]
When = " "
Brief = " "

available_algorithms = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
}

parser = argparse.ArgumentParser(
    description=Brief,
    epilog="Edited by {} on {}".format(", ".join(Editor), When)
)

parser.add_argument("FILE", help="File To Hash")
parser.add_argument("ALG", help="Hashing Function To Deploy",
                    choices=sorted(available_algorithms.keys()))
args = parser.parse_args()

input_file = args.FILE
hash_alg = args.ALG

file_name = available_algorithms[hash_alg]()
abs_path = os.path.abspath(input_file)
file_name.update(abs_path.encode())

print("The {} Hash Value of the filename is: {}".format(
    hash_alg, file_name.hexdigest()))

file_content = available_algorithms[hash_alg]()
with open(input_file, 'rb') as open_file:
    buff_size = 1024
    buff = open_file.read(buff_size)

    while buff:
        file_content.update(buff)
        buff = open_file.read(buff_size)

print("The {} Hash Value of the content is: {}".format(
    hash_alg, file_content.hexdigest()))

###Special Thanks to The Python Digital Forensics CookBook By Preston Miller and Chapin Bryce for the code examples###
