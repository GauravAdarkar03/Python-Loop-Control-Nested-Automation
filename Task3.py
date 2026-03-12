
print("\n----- Number Pattern Generator -----")

number = 1

while number <= 20:

    if number % 3 == 0 and number % 5 ==0:
        number += 1
        continue
    elif number % 3 == 0:
        print(f"{number}: FIZZ")
    elif number % 5 == 0:
        print(f"{number}: BUZZ")

    else:
        print(number)
    number  += 1