import hashlib
import base64
import random

from cryptography.fernet import Fernet


class Diffie(object):
    def __init__(self, n=None, g=2, p=101):
        if n is None:
            self.n = random.getrandbits(32)
        else:
            self.n = n          # private number
            
        self.g = g              # generator
        
        # if self.is_prime(p):
        self.p = p          # prime modulus
        # else:
        #     raise ValueError('Prime modulus must be prime')
        
        self.pub = self.discrete_log(self.g, self.n, self.p)
        self.priv = None

    def __call__(self, pub):
        self.priv = self.discrete_log(pub, self.n, self.p)
        self.priv_hash = hashlib.md5(str(self.priv)).hexdigest()
        self.priv_b64 = base64.urlsafe_b64encode(self.priv_hash)
        self.priv_key = Fernet(self.priv_b64)

    def __str__(self):
        return '({}, {})'.format(self.pub, self.priv)

    def __repr__(self):
        return 'Diffie({}, {}, {})'.format(self.n, self.g, self.p)
        
    def discrete_log(self, g, n, p):
        return pow(g, n, p)

    # @staticmethod
    # def is_prime(n):
    #     for i in xrange(2, int(n**.5)+1):
    #         if n % i == 0:
    #             return False
    #     return True
