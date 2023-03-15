# a. name for section
alpha = 1
beta = 2
x = [-3, -2, -1, 1, 2, 3]

# b. name for section
def function(x,alpha,beta):
    """ explain what the function does i.e. This function will do ...
    
    Args:
    
        x (float): explanation
        alpha (float): explanation
        beta (float): explanation
        
    Returns:
    
        y (float): explanation
    
    """
    
    y = x**2 
    return y

# c. name for section
for i in range(len(x)):
    
    # i. name for sub-section
    y = function(x[i],alpha,alpha)
    
    # ii. name for sub-section
    cond = alpha > 0 # non-positive not allowed due to log (line comment)
    
    # iii. name for sub-section
    if cond:
        print(math.log(y))