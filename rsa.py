import sys

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 and is_prime(i) and is_prime(num // i):
            p = i
            q = num // i
            return p, q
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        return
    
    input_file = sys.argv[1]
    
    try:
        with open(input_file, r) as file:
            num = int(file.readline().strip())
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return
    except ValueError:
        print("Invalid input in the file. Only a single natural number greater than 1 is allowed.")
        return
    
    result = factorize(num)
    if result is None:
        print(f"Unable to factorize {num} into two prime numbers.")
    else:
        p, q = result
        print(f"{num}={p}*{q}")
    
if __name__ == "__main__":
    main()

