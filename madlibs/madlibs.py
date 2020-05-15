with open('assets/template.txt', 'r') as file:
    contents = file.read()

print(contents)

for i in contents:
    if i == '{':
        print('found the bracket')

with open('assets/filled.txt', 'w') as file2:
    file2.write(contents)