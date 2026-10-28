
n = int(input("Enter total number of objects (n): "))
r = int(input("Enter number of objects to select (r): "))

if n < 0 or r < 0 or r > n:
    print("Invalid input!")
else:
    fact_n = 1
    fact_r = 1
    fact_nr = 1

    for i in range(1, n + 1):
        fact_n *= i

    for i in range(1, r + 1):
        fact_r *= i

    for i in range(1, n - r + 1):
        fact_nr *= i

    permutation = fact_n // fact_nr
    combination = fact_n // (fact_r * fact_nr)

    print("Permutation =", permutation)
    print("Combination =", combination)
