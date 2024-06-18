import secrets
import string

def genera_password(complicata=False):

    if complicata:
        caratteri = string.ascii_letters + string.digits + string.punctuation
        lunghezza = 20
    else:
        caratteri = string.ascii_letters + string.digits
        lunghezza = 8
    
    # Genera la password
    password = ''.join(secrets.choice(caratteri) for _ in range(lunghezza))
    return password

def main():
    print("Generatore di Password")
    print("1. Password Semplice (8 caratteri alfanumerici)")
    print("2. Password Complicata (20 caratteri ASCII)")
    
    scelta = input("Scegli il tipo di password (1 per semplice, 2 per complicata): ")
    
    if scelta == '1':
        print("Password Semplice:", genera_password())
    elif scelta == '2':
        print("Password Complicata:", genera_password(complicata=True))
    else:
        print("Scelta non valida! Inserisci 1 o 2.")

if __name__ == "__main__":
    main()
