def celsius_to_fahrenheit(celsius):
    """Конвертирует градусы Цельсия в Фаренгейты"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Конвертирует градусы Фаренгейта в Цельсии"""
    return (fahrenheit - 32) * 5/9

# Использование
if __name__ == "__main__":
    print("Конвертер температуры")
    print("1. Цельсий → Фаренгейт")
    print("2. Фаренгейт → Цельсий")
    
    choice = input("Выберите опцию (1 или 2): ")
    
    if choice == "1":
        temp = float(input("Введите температуру в °C: "))
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.1f}°F")
    elif choice == "2":
        temp = float(input("Введите температуру в °F: "))
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.1f}°C")
    else:
        print("Неверный выбор")