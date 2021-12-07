# credit to shwethab to fixing my program! (thanks hodeaayee)
while True:
    print("you have entered improper to mixed mode.")
    numerator_of_input = int(input("input the numerator: "))

    print(f"you have entered: {numerator_of_input} / D")
    denominator_of_input = int(input("input the denominator: "))

    if numerator_of_input < denominator_of_input:
        print("oops! this is not an improper fraction. runing program from start!.")
        continue
    elif denominator_of_input == 0:
        print("oops! invalid fraction. reruning...")
        continue

    print(f"you have entered: {numerator_of_input} / {denominator_of_input}")

    step_1_whole_of_output = numerator_of_input // denominator_of_input
    step_2_whole_of_output_or_numerator_of_output = numerator_of_input % denominator_of_input
    whole_of_output = step_1_whole_of_output
    denominator_of_output = denominator_of_input
    print(f"you entered: {numerator_of_input} / {denominator_of_input}\n answer: {whole_of_output} {step_2_whole_of_output_or_numerator_of_output} / {denominator_of_output}")
