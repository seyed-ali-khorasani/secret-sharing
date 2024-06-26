import random



def check_prime(mod):
    for i in range(2,mod):
        if mod % i == 0: return False
    return True


def create_share(secret, n, t, MOD):
    zarib = [random.randint(0, MOD) for _ in range(t-1)]
    return shares







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

    