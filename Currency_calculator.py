import requests
from bs4 import BeautifulSoup

url = "https://data.fixer.io/api/latest?access_key=70143b7fd15d8a0bbe04f739da9d941a"

response = requests.get(url)

html = response.json()
print("""
    WELCOME TO CURRENCY CALCULATOR

    Press m to view the currencies available for conversion
    If you want to convert to all currency types, Press e 
    Press q to exit 
      
    Developed by Devrim Tunçer
    Github: https://github.com/devrim-1283

""")
currency_dict = {
    'AED': 'United Arab Emirates Dirham',
    'AFN': 'Afghan Afghani',
    'ALL': 'Albanian Lek',
    'AMD': 'Armenian Dram',
    'ANG': 'Netherlands Antillean Guilder',
    'AOA': 'Angolan Kwanza',
    'ARS': 'Argentine Peso',
    'AUD': 'Australian Dollar',
    'AWG': 'Aruban Florin',
    'AZN': 'Azerbaijani Manat',
    'BAM': 'Bosnia-Herzegovina Convertible Mark',
    'BBD': 'Barbadian Dollar',
    'BDT': 'Bangladeshi Taka',
    'BGN': 'Bulgarian Lev',
    'BHD': 'Bahraini Dinar',
    'BIF': 'Burundian Franc',
    'BMD': 'Bermudian Dollar',
    'BND': 'Brunei Dollar',
    'BOB': 'Bolivian Boliviano',
    'BRL': 'Brazilian Real',
    'BSD': 'Bahamian Dollar',
    'BTC': 'Bitcoin',
    'BTN': 'Bhutanese Ngultrum',
    'BWP': 'Botswana Pula',
    'BYN': 'Belarusian Ruble',
    'BZD': 'Belize Dollar',
    'CAD': 'Canadian Dollar',
    'CDF': 'Congolese Franc',
    'CHF': 'Swiss Franc',
    'CLF': 'Chilean Unit of Account (UF)',
    'CLP': 'Chilean Peso',
    'CNY': 'Chinese Yuan',
    'COP': 'Colombian Peso',
    'CRC': 'Costa Rican Colón',
    'CUP': 'Cuban Peso',
    'CVE': 'Cape Verdean Escudo',
    'CZK': 'Czech Koruna',
    'DJF': 'Djiboutian Franc',
    'DKK': 'Danish Krone',
    'DOP': 'Dominican Peso',
    'DZD': 'Algerian Dinar',
    'EGP': 'Egyptian Pound',
    'ERN': 'Eritrean Nakfa',
    'ETB': 'Ethiopian Birr',
    'EUR': 'Euro',
    'FJD': 'Fijian Dollar',
    'GBP': 'British Pound Sterling',
    'GEL': 'Georgian Lari',
    'GHS': 'Ghanaian Cedi',
    'GIP': 'Gibraltar Pound',
    'GMD': 'Gambian Dalasi',
    'GNF': 'Guinean Franc',
    'GTQ': 'Guatemalan Quetzal',
    'GYD': 'Guyanese Dollar',
    'HKD': 'Hong Kong Dollar',
    'HNL': 'Honduran Lempira',
    'HRK': 'Croatian Kuna',
    'HTG': 'Haitian Gourde',
    'HUF': 'Hungarian Forint',
    'IDR': 'Indonesian Rupiah',
    'ILS': 'Israeli New Shekel',
    'INR': 'Indian Rupee',
    'IQD': 'Iraqi Dinar',
    'IRR': 'Iranian Rial',
    'ISK': 'Icelandic Króna',
    'JMD': 'Jamaican Dollar',
    'JOD': 'Jordanian Dinar',
    'JPY': 'Japanese Yen',
    'KES': 'Kenyan Shilling',
    'KGS': 'Kyrgyzstani Som',
    'KHR': 'Cambodian Riel',
    'KMF': 'Comorian Franc',
    'KPW': 'North Korean Won',
    'KRW': 'South Korean Won',
    'KWD': 'Kuwaiti Dinar',
    'KZT': 'Kazakhstani Tenge',
    'LAK': 'Lao Kip',
    'LBP': 'Lebanese Pound',
    'LKR': 'Sri Lankan Rupee',
    'LRD': 'Liberian Dollar',
    'LSL': 'Lesotho Loti',
    'MAD': 'Moroccan Dirham',
    'MDL': 'Moldovan Leu',
    'MGA': 'Malagasy Ariary',
    'MKD': 'Macedonian Denar',
    'MMK': 'Myanmar Kyat',
    'MNT': 'Mongolian Tögrög',
    'MOP': 'Macanese Pataca',
    'MRU': 'Mauritanian Ouguiya',
    'MUR': 'Mauritian Rupee',
    'MVR': 'Maldivian Rufiyaa',
    'MWK': 'Malawian Kwacha',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'MZN': 'Mozambican Metical',
    'NAD': 'Namibian Dollar',
    'NGN': 'Nigerian Naira',
    'NIO': 'Nicaraguan Córdoba',
    'NOK': 'Norwegian Krone',
    'NPR': 'Nepalese Rupee',
    'NZD': 'New Zealand Dollar',
    'OMR': 'Omani Rial',
    'PAB': 'Panamanian Balboa',
    'PEN': 'Peruvian Sol',
    'PGK': 'Papua New Guinean Kina',
    'PHP': 'Philippine Peso',
    'PKR': 'Pakistani Rupee',
    'PLN': 'Polish Złoty',
    'PYG': 'Paraguayan Guarani',
    'QAR': 'Qatari Riyal',
    'RON': 'Romanian Leu',
    'RSD': 'Serbian Dinar',
    'RUB': 'Russian Ruble',
    'RWF': 'Rwandan Franc',
    'SAR': 'Saudi Riyal',
    'SBD': 'Solomon Islands Dollar',
    'SCR': 'Seychellois Rupee',
    'SDG': 'Sudanese Pound',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'SHP': 'Saint Helena Pound',
    'SLE': 'Sierra Leonean Leone',
    'SLL': 'Sierra Leonean Leone',
    'SOS': 'Somali Shilling',
    'SRD': 'Surinamese Dollar',
    'STD': 'São Tomé and Príncipe Dobra',
    'SVC': 'Salvadoran Colón',
    'SYP': 'Syrian Pound',
    'SZL': 'Swazi Lilangeni',
    'THB': 'Thai Baht',
    'TJS': 'Tajikistani Somoni',
    'TMT': 'Turkmenistani Manat',
    'TND': 'Tunisian Dinar',
    'TOP': 'Tongan Paʻanga',
    'TRY': 'Turkish Lira',
    'TTD': 'Trinidad and Tobago Dollar',
    'TWD': 'Taiwan Dollar',
    'TZS': 'Tanzanian Shilling',
    'UAH': 'Ukrainian Hryvnia',
    'UGX': 'Ugandan Shilling',
    'USD': 'United States Dollar',
    'UYU': 'Uruguayan Peso',
    'UZS': 'Uzbekistani Som',
    'VES': 'Venezuelan Bolívar',
    'VND': 'Vietnamese đồng',
    'VUV': 'Vanuatu Vatu',
    'WST': 'Samoan Tala',
    'XAF': 'Central African CFA Franc',
    'XAG': 'Silver (troy ounce)',
    'XAU': 'Gold (troy ounce)',
    'XCD': 'East Caribbean Dollar',
    'XDR': 'Special Drawing Rights (IMF)',
    'XOF': 'West African CFA Franc',
    'XPF': 'CFP Franc',
    'YER': 'Yemeni Rial',
    'ZAR': 'South African Rand',
    'ZMK': 'Zambian Kwacha',
    'ZMW': 'Zambian Kwacha',
    'ZWL': 'Zimbabwean Dollar'
}
def conventer(a,b,c):
    currency_a=None
    currency_b=None
    if a=="M" and b=="M":
        for i,j in html["rates"].items():
            for x,y in html["rates"].items():
                print(f"{c} {i} = {c*j/y} {x}")
    elif b=="M" and a!="M":
        for i,j in html["rates"].items():
            if i == a:
                currency_a=j
        for i,j in html["rates"].items():
            print(f"{c} {a} = {c*currency_a/j} {i}") 
    elif a == "M" and b!="M":
        for i,j in html["rates"].items():
            if i == b:
                currency_b=j
        for i,j in html["rates"].items():
            print(f"{c} {i} = {c*j/currency_b} {b}")
    elif a!="M" and b!="M":
        for i,j in html["rates"].items():
            if i == a:
                currency_a = j
            if i == b:
                currency_b = j
        calculate = currency_b/currency_a
        return c*calculate

