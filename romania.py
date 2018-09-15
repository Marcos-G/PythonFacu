def extended_gcd(a, b):
    """Returns pair (x, y) such that xa + yb = gcd(a, b)"""
    x, lastx, y, lasty = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, lastx = lastx - q * x, x
        y, lasty = lasty - q * y, y
    return lastx, lasty


def multiplicative_inverse(e, n):
    """Find the multiplicative inverse of e mod n."""
    x, y = extended_gcd(e, n)
    if x < 0:
        return n + x
    return x


def rsa_generate_key():
    p = 1094782941871623486260250734009229761
    q = 57248512388615138300979959427360676128469
    # Ensure q != p, though for large values of bits this is
    # statistically very unlikely
    
    n = p * q
    phi = (p - 1) * (q - 1)
    # Here we pick a random e, but a fixed value for e can also be used.
    while True:
        e = 10001
        if fractions.gcd(e, phi) == 1:
            break
    d = multiplicative_inverse(e, phi)
    return (n, e, d)


def rsa_encrypt(message, n, e):
    return modular.power(message, e, n)


def rsa_decrypt(cipher, n, d):
    return modular.power(cipher, d, n)
msg="<UËA9 |u2dJ<e¢sDaž¬ù§Zú"
(n,e,d)=rsa_generate_keys
