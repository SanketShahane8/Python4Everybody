fname = input("Enter the File Name: ")
fh = open(fname,"r")
file_content = fh.read()
striped_file_content = file_content.rstrip()
print(file_content.upper())
print(striped_file_content.upper())