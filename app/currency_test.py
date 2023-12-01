import currency_converter
from datetime import date

c = currency_converter.CurrencyConverter()

print("c.convert(100, 'BTC', 'USD', date=date(2014, 3, 28)) : ",c.convert(100, 'EUR', 'USD', date=date(2020, 12, 28)))
print("\nc.convert(100, 'EUR', 'USD', date=date(2023, 2, 28)) : ",c.convert(100, 'EUR', 'USD', date=date(2014, 2, 28)))

print("\nles devises supportées : ",c.currencies)