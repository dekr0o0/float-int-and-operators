n = int(input())

Ed = n % 10
n //= 10
Des = n % 10
n //= 10
Hun = n % 10
n //= 10
Th = n % 10
n //= 10
Des_th = n % 10


r = ((Des ** Ed) * Hun) // (Des_th - Th)
print(r)