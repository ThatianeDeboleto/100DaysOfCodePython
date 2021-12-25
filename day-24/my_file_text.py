with open("my_file.txt") as file:
contents = file.read()
print(contents)
file.close()

#parametro
with open("my_file_txt", mode="w") as file:
    file.write("New text.")