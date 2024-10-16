import aiohttp
import asyncio
import datetime


async def fetch_api_data_by_date(date):
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + date) as response:
            data_api = await response.json()  # Await the response
    return data_api


async def get_days(days: int):
    dates = [(datetime.datetime.now() - datetime.timedelta(days=i)).strftime('%d.%m.%Y') for i in range(days)]
    return dates


async def main():
    days = int(input("Enter days (1-10): "))
    if days < 1 or days > 10:
        print("bro.. number between 1-10 wtf?")
        return

    currencies_input = input('Enter currencies (as default USD): ')
    currencies = [curr.strip().upper() for curr in currencies_input.split(',')] if currencies_input else ['USD']

    # Get the dates for the specified number of days
    dates = await get_days(days)

    # Fetch data for each date and display results
    for date in dates:
        data = await fetch_api_data_by_date(date)
        # You can filter the results for the requested currencies here if needed
        print(f"Exchange rates for {date}: {data}")


if __name__ == '__main__':
    asyncio.run(main())
