def greeting():
    print("""
    *********
    Hello! Are you ready to play a game of madlibs?
    *********
    """)

def read_template(path):
    with open(path, 'r') as file:
        contents = file.read()
        keys = []
        end = None #exists here to be reassigned below
        bracket_count = contents.count('{')

        for i in range(bracket_count):
            start = contents.find('{', end) + 1
            end = contents.find('}', start)
            key = contents[start:end]
            keys.append(key)

        print(keys)
        return keys



def handle_keys(keys):
    libs = []
    
    for i in keys:
        prompt = input(f'****** enter a {i} ******') 
        libs.append(prompt)

    print(libs)
    return libs

def fill_template():
    pass




# with open('assets/filled.txt', 'w') as file2:
#     file2.write(contents)



if __name__ == "__main__":
    path = 'assets/template.txt'
    greeting()
    read_template(path)
    keys = read_template(path)
    handle_keys(keys)