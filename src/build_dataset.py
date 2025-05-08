import finviz

# Kreiraj screener za filtriranje kompanija iz finansijskog sektora
screener = finviz.Screener(filters=['sector_Financials'])

# Učitaj rezultate
stocks = screener.get_all()

# Struktuiraj u dict format
companies = {}
for stock in stocks:
    ticker = stock['Ticker']
    name = stock['Company']
    exchange = stock['Exchange']
    companies[ticker] = {
        'stock-exchange': exchange,
        'name': name
    }

# Prikaz rezultata
print(companies)
