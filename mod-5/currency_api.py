import aiohttp
import asyncio
from datetime import datetime, timedelta

class CurrencyAPI:
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="

    async def fetch_currency_rate(self, date: str):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"{self.BASE_URL}{date}") as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        response.raise_for_status()
            except aiohttp.ClientError as e:
                print(f"Failed to fetch data: {e}")
                return None

    async def get_exchange_rates(self, days: int):
        today = datetime.now()
        dates = [(today - timedelta(days=i)).strftime('%d.%m.%Y') for i in range(days)]
        tasks = [self.fetch_currency_rate(date) for date in dates]
        return await asyncio.gather(*tasks)
