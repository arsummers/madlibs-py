def greeting():
    print("""
    *********
    Hello! Are you ready to play a game of madlibs?
    *********
    """)

def get_keys(path):
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

        return keys



def handle_keys(keys):
    libs = [] #you know, like madlibs...
    
    for i in keys:
        prompt = input(f"""****** enter a {i} ******""") 
        libs.append(prompt)

    return libs

def fill_template(libs):
    with open(path, 'r') as file:
        contents = file.read()

    bracket_count = contents.count('{')
    for i in range(bracket_count):
        start = contents.find('{', 0)
        end = contents.find('}', 0) + 1
        contents = contents[:start] + libs[i] + contents[end:]

    return contents

def print_output(stuff):

    with open('assets/filled.txt', 'w') as file2:
        file2.write(stuff)



if __name__ == "__main__":
    path = 'assets/template.txt'
    greeting()
    get_keys(path)
    keys = get_keys(path)
    handle_keys(keys)
    libs = handle_keys(keys)
    fill_template(libs)
    filled_in = fill_template(libs)
    print_output(filled_in)