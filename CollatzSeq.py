def collatz(number):

    if number % 2 == 0:
        even = number // 2
        print(even)
        #Ensure to return even value and not number variabel
        return even

    else:
        odd = 3 * number + 1
        print(odd)
        return odd

#User input for number to collatz'd
request = input("Enter a number: ")

# Setting initial iteration point
try:
    iter = collatz(int(request))

    # Iterate over the given value to it reaches 1
    while iter != 1:
        iter = collatz(iter)

except:
    print("Please enter a number")
