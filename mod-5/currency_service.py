class CurrencyService:
    def __init__(self, api):
        self.api = api

    async def get_filtered_rates(self, days, currencies=['USD', 'EUR']):
        data = await self.api.get_exchange_rates(days)
        filtered_data = []
        for day_data in data:
            if day_data:
                date = day_data.get('date')
                rates = {currency: {
                    'sale': next(item['saleRate'] for item in day_data['exchangeRate'] if item['currency'] == currency),
                    'purchase': next(item['purchaseRate'] for item in day_data['exchangeRate'] if item['currency'] == currency)
                } for currency in currencies if any(item['currency'] == currency for item in day_data['exchangeRate'])}
                filtered_data.append({date: rates})
        return filtered_data
