#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program asks the user to enter how many numbers they want to add
# Then the user inputs the number they want to user


def main():
    # this tells the user the sum of all the positive numbers they want to add
    loop_counter = 0
    answer = 0

    # input
    number_count = input("How many numbers are you going to add: ")

    # process & output
    try:
        integer_as_number = int(number_count)
        for loop_counter in range(integer_as_number):
            number_count_two = input("Enter a number to add: ")
            try:
                integer_as_number_two = int(number_count_two)
                if integer_as_number_two < 0:
                    continue
                answer = answer + integer_as_number_two
            except Exception:
                print("This is an invalid number!")
                break
            finally:
                print("")
        else:
            print("The sum of all of the positive numbers is = {0}!".format(answer))
            print("")
    except Exception:
        print("This is an invalid number!")
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
