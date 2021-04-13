"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""
#Declaring global variables to be used in fall functions
plus = '+'
dash = '-'
space = ' '
line = '|'
# PART 1
def print_grid1():
    n = 4 # just used to scale the size of the grid to be printed
    print(plus + n*(space + dash) + space + plus + n*(space + dash) + space + plus)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(plus + n * (space + dash) + space + plus + n * (space + dash) + space + plus)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(line + n * (2*space) + space + line + n * (2*space) + space + line)
    print(plus + n * (space + dash) + space + plus + n * (space + dash) + space + plus)
    pass
#end of part 1 function block

# PART 2
def print_grid2(size):
    if size <= 0: #added this condition because a size < 0 doesn't make sense
        print("Invalid input for size, please enter a value greater than zero")
        exit()
    print(plus + size*(space + dash) + space + plus + size*(space + dash) + space + plus)
    for i in range(0,size):
        print(line + size * (2*space) + space + line + size * (2*space) + space + line)
    print(plus + size * (space + dash) + space + plus + size * (space + dash) + space + plus)
    for i in range(0,size):
        print(line + size * (2*space) + space + line + size * (2*space) + space + line)
    print(plus + size * (space + dash) + space + plus + size * (space + dash) + space + plus)
    pass
#end of part 2 function block

# PART 3
def print_grid3(box_size, cell_size):
    for i in range (0,box_size):
        for i in range(0, box_size):
            print(plus + cell_size * (space + dash), end = '')
            print(space,end='')
        print(plus)
        for i in range(0,cell_size):
            for i in range(0, box_size+1):
                print(line + cell_size * (2*space), end='')
                print(space, end='')
            print()
    for i in range(0, box_size):
        print(plus + cell_size * (space + dash), end='')
        print(space, end='')
    print(plus)
    pass

#no input variable for print_grid1() function. Will just print a 2x2 grid.
print_grid1()
#input a variable that will scale a 2x2 grid
print_grid2(4)
#input a box_size to dictate how many boxes, and input a cell_size to dictate the size of the boxes
print_grid3(2,4)

#the current values in the functions above will loaded will all print the same size grid