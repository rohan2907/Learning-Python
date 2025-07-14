# write function for minimum of variable numbers of arguments and it should have one of the 
# default arguments as 0 and if there is no default argument then it should return minimum of all the arguments.

# minimum function to find the minimum of variable numbers of arguments
def minimum(*args, low_limit=None):
    if not args:
        return None  # Return None if no arguments are provided

    if low_limit is not None:
        args = [arg for arg in args if arg >= low_limit]

    return min(args)

# Example usage:
result = minimum(5, 3, 8, 1, low_limit=3)
print(f"The minimum value is: {result}.")
# Example usage:
# The minimum value is: 3.
# Example usage without low_limit:
result_no_limit = minimum(5, 3, 8, 1)       
print(f"The minimum value is: {result_no_limit}.")
# Example usage without low_limit:
# The minimum value is: 1. 
# Example usage with no arguments:
result_empty = minimum()
print(f"The minimum value with no arguments is: {result_empty}.")   
# Example usage with no arguments:
# The minimum value with no arguments is: None.
#
 
