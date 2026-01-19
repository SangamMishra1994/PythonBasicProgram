# file = open("text.py", "w")

# try:
#     file.write("Hello Sangam Mishra")
# finally:
#     file.close()


# Approach Second to open and write the file

with open("test.py", "w") as file:
    file.write("# This is the new file for python.")
