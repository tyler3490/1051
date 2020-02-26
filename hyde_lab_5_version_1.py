# def USD_to_converter(amount):
#     amount = float(input('How much money do you have?: '))
#     currency_you_want = input('What currency do you want?: ')
#     if currency_you_want == EUR: 
#         return amount * 0.85
    
#     # elif currency_you_want == GBP:
# USD_to_converter(1)

# currency_converter()

# def usd_to_eur(amount):
#     return amount * 0.85

# # conversion = usd_to_eur(10)
# print(usd_to_eur(10))


# def USD_to_EUR(amount):
#     return amount * 0.85
# def USD_to_GBP(amount):
#     return amount * 0.76
# def USD_to_JPY(amount):
#     return amount * 112.91
# def USD_to_BRL(amount):
#     return amount * 4.08
import currency_conversion_rates_library

def currency_converter(amount, currency_you_have, currency_you_want):
    if currency_you_have == 'USD' and currency_you_want == 'EUR':
        return currency_conversion_rates_library.USD_to_EUR(amount)
    elif currency_you_have == 'USD' and currency_you_want == 'GBP':
        return currency_conversion_rates_library.USD_to_GBP(amount)
    elif currency_you_have == 'USD' and currency_you_want == 'JPY':
        return currency_conversion_rates_library.USD_to_JPY(amount)
    elif currency_you_have == 'USD' and currency_you_want == 'BRL':
        return currency_conversion_rates_library.USD_to_BRL(amount)
    elif currency_you_have == 'EUR' and currency_you_want == 'USD':
        return currency_conversion_rates_library.EUR_to_USD(amount)
    elif currency_you_have == 'EUR' and currency_you_want == 'GBP':
        return currency_conversion_rates_library.EUR_to_GBP(amount)
    elif currency_you_have == 'EUR' and currency_you_want == 'JPY':
        return currency_conversion_rates_library.EUR_to_JPY(amount)
    elif currency_you_have == 'EUR' and currency_you_want == 'BRL':
        return currency_conversion_rates_library.EUR_to_BRL(amount)
    elif currency_you_have == 'GBP' and currency_you_want == 'USD':
        return currency_conversion_rates_library.GBP_to_USD(amount)
    elif currency_you_have == 'GBP' and currency_you_want == 'EUR':
        return currency_conversion_rates_library.GBP_to_EUR(amount)
    elif currency_you_have == 'GBP' and currency_you_want == 'JPY':
        return currency_conversion_rates_library.GBP_to_JPY(amount)
    elif currency_you_have == 'GBP' and currency_you_want == 'BRL':
        return currency_conversion_rates_library.GBP_to_BRL(amount)
    elif currency_you_have == 'JPY' and currency_you_want == 'USD':
        return currency_conversion_rates_library.JPY_to_USD(amount)
    elif currency_you_have == 'JPY' and currency_you_want == 'EUR':
        return currency_conversion_rates_library.JPY_to_EUR(amount)
    elif currency_you_have == 'JPY' and currency_you_want == 'GBP':
        return currency_conversion_rates_library.JPY_to_GBP(amount)
    elif currency_you_have == 'JPY' and currency_you_want == 'BRL':
        return currency_conversion_rates_library.JPY_to_BRL(amount)
    elif currency_you_have == 'BRL' and currency_you_want == 'USD':
        return currency_conversion_rates_library.BRL_to_USD(amount)
    elif currency_you_have == 'BRL' and currency_you_want == 'EUR':
        return currency_conversion_rates_library.BRL_to_EUR(amount)
    elif currency_you_have == 'BRL' and currency_you_want == 'GBP':
        return currency_conversion_rates_library.BRL_to_GBP(amount)
    elif currency_you_have == 'BRL' and currency_you_want == 'JPY':
        return currency_conversion_rates_library.BRL_to_JPY(amount)

def main():
    amount = float(input('How much money do you have?: '))
    currency_you_have = input('What currency do you have? (USD, EUR, GBP, JPY, BRL): ')
    currency_you_want = input('What currency do you want? (USD, EUR, GBP, JPY, BRL): ')
    converted_currency = currency_converter(amount, currency_you_have, currency_you_want)
    print('Your', amount, currency_you_have, 'is worth', converted_currency, currency_you_want)

main()

