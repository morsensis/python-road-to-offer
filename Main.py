print('Hello, username. Please, verify your age and name')
name = input('Input your name:')
try:
    age = int(input('How old are u?'))
    if(age>=18):
        print("Access granted. Welcome to the project, " + name)
    elif(age<18):
        print("Access denied")
except:
    print("Verify not clear")
