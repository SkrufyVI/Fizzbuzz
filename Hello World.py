# Fizzbuzz Game: replace every number divisible by 3 with "Fizz". Replace every number divisible by 5 with "Buzz." Replace every number divisible by both 3 and 5 with "Fizzbuzz"

#def Fizzbuz(play_until):
def Fizzbuzz (play_until):
    i = 1
    while (i <= play_until):
        if (i % 5 == 0) and (i % 3 == 0):
            print("Fizzbuzz!")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
        i += 1
    return 0

Fizzbuzz(100)
