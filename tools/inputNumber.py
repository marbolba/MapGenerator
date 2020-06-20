def inputNumber(text:str):
    val = 0
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            val = int(input(text))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return val