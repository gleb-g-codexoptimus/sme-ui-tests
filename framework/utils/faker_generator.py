from faker import Faker


def generate_text(chars, fake=Faker()):
    random_text = fake.text(max_nb_chars=chars)
    return random_text


def generate_phone_number(country_code=False, number_lenth=12, fake=Faker()):
    """
    Генерит рандомный номер с рандомным кодом страны
    Можно указать первые цифры номера, метод отдаст только 12 цифр
    """
    country_code = fake.country_calling_code() if not country_code else country_code
    random_phone_number = f'{country_code}{fake.msisdn()}'.replace(" ", "")
    return random_phone_number[:number_lenth]


def generate_company_name(fake=Faker()):
    return fake.company()
