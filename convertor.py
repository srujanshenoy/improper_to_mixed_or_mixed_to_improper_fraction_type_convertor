while True:
    print("W N/D")
    print("if you want to end, type End Now exactly into any feild.")
    Whole_part = input("W: ")
    if Whole_part == "End Now":
        print("OK. Ending now...")
        break

    Numerator_of_input = input("N: ")

    if Numerator_of_input == "End Now":
        print("OK. Ending now...")
        break
    else:
        Numerator_of_input_int = int(Numerator_of_input)
    denominator_of_input = input("D: ")

    if denominator_of_input == "End Now":
        print("OK. Ending now...")
        break
    else:
        denominator_of_input_int = int(denominator_of_input)

    numerator_of_output = Whole_part*denominator_of_input+Numerator_of_input
    print(f"{Whole_part} {Numerator_of_input_int}/{denominator_of_input_int} = {numerator_of_output}/{denominator_of_input_int}")
