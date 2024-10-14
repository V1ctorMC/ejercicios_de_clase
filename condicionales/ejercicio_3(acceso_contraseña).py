#Este programa te pregunta tu usuario y contraseña para entrar
usuarioV = "admin"
contraseñaV = 1234
print("Nombre de usuario:")
usuario = input()
print("contraseña:")
contraseña = int(input())
if(contraseña == contraseñaV and usuario == usuarioV):
    print("Acceso concedido")
else:
    print("Acceso denegado")