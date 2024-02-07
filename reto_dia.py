nroUsuarios = int(input('Digite el número de usuarios que desea registrar: '))
usuarios_registrados = []

for registro in range(0, nroUsuarios):
    print('--------------------------------------')
    print('Hola, digite sus datos para registrarse en el sistema')

    name = input('Digite su(s) nombre(s): ')
    if len(name) < 5 or len(name) > 50:
        print('El nombre debe tener entre 5 y 50 caracteres')
        name = input('Digite su(s) nombre(s) correctamente: ')
        
    lastname = input('Digite su(s) apellido(s): ')
    if len(lastname) < 5 or len(lastname) > 50:
        print('El apellido debe tener entre 5 y 50 caracteres')
        lastname = input('Digite su(s) apellido(s) correctamente: ')
        
    email = input('Digite su correo electrónico: ')
    if len(email) < 5 or len(email) > 50:
        print('El correo debe tener entre 5 y 50 caracteres')
        email = input('Digite su correo electrónico correctamente: ')
    
    phone = input('Digite su nro de telef: ')
    if len(phone) != 10:
        print('El nro de telefono debe tener 10 digitos')
        phone = int(input('Digite su nro de telef correctamente: '))
    
    usuarios_registrados.append({
        'name': name,
        'lastname': lastname,
        'email': email,
        'phone': phone
    })
        
print('--------------------------------------')
print('Usuarios registrados correctamente')
print(usuarios_registrados)
    

