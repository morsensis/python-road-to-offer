
def get_name():
    name = input('Input your name:')
    return name

def get_age():
    while True:
        try:
            return int(input('How old are u?'))
            
        except ValueError:
            print("Invalid input")

def check_access(age, name): 
    if age >= 18:
        print("Access granted. Welcome to the project, ", name)
    else:
        print("Access denied")           
    
def main():
    #print('Hello, username. Please, verify your age and name')
    #name = get_name()
    #age = get_age()
    #check_access(age, name)
    list = []
    print(list)
    list.append("h1st")
    #list = ["h1st", "nissaba", "mor1"]
    print(list)
    list.append("mor1")
    #list = ["h1st", "nissaba", "mor1"]
    print(list)
main() 