def main():
    while True:
        try: 
            exit_value=0
            while True:
                input_a = input("Please enter the currency you want to convert from: ")
                if input_a.lower()=="q":
                    exit_value+=1
                    break
                elif input_a.lower()=="e":
                    for i,j in currency_dict.items():
                        print(i,j)
                    continue
                elif input_a.lower()=="m":
                    break
                elif not input_a.isalpha():
                   raise ValueError
                else:
                    match_value = 0
                    for i,j in html["rates"].items():
                        if input_a.upper() == i:
                            match_value+=1
                    if match_value==0:
                        print("Please enter a valid currency")
                        continue
                    else:
                        break

            if exit_value==1:
                print("Exit succesful............")
                break

            while True:
                input_b = input(f"Which currency would you like to convert the {input_a.upper()} to: ")
                if input_b.lower()=="q":
                   exit_value+=1
                   break
                elif input_b.lower()=="e":
                    for i,j in currency_dict.items():
                        print(i,j)
                    continue
                elif input_b.lower()=="m":
                    break
                elif not input_b.isalpha():
                    raise ValueError
                else:
                    match_value = 0
                    for i,j in html["rates"].items():
                        if input_b.upper() == i:
                            match_value+=1
                    if match_value == 0:
                        print("Please enter a valid currency")
                        continue
                    else:
                        break


            if exit_value==1:
                print("Exit succesful............")
                break

            while True:
                input_c = input(f"How many {input_a.upper()} would you like to convert to {input_b.upper()}: ")
                if input_c.lower()=="q":
                    exit_value+=1
                    break
                elif input_c.lower()=="e":
                    for i,j in currency_dict.items():
                        print(i,j)
                    ConnectionRefusedError
                elif not input_c.isdigit():
                    raise ValueError
                else:
                    input_c=int(input_c)
                    break
            if exit_value==1:
                print("Exit succesful............")
                break      
            if input_a!="m" and input_b!="m":
                print(f"{input_c} {input_a.upper()} = {round(conventer(input_a.upper(),input_b.upper(),input_c),4)} {input_b.upper()}")
            else:
                print(conventer(input_a.upper(),input_b.upper(),input_c))
        except ValueError:
            print("Please enter a valid value.")
if __name__ == "__main__":
    main()