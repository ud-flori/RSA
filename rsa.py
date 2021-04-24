import random
import sys

"""
        RSA Object for implementing RSA algorithm object oriented.

        Use only for educational purpose.
        Project was made for a College project.
        No warranty, may occur side effects.
        Program is in test phase.
        Algorithm worsk well, efficiently with 512 bit key generation
        
        Project by: Zselenák Flórián
"""

class RSA:
    """RSA Class for the implementation
    """

    def get_elements(self):
        """Get method for public key

        Returns:
            RSA.keys: Return RSA object with "n" and "e" values (The public key)
        """
        return self.keys

    def get_cipher(self):
        """Get method for encrypted text

        Returns:
            string: Return encoded string object
        """
        return self.cipher

        
    def get_primes(self):
        """Get method for p and q primes

        Returns:
            int: Return first prime - P
            int: Return second prime - Q
        return self.p,self.q

        """

    def __gcd_extended(self,a, b): 
        """Extended euclidean algorithm implementation

        Args:
            a (int): integer with value of the first number
            b (int): integer with value of the second number

        Returns:
            int: Return the greatest common divisor
            int: Return x
            int: Return y
        """
        if a == 0 :  
            return b,0,1
             
        gcd,x1,y1 = self.__gcd_extended(b%a, a) 
     
        x = y1 - (b//a) * x1 
        y = x1 
     
        return gcd,x,y


    def decimal_to_binary(self,decimal):
        """Function that return binary form of decimal number

        Args:
            decimal (int): Decimal number input

        Returns:
            int: Return the binary form of decimal number
        """
        binary_buffer = [] 

        binary_buffer.append(str(decimal % 2))
        decimal = decimal // 2

        while decimal:
            binary_buffer.append(str(decimal % 2))
            decimal = decimal // 2

        return "".join(binary_buffer[::-1])


    def __fast_exp_mod(self,a,k,m):
        """Fast Modular Exponentiation algorithm

        Args:
            a (int): The first argument stands for the base
            k (int): The second argument stands for the exponential part
            m (int): The third argument is the modulo

        Returns:
            int: Return a**k mod n 
        """
        k = self.decimal_to_binary(k)

        result = 1
        l = len(k)-1
        i = 0
        for i in range(len(k)):
            a = a % m
            if (k[l-i] == "1"):
                result *= a
        
            a = a**2

        
        return result % m
                                           


    def __is_prime(self,p):
        """Function to test numbers if its prime

        Args:
            p (int): Number to test

        Returns:
            bool: Return a logical value of the primality test
        """
        if (p <= 1 or p == 4):
            return False;
        if (p <= 3):
            return True;
        
        S = 0
        d = p-1

        while(d % 2 == 0):
            S += 1    
            d //= 2

        if(self.__miller_algorithm(p,S,d)):
            return True
        else:
            return False

    def __miller_algorithm(self,p,S,d):
        """Miller Rabin primality test for efficient primality testing

        Args:
            p (int): The first argument is the number
            S (int): The second argument is the precalculated S
            d (int): The third argument is the precalculated d

        Returns:
            bool: Return the value of the primality test
        """

        a = 3
        x = self.__fast_exp_mod(a,d,p)
        if (x == 1 or x == p - 1):
            return True;

        while (d != p - 1):
            x = (x * x) % p;
            d *= 2; 
        if (x == 1):
            return False;
        if (x == p - 1):
            return True;

        return False          


    def generate_keys(self,bits):
        """Function for generating RSA keys

        Args:
            bits (int): RSA public keys bit storage
        """

        while(True):
            p = random.getrandbits(bits)
            if(self.__is_prime(p)):
                self.p = p
                break

        while(True):
            q = random.getrandbits(bits)
            if(self.__is_prime(q)):
                self.q = q
                break
        
        phi_n = (p-1)*(q-1)
        self.n = p*q

        while(True):
            e = random.randrange(2,phi_n)
            gcd,x,y = self.__gcd_extended(e,phi_n)
            if(gcd == 1):
                self.d = x % phi_n
                self.e = e
                break
               
        self.keys = {'n': p*q, 'e' : e}
        


    def encrypt(self, message):
        """Function for encrypt message

        Args:
            message (string): String message to encrypt
        """
        self.cipher = ""
        self.cipher = [self.__fast_exp_mod(ord(char),self.keys.get("e"),self.keys.get("n")) for char in message]

    def decrypt(self):
        """Method for decrypt message using chinese remainder theorem
            Using the RSA components encrypted object for decryption
            Save the decypted text in a string            
        """
        self.decrypted_text = ""
        l = len(self.cipher)
        i = 0
        while i < l:
            x = self.chinese_theorem(self.cipher[i])
            y = chr(x) 
            self.decrypted_text += y
            i+=1

    def decrypt2(self):
        """Method for decrypt message using Fast Modular Exponentiation
            Using the RSA components encrypted object for decryption
            Save the decypted text in a string    
        """
        self.decrypted_text = ""
        l = len(self.cipher)
        i = 0
        while i < l:
            x = self.__fast_exp_mod(self.cipher[i],self.d,self.keys.get("n"))
            y = chr(x) 
            self.decrypted_text += y
            i+=1


    def chinese_theorem(self, c):
        """Chinese Remainder Theorem for efficient decryption

        Args:
            c (string): The input is the encrypted message
            Works with RSA object components

        Returns:
            int: Returns the decrypted message
        """
        dp = self.d % (self.p-1)
        dq = self.d % (self.q-1)
        mp = self.__fast_exp_mod(c,dp,self.p)
        mq = self.__fast_exp_mod(c,dq,self.q)
        gcd, x, y = self.__gcd_extended(self.p,self.q)

        f = (mp*y*self.q + mq*x*self.p)

        return f % self.n