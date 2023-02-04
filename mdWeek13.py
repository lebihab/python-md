#  Here's an example of a Python script that allows the user to input the number of EC2 
#instances they want names for and the name of their department and generates unique 
#names using the department name and random characters and numbers:

import random
import string

def generate_ec2_name(department, instances_count):
    ec2_names = []
    for i in range(instances_count):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        ec2_name = f"{department}-EC2-{random_string}"
        ec2_names.append(ec2_name)
    return ec2_names

# User input
instances_count = int(input("Enter the number of EC2 instances: "))
department = input("Enter the name of your department: ")

# Generate unique EC2 names
ec2_names = generate_ec2_name(department, instances_count)

# Output the EC2 names
for i, ec2_name in enumerate(ec2_names):
    print(f"EC2 instance {i+1}: {ec2_name}")