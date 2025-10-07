import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль заданной длины"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Использование
if __name__ == "__main__":
    password_length = int(input("Введите длину пароля: ") or 12)
    new_password = generate_password(password_length)
    print(f"Ваш новый пароль: {new_password}")