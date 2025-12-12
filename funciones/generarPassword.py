import secrets
import string

def password_segura(longitud):
    # Grupos de caracteres
    numeros = string.digits
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    simbolos = string.punctuation

    # Unir todos los caracteres posibles
    todos = numeros + minusculas + mayusculas + simbolos

    # Asegurar que haya al menos un carácter de cada tipo
    contrasena = [
        secrets.choice(numeros),
        secrets.choice(minusculas),
        secrets.choice(mayusculas),
        secrets.choice(simbolos)
    ]

    # Completar el resto de la longitud
    for _ in range(int(longitud) - 4):
        contrasena.append(secrets.choice(todos))

    # Mezclar de forma segura
    secrets.SystemRandom().shuffle(contrasena)

    return "".join(contrasena)


# Ejemplo

