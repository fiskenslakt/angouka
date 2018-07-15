class Diffie(object):
    def __init__(self, n, g=2, p=101):
        self.n = n              # private number
        self.g = g              # generator
        if self.is_prime(p):
            self.p = p          # prime modulus
        else:
            raise ValueError('Prime modulus must be prime')
        self.pub = self.discrete_log(self.g, self.n, self.p)
        self.priv = None

    def __call__(self, pub):
        self.priv = self.discrete_log(pub, self.n, self.p)

    def __str__(self):
        return '({}, {})'.format(self.pub, self.priv)

    def __repr__(self):
        return 'Diffie({}, {}, {})'.format(self.n, self.g, self.p)
        
    def discrete_log(self, g, n, p):
        return pow(g, n, p)

    @staticmethod
    def is_prime(n):
        for i in xrange(2, int(n**.5)+1):
            if n % i == 0:
                return False
        return True
