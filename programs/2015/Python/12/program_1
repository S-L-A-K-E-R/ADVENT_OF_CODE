# --- ADVENT OF CODE ---
#  
# 2025-12
# "JSAbacusFramework.io"
# 
# Date: 2026/09/06 
# ----------------------

# --- LIBRAIRIES & DEPENDENCIES
from pathlib import Path


# --- GLOBAL VARIABLES
FILE_SELECTED = "input"
INPUT_PATH = Path(f"programs/2015/Python/12/{FILE_SELECTED}.txt")


# --- FUNCTIONS

def readFile() -> str:

    with open( INPUT_PATH, "r") as file:
        data = file.read().strip()

    return data


def sumAllNumberInString(input: str) -> int:

    index = 0
    sum_buffer = 0

    while index < len(input):

        if input[index].isdigit() or (input[index] == "-" and input[index+1].isdigit()):

            found_number_text = ""

            # Only for the first "- ...", we add it specially to the string.
            # This avoids the problem like: "-458-"... wrongly taking the latest "-".
            if input[index] == "-":
                found_number_text += "-"
                index += 1

            # Now let's unravel the string until we find the full number
            while input[index].isdigit() :
                found_number_text += input[index]
                index += 1

            # print(f"FINAL: {found_number_text}")

            """
            LEGACY CODE: Had an issue with int() but fixed it!
            # --- CONVERT (str) TO (int) (taking into)
            found_number_int: int

            if( found_number_text[0] == "-"):
                found_number_int = (-1) * int(found_number_text[1:])

            else:
                found_number_int = int(found_number_text)
            """

            sum_buffer += int(found_number_text)

        else:
            index += 1


    return sum_buffer



# --- main()
def main() -> int:

    input = readFile()

    number_sum = sumAllNumberInString(input)

    print("\n")
    print(f"SUM of all number = {number_sum}")

    return 0



# --- Main launcher
if __name__ == "__main__":
    main()


