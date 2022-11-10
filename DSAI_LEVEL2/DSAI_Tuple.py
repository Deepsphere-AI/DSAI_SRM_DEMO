# ***********************************************************************************************

  # File Name 	:   DSAI_Tuple
  # Purpose 	:   Access Elements with Tuple Program in Python
  # Author	:   Deepsphere.ai
  # Reviewer 	:   Jothi Periasamy
  # Date :   11/10/2022 
  # Version	:   1.0	

# ***********************************************************************************************

# # Program Description : Accessing Tuple Elements Program in Python

# # Python Development Environment & Runtime - Python

vAR_list = [1,2,3,3,4]
print("List Elements Before modification: ",vAR_list)

vAR_list[3] = 4
print("List Elements After modification: ",vAR_list)

print("\033[1m"+"Note :List elements are mutable and tuple elements are immutable"+"\033[0m")
# Tuple Declaration with elements

vAR_tuple = (1,2,3,3,4)
print("Tuple Elements Before modification: ",vAR_tuple)

# Below code will throw an error
vAR_tuple[3] = 4
print("Tuple Elements After modification: ",vAR_tuple)



# print("1st Element in Tuple - ",vAR_tuple[0])
# print("2nd Element in Tuple - ",vAR_tuple[1])
# print("3rd Element in Tuple - ",vAR_tuple[2])
# print("4th Element in Tuple - ",vAR_tuple[3])
# print("5th Element in Tuple - ",vAR_tuple[4])


# ***********************************************************************************************
# Disclaimer.

# We are providing this code block strictly for learning and researching, this is not a production ready code. We have no liability on this particular code under any circumstances; users should use this code on their own risk. 

# All software, hardware and other products that are referenced in these materials belong to the respective vendor who developed or who owns this product.

# ***********************************************************************************************
