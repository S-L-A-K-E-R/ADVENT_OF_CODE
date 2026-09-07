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

def read_file() -> str:

    data = INPUT_PATH.read_text(encoding="utf-8").strip()
    return data


def sum_all_numbers_in_str(text: str) -> int:

    index = 0
    sum_buffer = 0

    while index < len(text):

        if (text[index].isdigit()) or (text[index] == "-" and index + 1 < len(text) and text[index+1].isdigit()):

            found_number_text = ""

            # Only for the first "- ...", we add it specially to the string.
            # This avoids the problem like: "-458-"... wrongly taking the latest "-".
            if text[index] == "-":
                found_number_text += "-"
                index += 1

            # Now let's unravel the string until we find the full number
            while index < len(text) and text[index].isdigit() :
                found_number_text += text[index]
                index += 1

            # print(f"FINAL: {found_number_text}")

            sum_buffer += int(found_number_text)

        else:
            index += 1


    return sum_buffer


def find_closing_cbracket(text: str, starting_pos: int) -> int:

    index = starting_pos
    curly_bracket_depth = 0
    while index < len(text):

        letter = text[index]
        
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


def rfind_opening_cbracket(text: str, starting_pos: int) -> int:

    index = starting_pos
    curly_bracket_depth = 0

    while index >= 0:

        letter = text[index]
        
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


def clear_red_property(text: str) -> str:
    """
    If we find a "red" in the STR, we start at its location.
    > Then, we look for the inner brackets surrounding it: { <<< red >>> }
    > We remove the whole area (from the two {-} found) from the input.
    """

    red_position = text.find(':"red"')

    while red_position != -1:

        # We can remove the whole {...} structure around it.
        cbracket_pos_1 = rfind_opening_cbracket(text, red_position-1)
        cbracket_pos_2 = find_closing_cbracket(text, red_position+5)

        # print(f"bracket_1 = {cbracket_pos_1}\nbracket_2 = {cbracket_pos_2}\n---")

        # --- We remove the section we just found: {...}
        # If we found the 2 {} around it:
        if (cbracket_pos_1 != -1) and (cbracket_pos_2 != -1):
            text = text[:cbracket_pos_1] + text[cbracket_pos_2+1:]

        # In case we don't find {}... we just remove "red" alone (should not happen anyway)
        # This allows us to keep going in the while.
        else:
            raise ValueError("Unable to find the object surrounding 'red'")


        # Let's try finding another "red" before the end of the loop
        red_position = text.find(':"red"')


    return text



# --- main()
def main() -> int:

    data_input = read_file()
    data_input = clear_red_property(data_input)

    print(data_input)

    number_sum = sum_all_numbers_in_str(data_input)

    print("\n")
    print(f"SUM of all number = {number_sum}")

    return 0



# --- Main launcher
if __name__ == "__main__":
    main()


