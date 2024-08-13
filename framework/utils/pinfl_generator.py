import random


def calculate_checksum(pin):
    """Вычисление контрольной цифры для ПИН ФЛ"""
    weights = [7, 3, 1]
    checksum = sum(int(digit) * weights[i % 3] for i, digit in enumerate(pin))
    return str(checksum % 10)


def random_sex_century_index():
    """Генерация случайного индекса пола и века рождения"""
    return random.choice([1, 2, 3, 4])  # 1, 3 для мужчин; 2, 4 для женщин


def random_birth_date():
    """Генерация случайной даты рождения (ДДММГГ)"""
    day = f"{random.randint(1, 28):02d}"  # Ограничиваемся 28 днями для простоты
    month = f"{random.randint(1, 12):02d}"
    year = f"{random.randint(0, 99):02d}"  # 2 цифры для года
    return f"{day}{month}{year}"


def random_region_code():
    """Генерация случайного кода региона/города (3 цифры)"""
    return f"{random.randint(1, 999):03d}"


def random_serial_number():
    """Генерация случайного порядкового номера гражданина (3 цифры)"""
    return f"{random.randint(1, 999):03d}"


def generate_random_pin_fl():
    """
    Генерация случайного ПИН ФЛ
    """
    sex_century_index = random_sex_century_index()
    birth_date = random_birth_date()
    region_code = random_region_code()
    serial_number = random_serial_number()

    pin = f"{sex_century_index}{birth_date}{region_code}{serial_number}"
    checksum = calculate_checksum(pin)

    return pin + checksum
