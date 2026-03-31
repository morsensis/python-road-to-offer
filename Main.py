print('Hello, username. Please, verify your age and name')
name = input('Input your name:')
while True:
    try:
        age = int(input('How old are u?'))
        if(age>=18):
            print("Access granted. Welcome to the project, ", name)
        else:
            print("Access denied")
        break
    except ValueError:
        print("Verify not clear")

