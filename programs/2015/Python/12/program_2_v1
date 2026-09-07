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

"""
LEGACY CODE:
This logic doesn't work.
Counter example: " {"n":10,"a":{"b":{"c":100}},"x":"red"} " becomes: " {"n":10,"a": " instead of "".
Because I'm not counting the depth and jumping directly to a wrong { position for further check.
"""
"""
def rfind_opening_cbracket(input: str, starting_pos: int) -> int:

    while True:

        previous_open_bracket   = input.rfind("{", 0, starting_pos)
        previous_close_bracket  = input.rfind("}", 0, starting_pos)

        # print(f"open = {previous_open_bracket}")
        # print(f"closing = {previous_close_bracket}")

        # We found the original opening bracket "{" that's not linked with something else
        if (previous_open_bracket > previous_close_bracket) :
            return previous_open_bracket

        # We are in this situation: { blabla, {...} test = "red"}
        #                                    ---
        #                                  wrong "{"!
        #                               closing > opening
        else: 
            starting_pos = previous_open_bracket

"""

"""
LEGACY CODE:
This logic doesn't work with this counter example:
" {"a":"red","b":{"c":{"d":100}},"e":5} "
Because I'm not counting the depth and jumping directly to a wrong } position for further check.
"""
"""
def find_closing_cbracket(input: str, starting_pos: int) -> int:

    while True:

        next_open_bracket   = input.find("{", starting_pos)
        next_close_bracket  = input.find("}", starting_pos)

        # print(f"open = {next_open_bracket}")
        # print(f"closing = {next_close_bracket}")

        # We found the original opening bracket "{" that's not linked with something else
        if (next_close_bracket < next_open_bracket) or (next_open_bracket == -1):
            return next_close_bracket

        # We are in this situation: { blabla, {...} test = "red"}
        #                                    ---
        #                                  wrong "{"!
        #                               closing > opening
        else: 
            starting_pos = next_close_bracket+1

"""
            
"""
LEGACY: I'm not using this anymore. I just kept it for historical reason when developping the new method.
For this function, I could use find()/rfind(), but I want something else.
I'll move in my string until I find "[" and "]" separately. 
Then, on my way, I'll count how many times I've seen curly brackets ({...}).
If I saw an odd/even amount of them, it will tell me whether I'm in a {...} or not.

Examples:
[ {test...} "red"]                          > EVEN      = ignore we keep the array
[ {test...}, {blue, red}, [heyy, "test"]]   > ODD       = we remove the inside: [ {test...}, , [heyy, "test"]]
{ {t1, t2...} [1, "red", blue], 2}          > EVEN      = ignore
{ [T1, T2] {[2,4,3], "red", [T3, T4] }
"""

def is_pos_in_array(input: str, starting_pos: int) -> bool:

    index = starting_pos

    square_bracket_encounter = 0
    curly_bracket_encounter = 0

    # Exploring the <<< side of the string
    while index>=0:

        input_letter = input[index]
        
        # We stop if we see a "[" or "{":
        if (input_letter in "[{") and (square_bracket_encounter == 0) and (curly_bracket_encounter == 0):

            return input_letter == "["


        elif input_letter == "]":
            square_bracket_encounter += 1

        elif input_letter == "[":
            square_bracket_encounter -= 1

        elif input_letter == "}":
            curly_bracket_encounter += 1

        elif input_letter == "{":
            curly_bracket_encounter -= 1


        # print(f"letter = {input_letter}, []counter = {square_bracket_encounter},C.counter = {curly_bracket_encounter}" )
        index -= 1

    # We haven't found any limit to it... that's an odd case.
    return False


def find_closing_cbracket(input: str, starting_pos: int) -> int:

    index = starting_pos
    curly_bracket_depth = 0
    while index < len(input):

        letter = input[index]
        
        if (letter == "}") and (curly_bracket_depth == 0):
            return index

        elif letter == "{":
            curly_bracket_depth += 1

        elif letter == "}":
            curly_bracket_depth -= 1

        index += 1

    # If we're here without ever reaching return, there has been an error.
    # We didn't find the remaining closing bracket!!
    return -1


def rfind_opening_cbracket(input: str, starting_pos: int) -> int:

    index = starting_pos
    curly_bracket_depth = 0

    while index >= 0:

        letter = input[index]
        
        if (letter == "{") and (curly_bracket_depth == 0):
            return index

        elif letter == "}":
            curly_bracket_depth += 1

        elif letter == "{":
            curly_bracket_depth -= 1

        index -= 1

    # If we're here without ever reaching return, there has been an error.
    # We didn't find the remaining closing bracket!!
    return -1


def clearRedProperty(text_input: str) -> str:
    """
    If we find a "red" in the STR, we start at its location.
    > Then, we look for the inner brackets surrounding it: { <<< red >>> }
    > We remove the whole area (from the two {-} found) from the input.
    """

    input = text_input[:]

    red_position = input.find(':"red"')

    while red_position != -1:

        is_red_in_array = is_pos_in_array(input, red_position-1)

        if is_red_in_array:
            # We just remove the 3 letters
            input = input[:red_position] + input[red_position+5+1:]

        # We can remove the whole {...} structure around it.
        else:
            cbracket_pos_1 = rfind_opening_cbracket(input, red_position-1)
            cbracket_pos_2 = find_closing_cbracket(input, red_position+5)

            # print(f"bracket_1 = {cbracket_pos_1}\nbracket_2 = {cbracket_pos_2}\n---")

            # --- We remove the section we just found: {...}
            # If we found the 2 {} around it:
            if (cbracket_pos_1 != -1) and (cbracket_pos_2 != -1):
                input = input[:cbracket_pos_1] + input[cbracket_pos_2+1:]

            # In case we don't find {}... we just remove "red" alone (should not happen anyway)
            # This allows us to keep going in the while.
            else:
                input = input[:red_position] + input[red_position+5+1:]


        # Let's try finding another "red" before the end of the loop
        red_position = input.find(':"red"')


    return input



# --- main()
def main() -> int:

    input = readFile()
    input_red_cleared = clearRedProperty(input)

    print(input_red_cleared)

    number_sum = sumAllNumberInString(input_red_cleared)

    print("\n")
    print(f"SUM of all number = {number_sum}")

    return 0



# --- Main launcher
if __name__ == "__main__":
    main()


