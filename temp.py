class Person:
    def __init__(self,username,password):
        self.username = username
        self.password = password

def criarUsuario(usuarios):
        print("Create an username and password please")
        username = input("Username:\n")
        password = input("Password:\n")
        usuarios.append(Person(username, password))
        
def print_Usuarios(usuarios):
    for i in range (0, len(usuarios)):
        print(i, usuarios[i].__dict__)

while (True):
    x = input("want to make a username?")
    if (x == "yes"):
        criarUsuario(usuarios)
    else:
        print_Usuarios(usuarios)
        break
while (True):
    user_var=input("username:\n")
    pass_var=input("password:\n")
    for i in range (0, len(usuarios)):
        if usuarios[i].username == user_var and usuarios[i].password == pass_var:
            isValidUser = True
        else: 
            isValidUser = False 
    if isValidUser:
        print("ok")
    else: 
        print("not ok")
    ##break
                    
    