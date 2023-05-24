import sys

def factorize(num):
    factors = []
    for i in range(2, int(num**0.5) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return
    
    input_file = sys.argv[1]
    
    try:
        with open(input_file, r) as file:
            numbers = [int(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return
    except ValueError:
        print("Invalid input in the file. Only natural numbers greater than 1 are allowed.")
        return
    
    for num in numbers:
        factors = factorize(num)
        if len(factors) >= 2:
            p = factors[0]
            q = factors[1]
            print(f"{num}={p}*{q}")
    
if __name__ == "__main__":
    main()

