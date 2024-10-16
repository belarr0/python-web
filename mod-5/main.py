<<<<<<< HEAD
=======
import asyncio
from currency_api import CurrencyAPI
from currency_service import CurrencyService

async def main():
    try:
        days = int(input("Введіть кількість днів (1-10): "))
        if days < 1 or days > 10:
            print("Будь ласка, введіть число від 1 до 10.")
            return
    except ValueError:
        print("Некоректний ввід. Будь ласка, введіть правильне число.")
        return

    currencies_input = input("Введіть бажані валюти через кому (за замовчуванням USD, EUR): ")
    currencies = [currency.strip().upper() for currency in currencies_input.split(',')] if currencies_input else ['USD', 'EUR']

    api = CurrencyAPI()
    service = CurrencyService(api)

    result = await service.get_filtered_rates(days, currencies)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
>>>>>>> ca91882c97f29695aec9c6a5bd157e2f7e26c912
