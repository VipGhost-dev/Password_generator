import random
import string

password = ""
passwords_list = []
length_password = 8
use_ABC = True #Добавление в генерацию строчных букв | Adding lowercase letters to generation
use_123 = True #Добавление в генерацию чисел | Adding digits to generation
use_specsymbols = True #Добавление в генерацию спец символов | Adding special characters to generation
code = "start"


def generator(length_password, use_ABC, use_123, use_specsymbols): #Логика генерации пароля | Password generation logic
    chars = string.ascii_lowercase
    if use_ABC:
        chars += string.ascii_uppercase
    if use_123:
        chars += string.digits
    if use_specsymbols:
        chars += "!@#$%^&*"
    for i in range(10):
        password_generate = "".join(random.choice(chars) for _ in range(length_password))
        password_generate = checker(password_generate, use_ABC, use_123, use_specsymbols, chars)
        passwords_list.append(password_generate)
        print(f"{i+1}. {password_generate}")
    
def checker(password_generate, use_ABC, use_123, use_specsymbols, chars):
    if use_ABC:
        if not any(c.isupper() for c in password_generate):
            password_generate = "".join(random.choice(chars) for _ in range(length_password))
            password_generate = checker(password_generate, use_ABC, use_123, use_specsymbols, chars)
    if use_123:
        if not any(c.isdigit() for c in password_generate):
            password_generate = "".join(random.choice(chars) for _ in range(length_password))
            password_generate = checker(password_generate, use_ABC, use_123, use_specsymbols, chars)
    if use_specsymbols:
        if not any(c in string.punctuation for c in password_generate):
            password_generate = "".join(random.choice(chars) for _ in range(length_password))
            password_generate = checker(password_generate, use_ABC, use_123, use_specsymbols, chars)
    return password_generate
            

def commands(length_password, use_ABC, use_123, use_specsymbols): #Текстовый интерфейс | Text interface
    print("Выберите нужную команду при помощи ввода текста с клавиатуры")
    print("generate() - генерирует пароль по установленным настройкам")
    print("settings() - переходит в раздел настройки для управления настройками генерации пароля")
    print("exit() - выход из программы")
    code = input("Введите необходимое слово: ")
    match code:
        case "generate()":
            generator(length_password, use_ABC, use_123, use_specsymbols)
        case "settings()":
            print("Настройки генерации:")
            print(f"1 - Количество символов ({length_password})")
            print(f"2 - Использование строчных букв ({"On" if use_ABC == True else "Off"})")
            print(f"3 - Использование цифр ({"On" if use_123 == True else "Off"})")
            print(f"4 - Использование спец. символов (Например, !@#$%) ({"On" if use_specsymbols == True else "Offsetti"})")
            print("0 - Вернуться на главную")
            number = int(input("Введите нужную цифру: "))
            match number:
                case 1:
                    print("Стандартное значение: 8")
                    length_password = int(input("Введите число: "))
                    commands(length_password, use_ABC, use_123, use_specsymbols)
                case 2:
                    print("Стандартное значение: Да")
                    print("1 - Да")
                    print("0 - Нет")
                    if int(input("Введите цифру: ")) == 1:
                        use_ABC = True
                    else:
                        use_ABC = False
                    commands(length_password, use_ABC, use_123, use_specsymbols)
                case 3:
                    print("Стандартное значение: Да")
                    print("1 - Да")
                    print("0 - Нет")
                    if int(input("Введите цифру: ")) == 1:
                        use_123 = True
                    else:
                        use_123 = False
                    commands(length_password, use_ABC, use_123, use_specsymbols)
                case 4:
                    print("Стандартное значение: Да")
                    print("1 - Да")
                    print("0 - Нет")
                    if int(input("Введите цифру: ")) == 1:
                        use_specsymbols = True
                    else:
                        use_specsymbols = False
                    commands(length_password, use_ABC, use_123, use_specsymbols)
                case 0:   
                    commands(length_password, use_ABC, use_123, use_specsymbols)
        case "exit()":
            code = 0
            exit()

print("Здравствуйте! Это генератор паролей. Здесь Вы можете сгенерировать пароль по своему вкусу.")
commands(length_password, use_ABC, use_123, use_specsymbols)