while True:
    print("\n\nW N/D")
    print("if you want to end, type End Now exactly into any feild.")
    Whole_part = input("\nW: ")
    if Whole_part == "End Now":
        print("OK. Ending now...")
        break
    else:
        Whole_part_int = int(Whole_part)

    Numerator_of_input = input("\nN: ")

    if Numerator_of_input == "End Now":
        print("OK. Ending now...")
        break
    else:
        Numerator_of_input_int = int(Numerator_of_input)
    denominator_of_input = input("\nD: ")

    if denominator_of_input == "End Now":
        print("OK. Ending now...")
        break
    else:
        denominator_of_input_int = int(denominator_of_input)

    numerator_of_output = Whole_part_int * \
        denominator_of_input_int+Numerator_of_input_int
    print(f"{Whole_part} {Numerator_of_input_int}/{denominator_of_input_int} = {numerator_of_output}/{denominator_of_input_int}")
