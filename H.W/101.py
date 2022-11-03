try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

    try:
        meaning = 42
        print(meaning / 0)
        print("the meaning of life")
    except (ValueError, TypeError):
        print("ValueError or TypeError occurred")
    except ZeroDivisionError:
        print("Divided by zero")

        try:
            variable = 10
            print(variable + "hello")
            print(variable / 2)
        except ZeroDivisionError:
            print("Divided by zero")
        except (ValueError, TypeError):
            print("Error occurred")

            try:
                variable = 10
                print(10 / 2)
            except ZeroDivisionError:
                print("Error")
            print("Finished")

            pin = input()
            try:
                # your code goes here
                int(pin)
                print("PIN code is created")

            except ValueError:
                # and here
                print("Please enter a number")