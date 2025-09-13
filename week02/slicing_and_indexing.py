prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print("Middle five primes:",prime_numbers[2:7])
print("Every second prime:",prime_numbers[::2])
print("Last three primes:",prime_numbers[-3:])
print("Reversed list:",prime_numbers[::-1])
prime_numbers.sort(reverse=True)
print("Sorted descending order:",prime_numbers)
