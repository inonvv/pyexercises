# input variables
temp = 20
is_raining = False

# output variables
hat = False
umbrella = False
coat = False

# Check temperature
if temp > 15:
    # In case it is hot
    hat = True
    coat = False
else:
    # In case it is not hot
    hat = False
    coat = True

# Check if raining
if is_raining:
    # If it's raining
    umbrella = True
else:
    # If it's not raining
    umbrella = False

# Print results
if hat:
    print("You should take a hat")
else:
    print("You shouldnt take a hat")

if coat:
    print("You should take a coat")
else:
    print("You shouldnt take a coat")

if umbrella:
    print("You should take an umbrella")
else:
    print("You shouldnt take an umbrella")

    a = 1 * 1
    b = 1 + 0
    c = 8 - 7
    if a == b == c:
        print("yay hrray")
    else:
        print("not not good")

    x = 10
    st = "hello"
    if not x >= 10:
        print("x is small")
    elif x > 10 and not len(st) > 20:
        print("st is short")
    elif not (x > 10 or len(st) > 20):
        print("x is small and st is short")
    else:
        n = len("This is a string")
        print(n)
        if n > 10:
            print("this is a long string")
        elif n < 5:
            print("This is a short string")
