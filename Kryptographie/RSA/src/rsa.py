from prime import generate_params


class RSA:
    n = 0
    d = 0
    e = 0

    def __init__(self, seed=42, lb=3, ub=100):
        self.n, self.d, self.e = generate_params(seed, lb, ub)

    def encryption(self, message):
        res = pow(message, self.e, self.n)
        return res

    def decryption(self, message):
        res = pow(message, self.d, self.n)
        return res

    def get_key_pub(self):
        return (self.n, self.e)

    def get_key_pr(self):
        return (self.n, self.d)
