# ----- File reading
data_directory = "2015/03-Perfectly_Spherical_Houses_in_a_Vacuum/data/input.txt"

data_file = open(data_directory, "r")
input_data = data_file.read()
data_file.close()

# Print the result:
# print( input_data )

# ----- Santa movements

# We will set an imaginary grid where Santa is going to move on.
# On every move, we are going to check his positionning on a (x,y) position-based grid.
# We will also store the number of time he went on the grid.

# Then, we will only have to sort all the location where he delivered > 1 gift.

# To select the #2 variation of this exercise,
# set this boolean to "True". Otherwise let it to "False".
is_RoboSanta_deployed = True

grid_board = [
    {"position": [0,0], "delivering(s)": 1} 
    ]

if is_RoboSanta_deployed:
    y = grid_board[0]["delivering(s)"] = 2

# Coordinates
x = grid_board[0]["position"][0]
y = grid_board[0]["position"][1]

x_robo = grid_board[0]["position"][0]
y_robo = grid_board[0]["position"][1]

# Turn index, for Robo/Santa:
loop_index = 0

for move in input_data:
    
    if is_RoboSanta_deployed:
        # --- EVEN LOOP = SANTA
        if loop_index % 2 == 0:
            
            if move == "^":
                y -= 1
        
            elif move == ">":
                x += 1
            
            elif move == "v":
                y += 1
                
            elif move == "<":
                x -= 1
            
            newGridLocation = [x,y]
            
            # 2. Checking if the location already exists in the grid_board:
            gridPosition_alreadyExisting = False
            
            for i in range( len(grid_board) ): 
                if newGridLocation == grid_board[i]["position"]:
                    grid_board[i]["delivering(s)"] += 1
                    
                    gridPosition_alreadyExisting = True
                    break
            
            if not(gridPosition_alreadyExisting):
                grid_board.append(
                    {"position": newGridLocation, "delivering(s)": 1} 
                    )
        
        # --- ODD LOOP = ROBO
        else:
            if move == "^":
                y_robo -= 1
        
            elif move == ">":
                x_robo += 1
            
            elif move == "v":
                y_robo += 1
                
            elif move == "<":
                x_robo -= 1
            
            newGridLocation_robo = [x_robo,y_robo]
            
            # 2. Checking if the location already exists in the grid_board:
            gridPosition_alreadyExisting = False
            
            for i in range( len(grid_board) ): 
                if newGridLocation_robo == grid_board[i]["position"]:
                    grid_board[i]["delivering(s)"] += 1
                    
                    gridPosition_alreadyExisting = True
                    break
            
            if not(gridPosition_alreadyExisting):
                grid_board.append(
                    {"position": newGridLocation_robo, "delivering(s)": 1} 
                    )
        
        # When we've finally finished the turn of action, we add one to the counter:
        loop_index += 1
        
    else:
        # 1. Moving coordinates on input reading:
        if move == "^":
            y -= 1
        
        elif move == ">":
            x += 1
        
        elif move == "v":
            y += 1
            
        elif move == "<":
            x -= 1
        
        newGridLocation = [x,y]
    
    
        # 2. Checking if the location already exists in the grid_board:
        gridPosition_alreadyExisting = False
        
        for i in range( len(grid_board) ): 
            if newGridLocation == grid_board[i]["position"]:
                grid_board[i]["delivering(s)"] += 1
                
                gridPosition_alreadyExisting = True
                break
        
        if not(gridPosition_alreadyExisting):
            grid_board.append(
                {"position": newGridLocation, "delivering(s)": 1} 
                )

# Solution to riddle #1
houseNumber_delivered = len(grid_board)

print( "1# Number of house with at least 1 gift delivered:")
print( "houseNumber_delivered = ", houseNumber_delivered)
    
    