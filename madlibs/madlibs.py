def greeting():
    print("""
    *********
    Hello! Are you ready to play a game of madlibs?
    *********
    """)

def read_template(path):
    with open(path, 'r') as file:
        contents = file.read()
    print(contents)



    for i in contents:
        begin = '{'
        end = '}'
        if i == begin:
            print(contents[])


# with open('assets/filled.txt', 'w') as file2:
#     file2.write(contents)




if __name__ == "__main__":
    path = 'assets/template.txt'
    greeting()
    read_template(path)