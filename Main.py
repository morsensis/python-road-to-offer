print('Hello, username. Please, verify your age and name')
def get_name():
    name = input('Input your name:')
    return name

def get_age():
    while True:
        try:
            age = int(input('How old are u?'))
            break
        except ValueError:
            print("Invalid input")
        
    return age

def check_access(age, name): 
    if(age>=18):
        print("Access granted. Welcome to the project, ", name)
    else:
        print("Access denied")           
    

name = get_name()
age = get_age()
check_access(age, name)
