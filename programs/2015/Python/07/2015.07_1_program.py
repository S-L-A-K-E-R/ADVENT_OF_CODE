
# [>>>] Global variables
# ---------------------
data_directory = "programs/2015/Python/07/input.txt"
variable_searched = "a"

linkage_cache: dict[str, int] = {}

variable_list = ["a"] # True input
# variable_list = ["d", "e", "f", "g", "h", "i", "x", "y"] # Sample testing



# [>>>] Functions
# ---------------------
def main():
    
    data = file_reading()
    # data_display( data )


    # Multi-variables finder:
    for variable in variable_list:

        signal_value = logic_solver_recursive(variable, data)

        print(f"[>] Signal value for {variable} = {signal_value}" )

# - File reading
# ---------------------
def file_reading():

    with open(data_directory, "r") as file_data:
        data = [line.strip().split(" -> ") for line in file_data]

    return data


def data_display( data:list[list[str]] ):

    print( " /// TYPE OF 'DATA':", type(data) )
    print( " > Value in code: list[list[str]]\n" )
    
    for i, line in enumerate(data):
        print( f"{i}.\t{line}" )


# - Recursive value finder
# ---------------------
# The goal here:
# 1. Set a variable you want to scan: let's say x
# 2. The program will scan through the data line after line for: "(...) -> x\n"
# 3. On this line, it's going to take the (...) part, and run through it again until it gets into a readable value.
#
# 3+. There are some considerations to take, as we have to take into account AND, OR, NOT operators...
# 
# As you've certainly guessed it, it's going to be recursive time (yay).
# /!/ Warning: this definitely won't be optimized, I'm planning on scanning the whole data over and over for each iteration of the recursive process.
# Sorry if it hurts your programmer heart in advance.
# ---------------------
def logic_solver_recursive( variable_searched:str, data:list[list[str]] ) -> int:

    # Let's check if the link of a specific value is already done in previous iterations.
    # -------------
    if variable_searched in linkage_cache:

        logic_value = linkage_cache[variable_searched]
        return logic_value

    
    # --- OTHERWISE: we need to calculate the link, it's a new one
    # -------------

    # In case we give only a line of "123" to the recursive algorithm...
    # ... Honestly, I don't ever think this happens, but it's just a fallback emergency management, instead of potential crashes.
    elif variable_searched.isdigit():

        #print(f"[Single word line?] Instruction: {line} (transformed into (int) automatically)")

        logic_value = int( variable_searched )
        return logic_value


    else:
        for line in data:

            if line[-1] == variable_searched :

                # Here we have many situations to check.
                # Hopefully: each line contains only 1 "OR", "AND", so we start with this.

                instruction = line[0].split()

                if "AND" in instruction:
                    instruction_left = instruction[0]
                    instruction_right = instruction[2]

                    #print(f"[AND] Instruction: {instruction} -> {line[1]} /// Left: {instruction_left} / Right: {instruction_right}")
                    #print(f"EXTRA: value1 = {logic_solver_recursive(instruction_left, data)} // value2 = {logic_solver_recursive(instruction_right, data)}")

                    logic_value = (logic_solver_recursive(instruction_left, data) & logic_solver_recursive(instruction_right, data)) & 0xFFFF
                    linkage_cache[variable_searched] = logic_value
                    
                    return logic_value

                elif "OR" in instruction:
                    instruction_left = instruction[0]
                    instruction_right = instruction[2]

                    #print(f"[OR] Instruction: {instruction} -> {line[1]} /// Left: {instruction_left} / Right: {instruction_right}")

                    logic_value = (logic_solver_recursive(instruction_left, data) | logic_solver_recursive(instruction_right, data)) & 0xFFFF
                    linkage_cache[variable_searched] = logic_value

                    return logic_value

                elif "NOT" in instruction:
                    instruction_right = instruction[1]

                    #print(f"[NOT] Instruction: {instruction} -> {line[1]} /// Right: {instruction_right}")

                    logic_value = ~ (logic_solver_recursive(instruction_right, data)) & 0xFFFF
                    linkage_cache[variable_searched] = logic_value

                    return logic_value

                elif "LSHIFT" in instruction:
                    instruction_left = instruction[0]
                    instruction_offset = int(instruction[2])

                    #print(f"[L-SHIFT] Instruction: {instruction} -> {line[1]} /// Left: {instruction_left} / Offset: {instruction_offset}")

                    logic_value = (logic_solver_recursive(instruction_left, data) << instruction_offset) & 0xFFFF
                    linkage_cache[variable_searched] = logic_value

                    return logic_value

                
                elif "RSHIFT" in instruction:
                    instruction_left = instruction[0]
                    instruction_offset = int(instruction[2])

                    #print(f"[R-SHIFT] Instruction: {instruction} -> {line[1]} /// Left: {instruction_left} / Offset: {instruction_offset}")

                    logic_value = (logic_solver_recursive(instruction_left, data) >> instruction_offset) & 0xFFFF
                    linkage_cache[variable_searched] = logic_value

                    return logic_value

                elif instruction[0].isdigit():
                    instruction_left = int(instruction[0])

                    #print(f"[VALUE ATTRIBUTION] Instruction: {instruction} -> {line[1]} /// Left value: {instruction_left} to {variable_searched}")

                    return instruction_left

                
                else: # It's a direct link: (type: "lx -> a")
                    instruction_left = instruction[0]
                    
                    #print(f"[DIRECT LINK] Instruction: {instruction} -> {line[1]} /// Left value: {instruction_left} to {variable_searched}")

                    logic_value = logic_solver_recursive(instruction_left, data)
                    linkage_cache[variable_searched] = logic_value

                    return logic_value


        else:

            raise ValueError(f"The looked-up variable {variable_searched} couldn't be found in the data... :(")



# [>>>] main() launcher
# ---------------------
if __name__=="__main__":
    main()