

def check_prime(mod):
    for i in range(2,mod):
        if mod % i == 0: return False
    return True







t_is_lessthan = True
mod_is_prime = True
n = int(input("people number: "))
MOD = int(input("MOD: "))
secret = int(input("secret: "))
t = int(input("threshold: "))

mod_is_prime = check_prime(MOD)
if t > n:
    print("Threshold t cannot be greater than the number of people n.")
    t_is_lessthan = False
