import random



def check_prime(mod):
    for i in range(2,mod):
        if mod % i == 0: return False
    return True


def create_share(secret, n, t, MOD):
    zarib = [random.randint(0, MOD) for _ in range(t-1)]
    zarib.insert(0, secret)  # The first coefficient is the secret
    shares = [(i, calculate_y(zarib, i, MOD, secret)) for i in range(1, n + 1)]
    return shares


def calculate_y(zarib, x, MOD, secret):
    result = 0
    power = 0
    for zari in zarib:
        now = 1
        for i in range(power):
            now= now * x
        result = result + (zari * now) 
        power = power + 1
    return result % MOD



def mod_inverse(a, MOD):
    m0 = MOD
    x0, x1 = 0, 1
    if MOD == 1:
        return 0
    while a > 1:
        q = a // MOD
        t = MOD
        MOD = a % MOD
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1


def restore_secret(shares, MOD):
    secret = 0
    k = len(shares)
    for i in range(k):
        xi, yi = shares[i]
        term = yi
        for j in range(k):
            if i != j:
                xj = shares[j][0]
                term *= xj
                term *= mod_inverse((xj - xi)% MOD , MOD)
        secret += term
    secret %= MOD
    return secret



t_is_lessthan = True
mod_is_prime = True
n = int(input("people number: "))
t = int(input("threshold: "))
MOD = int(input("MOD: "))
secret = int(input("secret: "))


mod_is_prime = check_prime(MOD)
if t > n:
    print("Threshold must be greater than number of people.")
    t_is_lessthan = False
elif not mod_is_prime:
    print("your mod must be prime")


if t_is_lessthan and mod_is_prime:
    shares = create_share(secret, n, t, MOD)

    print("people shares: ")
    for share in shares:
        print(f"x: {share[0]}, y: {share[1]}")

    print(f"\nEnter at least {t} shares to restore the secret:")
    entered_shares = []
    for i in range(t):
        x, y = map(int, input(f"share ({i + 1}) [x y]: ").split())
        entered_shares.append((x, y))

    restored_secret = restore_secret(entered_shares, MOD)
    print(f"restored secret: {restored_secret}")
