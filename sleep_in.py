########################################################################################################
#ID     : Task 1                                                                                       #
#Author : Vineet Bhardwaz 05/12/2016                                                                   #
########################################################################################################

# Function Definition
def sleep_In(weekDay, vacation):
    if not weekDay and not vacation:
        return True
    elif not vacation:
        return False
    else:
        return True
        
# Function Calls with all possible arguments of week_day and vacation.
print(sleep_In(False, False))
print(sleep_In(True, False))
print(sleep_In(False, True))
print(sleep_In(True, True))

