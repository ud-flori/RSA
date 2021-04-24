"""
    Main method for testing

    Demonstrates the steps in RSA algorithm
    You can check also the efficienty of the algorithm with the time calculation steps

    The decryption has two version:
     1, Chinese Remainder Theorem
     2, Fast Modular Exponentiation

     For testing the program with other RSA public key bit length, modify the parameter in the 28. line

     Use only for educational purpose.
        Project was made for a College project.
        No warranty, may occur side effects.
        Program is in test phase.
        Algorithm worsk well, efficiently with 512 bit key generation
        
        Project by: Zselenák Flórián
"""
from rsa import RSA
import timeit
import math
import random
import time

if __name__ == '__main__':
   
    p = 0

    rsa_object = RSA()

    print("[+] Generating keys! Be patient! :) ")
    print()
    start = timeit.default_timer()
    rsa_object.generate_keys(512)
    stop = timeit.default_timer()
    print("[i] Keys generated!")
    print('[+] Elapsed time:', stop-start)
    print()
    print("[i] Your public key is: ")
    time.sleep(.5)
    print(rsa_object.get_elements())
    print()
    raw_text = input("Write a message to encrypt: ")
    start = timeit.default_timer()
    rsa_object.encrypt(raw_text)
    stop = timeit.default_timer()
    time.sleep(.2)
    print("[i] Your message has been encrypted.")
    print("[+] Elapsed time:", stop-start)
    time.sleep(1)
    print()
    print("[i] Decoding message...")
    start = timeit.default_timer()
    rsa_object.decrypt()
    stop = timeit.default_timer()
    print("[i] Decoded message with chinese remainder theorem:")
    print("[i] ", rsa_object.decrypted_text)
    print("[+] Elapsed time: ", stop-start)
    print()
    print("[i] Decoded message with Fast Modular Exponentiation:")
    start = timeit.default_timer()
    rsa_object.decrypt2()
    stop = timeit.default_timer()
    print("[i] ", rsa_object.decrypted_text)
    print("[+] Elapsed time: ", stop-start)