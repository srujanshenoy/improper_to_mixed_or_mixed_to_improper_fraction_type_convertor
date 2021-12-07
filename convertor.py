while True:
    mode = int(input("""select mode:
    1. mixed to improper
    2. improper to mixed"""))

    if mode == 1:

        print("you have entered mixed to improper mode.")
        print("\n\nW N/D")
        print("if you want to end, type End Now in any uppercase/ lowercse form into any feild.")
        Whole_part = input("\nW: ")
        if Whole_part.lower() == "end now":
            print("OK. Ending now...")
            break
        else:
            Whole_part_int = int(Whole_part)

        print(f"You have entered: {Whole_part_int} N/D")

        Numerator_of_input = input("\nN: ")

        if Numerator_of_input.lower() == "end now":
            print("OK. Ending now...")
            break
        else:
            Numerator_of_input_int = int(Numerator_of_input)

        print(f"you have entered: {Whole_part} {Numerator_of_input}/D ")

        denominator_of_input = input("\nD: ")

        if denominator_of_input.lower() == "end now":
            print("OK. Ending now...")
            break
        else:
            denominator_of_input_int = int(denominator_of_input)

        if denominator_of_input_int == 0:
            print("invalid input. running fromom start!")
            continue
        print(
            f"you have entered: {Whole_part} {Numerator_of_input}/{denominator_of_input} ")

        numerator_of_output = Whole_part_int * \
            denominator_of_input_int+Numerator_of_input_int
        print(f"{Whole_part} {Numerator_of_input_int}/{denominator_of_input_int} = {numerator_of_output}/{denominator_of_input_int}")

    if mode == 2:
        while True:
            print("you have entered improper to mixed mode.")
            print("you have entered improper to mixed mode.")
            numerator_of_input = int(input("input the numerator: "))

            print(f"you have entered: {numerator_of_input} / D")
            denominator_of_input = int(input("input the denominator: "))

            if numerator_of_input < denominator_of_input:
                print(
                    "oops! this is not an improper fraction. runing program from start!.")
                continue
            elif denominator_of_input == 0:
                print("oops! invalid fraction. reruning...")
                continue

            print(
                f"you have entered: {numerator_of_input} / {denominator_of_input}")

            step_1_whole_of_output = numerator_of_input // denominator_of_input
            step_2_whole_of_output_or_numerator_of_output = numerator_of_input % denominator_of_input
            whole_of_output = step_1_whole_of_output
            denominator_of_output = denominator_of_input
            print(f"you entered: {numerator_of_input} / {denominator_of_input}\n answer: {whole_of_output} {step_2_whole_of_output_or_numerator_of_output} / {denominator_of_output}")
