Correo_Electronico = False

for i in "correodeejemplo@hotmail.com":
    if(i == "@"):
        Correo_Electronico = True

if Correo_Electronico: #if Correo_Electronico
    print("El Correo Electronico es valido")
else:
    print("El Correo Electronico no es valido")