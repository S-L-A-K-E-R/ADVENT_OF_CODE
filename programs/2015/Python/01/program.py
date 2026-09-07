
# Santa Claus starts at the ground floor:
global VAR_INIT_FLOOR
VAR_INIT_FLOOR = int(0)

# ----- File reading
data_directory = "2015/01-Not_Quite_Lisp/data/input.txt"

data_file = open(data_directory, "r")
input_data = data_file.read()
data_file.close()

# Print the result:
# print( input_data )

# ----- Floor analysis
floorCursor = VAR_INIT_FLOOR
index_firstTimeInBasement = 0
basementReached = False

for symbol in input_data:
    if symbol == "(":
        floorCursor += 1
    
    else:
        floorCursor -= 1
    
    if not(basementReached):
        index_firstTimeInBasement += 1
        
        # We stop incrementing the index if we reach the basement
        if floorCursor < 0:
            basementReached = True

print( "Step #1: floorCursor = ", floorCursor )
print( "Step #2: index_firstTimeInBasement = ", index_firstTimeInBasement )