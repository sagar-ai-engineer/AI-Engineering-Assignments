def fizzbuzz(n):
    for i in range(0,n):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3==0 and i%5!=0:
            print("Fizz")
        elif i%3!=0 and i%5==0:
            print("Buzz")
        else: print(str(n))


n = int(input("Enter an integer:"))
fizzbuzz(n)




