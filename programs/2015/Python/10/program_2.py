# --- ADVENT OF CODE ---
#  
# 2025-10
# "Elves Look, Elves Say"
# 
# Date: 2026/08/27 
# ----------------------


# --- Libraries and dependencies



# --- Global variables
INPUT = "1113122113"
SAMPLE = "1"

PROCESS_REPETITION = 50



# --- Functions
def look_number(number:str) -> str:

    newString:str = ""
    digitRepetition:int = 1

    for index, digit in enumerate(number):

        if index < len(number)-1:

            if number[index+1] == digit:
                digitRepetition +=1 
                continue

            else:
                newString += f"{digitRepetition}{digit}"
                digitRepetition = 1

        # It's the last character
        else:
            newString += f"{digitRepetition}{digit}"

        #print(newString)

    return newString





# --- main()
def main() -> int:

    looked_string:str = INPUT

    for _ in range(0, PROCESS_REPETITION):

        looked_string = look_number(looked_string)
        #print(looked_string)

    print(f"LENGTH OF {PROCESS_REPETITION} look&say process on {INPUT}:\n")
    print(f"{len(looked_string)}")

    return 0



# --- main() launcher
if __name__ == "__main__":
    main()



