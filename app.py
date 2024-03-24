
# create the file
handling_file_assignment = open("my_file.txt", "x+")
handling_file_assignment = open("my_file.txt", "w")
handling_file_assignment.writelines(["Hello! My Name is Gilbert", "\nI am 35 years old", "\ncurrently enjoying learning python at plp"])
handling_file_assignment.close()
print(handling_file_assignment)

# read the file
handling_file_assignment = open("my_file.txt", "r")
file_content = handling_file_assignment.read()
handling_file_assignment.close()
print(file_content)


# append
handling_file_assignment = open("my_file.txt", "a+")
file_content = handling_file_assignment.writelines(["\nApart from coding i also love nature walks,", "\nMoney matters more in the insurance industry", "\nLastly I love cool gospel music, i am a true beliver or Jesus "])
handling_file_assignment.close()

print(file_content)