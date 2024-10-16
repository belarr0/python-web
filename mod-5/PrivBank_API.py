import aiohttp
import asyncio
import datetime

async def fetch_api_data_by_date(date):
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + date) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

async def get_last_three_days(date):
    return [(datetime.datetime.now() - datetime.timedelta(days=date)).strftime('%d.%m.%Y')]

async def final_fetch(dates, fin_curr):
    for date in dates:
        data = await fetch_api_data_by_date(date)
        if data is not None:
            print(f"Exchange rates for {date} (USD):")
            for item in data['exchangeRate']:
                if item['currency'] == 'USD':
                    print(f"USD - Buy: {item.get('purchaseRate', 'N/A')}, Sell: {item.get('saleRate', 'N/A')}")
        else:
            print(f"No data found for {date}")

async def main():
    date_what_need = int(input("Enter day amount(1-10): "))
    try:
        if date_what_need < 1 or date_what_need > 10:
            print("1-10 bro, wtf?")
            return
    except ValueError:
        return

    currency_input = input("Enter currency what u need(USD as default): ")
    final_currency = [curr.strip().upper() for curr in currency_input] if currency_input else 'USD'


    dates = await get_last_three_days(date_what_need)
    final_fetch(dates, final_currency)



if __name__ == '__main__':
    asyncio.run(main())
