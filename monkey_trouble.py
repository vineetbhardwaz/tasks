##########################################################################################################
#ID       : Task 2                                                                                       #
#Author   : Vineet Bhardwaz 05/12/2016                                                                   #
##########################################################################################################

#function Definition.
def monkey_trouble(a_smile, b_smile):
    if a_smile ^ b_smile:     #used the XOR operator and inverted the 1s to zeroes and zeroes to 1s to get the desired result.
        return False
    else:
        return True
        
#Function Call with all possible argument values. 
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
