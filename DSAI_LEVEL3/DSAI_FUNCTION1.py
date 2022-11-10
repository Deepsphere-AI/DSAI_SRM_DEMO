# ***********************************************************************************************

  # File Name 	:   DSAI_FUNCTION1
  # Purpose 	:   Create function and call function Program in Python
  # Author	:   Deepsphere.ai
  # Reviewer 	:   Jothi Periasamy
  # Date :   11/10/2022 
  # Version	:   1.0	

# ***********************************************************************************************

# # Program Description : Calling created function Program(without return) in Python

# # Python Development Environment & Runtime - Python

def Addition(vAR_num1,vAR_num2):
    print("Sum of {} & {} is {}".format(vAR_num1,vAR_num2,vAR_num1+vAR_num2))


def Subtraction(vAR_num1,vAR_num2):
    print("Subtraction of {} & {} is {}".format(vAR_num1,vAR_num2,vAR_num1-vAR_num2))

def Multiplication(vAR_num1,vAR_num2):
    print("Multiply of {} & {} is {}".format(vAR_num1,vAR_num2,vAR_num1*vAR_num2))

# Calling defined functions   

vAR_add = Addition(4,5)
vAR_sub = Subtraction(10,8)
vAR_mul = Multiplication(5,6)

print("Addition method return value - ",vAR_add)



# ***********************************************************************************************
# Disclaimer.

# We are providing this code block strictly for learning and researching, this is not a production ready code. We have no liability on this particular code under any circumstances; users should use this code on their own risk. 

# All software, hardware and other products that are referenced in these materials belong to the respective vendor who developed or who owns this product.

# ***********************************************************************************************
