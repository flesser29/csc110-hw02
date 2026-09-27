# ------------------------------------------------------
#        Name: Frances Lesser
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# -----------------------------------------------------
# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    """Read two integers from user imput."""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    a = int(input("give me x: "))
    b = int(input("give me y: "))
    return a,b
    
# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    """Compute (a+b)/(a-b) using the inputs."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult_result = a * b
    print (f"mult result: {mult_result}")
    add_result = a+b
    print (f"add result: {add_result}")
    return mult_result/add_result

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    """Print results in a fancy block."""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    print ("****************")
    print ("RESULTS:")
    print (f"first number: {a}")
    print (f"second number: {b}")
    print (f"multadd result: {ab_multadd}")
    print ("================")

def main ():
    # ADD a Docstring for this function
    """Main execution function."""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
x,y =read_two_ints()
    
       # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

xy_multadd =compute_multadd(x, y)

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

print_fancy(x,y, xy_multadd)

    # Do not modify this final print statement
print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()

# - [x] you added your name to the top comments of the python file
# - [x] runs without syntax errors (or -50%)
# - [ ] adds a few small but informative comments (or -5%)
# - [x] adds docstrings to each function (or -5%)
# - [x] Passes all tests (or lose 15% per missed test). If you do not pass all tests, do not check this box
# - [ ] You checked the correct boxes