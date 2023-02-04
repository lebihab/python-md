# Initialize an empty list of AWS services
aws_services = []

# Add items to the list
aws_services.append("EC2")
aws_services.append("S3")
aws_services.append("Lambda")
aws_services.append("RDS")
aws_services.append("SQS")

# Print the list and its length
print("AWS services:", aws_services)
print("Length of the list:", len(aws_services))

# Remove two services from the list
aws_services.remove("RDS")
aws_services.remove("SQS")

# Print the updated list and its length
print("Updated AWS services:", aws_services)
print("New length of the list:", len(aws_services))