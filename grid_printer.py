"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""

plus = '+'
dash = '-'
space = ' '
line = '|'
# PART 1
def print_grid1():
    n = 4
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
#end of function block

# PART 2
def print_grid2(size):
    print(plus + size*(space + dash) + space + plus + size*(space + dash) + space + plus)
    for i in range(0,size):
        print(line + size * (2*space) + space + line + size * (2*space) + space + line)
    print(plus + size * (space + dash) + space + plus + size * (space + dash) + space + plus)
    for i in range(0,size):
        print(line + size * (2*space) + space + line + size * (2*space) + space + line)
    print(plus + size * (space + dash) + space + plus + size * (space + dash) + space + plus)
    pass


# PART 3
def print_grid3(box_size, cell_size):
    pass

print_grid2(10)