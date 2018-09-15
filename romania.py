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
    e = 10001
    print(e,phi)

    d = multiplicative_inverse(e, phi)
    return (n, e, d)


def rsa_encrypt(message, n, e):
    return power(message, e, n)


def rsa_decrypt(cipher, n, d):
    return power(cipher, d, n)
def power(x, m, n):
    """Calculate x^m modulo n using O(log(m)) operations."""
    a = 1
    while m > 0:
        if m % 2 == 1:
            a = (a * x) % n
        x = (x * x) % n
        m //= 2
    return a
binary_file =open("data", "rb")
msg= binary_file.read()
(n,e,d)=rsa_generate_key()
print(msg,n,d)
