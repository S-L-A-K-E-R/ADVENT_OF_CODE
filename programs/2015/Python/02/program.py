# ----- File reading
data_directory = "2015/02-I_Was_Told_There_Would_Be_No_Math/data/input.txt"

data_file = open(data_directory, "r")
input_data = data_file.read()
data_file.close()

# Print the result:
#print( input_data )


# ----- Surface calculation for each gift!

# Dimension variables
l = int(0)
w = int(0)
h = int(0)

total_surface_all_gifts = 0
normal_ribbon_distance = 0
ribbon_distance_all_gifts = 0

for dimensions_raw in input_data.split( "\n" ):
    
    # 1 - Converting raw dimensions into specifics:
    dimensions = dimensions_raw.split( "x" )
    
    l = int( dimensions[0] )
    w = int( dimensions[1] )
    h = int( dimensions[2] )
    
    # 2 - Calculation of the surface area:
    geometry_surface_area = 2*l*w + 2*w*h + 2*h*l
    
    # 3 - Extra surface calculation
    extra_surface = min( l*w, w*h, h*l )
    
    # 4 - Total surface:
    total_surface_area_required = geometry_surface_area + extra_surface
    
    # 5 - Adding to the general value:
    total_surface_all_gifts += total_surface_area_required
    
    # ~~~ RIBBON EXTENSION:
    # Finding the 2 shortest elements, by substraction the highest one:
    all_dimensions_array = [h, w, l]

    dimension_toIgnoreForRibbon = max( l, w, h )
    
    ribbon_dimension_array = all_dimensions_array.copy()
    ribbon_dimension_array.remove( dimension_toIgnoreForRibbon )
    
    # Attribution of the elements:
    ribbon_dim1 = ribbon_dimension_array[0]
    ribbon_dim2 = ribbon_dimension_array[1]
    
    # 1. Normal ribbon distance calculation:
    normal_ribbon_distance = 2*(ribbon_dim1 + ribbon_dim2)
    
    # 2. Feet of the ribbon calculation:
    feet_ribbon_distance = h*w*l
    
    # 3. Ribbon total:
    ribbon_needed = normal_ribbon_distance + feet_ribbon_distance
    
    # 4. Adding to the general value for all gifts:
    ribbon_distance_all_gifts += ribbon_needed
    
    
print( "1. Total surface required for wrapping all the asked gifts:" )
print( "total_surface_all_gifts = ", total_surface_all_gifts )

print( "2. Total surface required for the ribbons:" )
print( "ribbon_distance_all_gifts = ", ribbon_distance_all_gifts )