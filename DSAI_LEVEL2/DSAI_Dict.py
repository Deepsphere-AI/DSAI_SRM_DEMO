# ***********************************************************************************************

  # File Name 	:   DSAI_Dict
  # Purpose 	:   Access attributes/objects with dictionary Program in Python
  # Author	:   Deepsphere.ai
  # Reviewer 	:   Jothi Periasamy
  # Date :   11/10/2022 
  # Version	:   1.0	

# ***********************************************************************************************

# # Program Description : Accessing Dictionary attributes Program in Python

# # Python Development Environment & Runtime - Python

# Declaring car object with some attributes in dictionary
vAR_car_dict1 = {"Name":"Fiat","Model":2018,"Weight":"850 Kg","Color":"White","Capacity":4}

print("*"*100)
print("\033[1m"+"\t\t\t\t\t Car Details"+"\033[0m")
print("-"*100)

print("\t\t\t\t\t Car Name : ",vAR_car_dict1["Name"])
print("\t\t\t\t\t Car Model : ",vAR_car_dict1["Model"])
print("\t\t\t\t\t Car Color : ",vAR_car_dict1["Color"])

print("*"*100)


# Declaring company object with some attributes in dictionary
vAR_company_dict2 = {"Name":"Deepsphere.ai",
            "Sector":"EdTech",
            "Employees":[{"EmployeeId":1,"EmployeeName":"Sathish"},{"EmployeeId":2,"EmployeeName":"Ramesh"}],
            "EmployeeCount":50,
            "Address":{"Landmark":"Near MMM Hospital","Pincode":600037}}

print("*"*100)
print("\033[1m"+"\t\t\t\t\t Company Details"+"\033[0m")
print("-"*100)

print("\t\t\t\t\t Company Name : ",vAR_company_dict2["Name"])
print("\t\t\t\t\t Company Sector : ",vAR_company_dict2["Sector"])
print("\t\t\t\t\t Company Employees : ",vAR_company_dict2["Employees"])
print("\t\t\t\t\t Company Employee1 : ",vAR_company_dict2["Employees"][0])
print("\t\t\t\t\t Company Employee2 : ",vAR_company_dict2["Employees"][1])

print("*"*100)

# ***********************************************************************************************
# Disclaimer.

# We are providing this code block strictly for learning and researching, this is not a production ready code. We have no liability on this particular code under any circumstances; users should use this code on their own risk. 

# All software, hardware and other products that are referenced in these materials belong to the respective vendor who developed or who owns this product.

# ***********************************************************************************************
