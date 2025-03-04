import requests

# Получаем текущий курс BTC/USD с Coinbase
def get_btc_usd():
    url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'
    response = requests.get(url)
    data = response.json()
    btc_usd = float(data['data']['amount'])
    return btc_usd

# Получаем текущий курс USD/RUB (например, с API Центробанка)
def get_usd_rub():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'  # API Центробанка
    response = requests.get(url)
    data = response.json()
    usd_rub = float(data['Valute']['USD']['Value'])
    return usd_rub

# Рассчитываем курс BTC/RUB
def calculate_btc_rub():
    btc_usd = get_btc_usd()
    usd_rub = get_usd_rub()
    btc_rub = btc_usd * usd_rub
    return btc_rub

# Функция для сравнения курса трейдера с биржей
def compare_btc_rub(trader_btc_rub):
    btc_rub = calculate_btc_rub()
    difference = trader_btc_rub - btc_rub
    percentage = (difference / btc_rub) * 100
    return btc_rub, difference, percentage

# Пример использования
trader_btc_rub = float(input("Введите курс продажи BTC трейдера в рублях: "))
btc_rub, difference, percentage = compare_btc_rub(trader_btc_rub)

print(f"Курс BTC по Coinbase: {btc_rub:.2f} руб.")
print(f"Разница с курсом трейдера: {difference:.2f} руб.")
print(f"Процент завышения: {percentage:.2f}%")

