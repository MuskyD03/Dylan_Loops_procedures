def main():
    """ 
    Quick refresher of prior weeks exercise.

    Variables are:
      - Declared
      - Have an Identifier (aka name)
      - Have a Value
      - Have an Assignment Operator

    Conditional Statements:
      - Evaluate some condition to be True or False
      - If True the logic inside the block is executed
      - If False the logic inside the block is ignored
      - Statements are read from top to bottom and the first
        True statement found is executed
      - if..then

    """
     
    #variables
    user_name = "Bob" 
    user_points = 10 
    has_enough_points = False
 
    # conditional statement
    if user_points == 50:
        print("You have 50 points!")
        has_enough_points = True
    else:
        print("You don't have enough points yet, increasing points by 10")
        user_points += 10
    
    # call print()
    print("Hi", user_name)
    print("Current points:", user_points)
    print("Has enough points:", has_enough_points) 


if __name__ == "__main__":
    main()
