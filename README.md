# rPiCryptoPrice
Display price of one selected top 50 Crypto assets on Coinmarketcap at LCD Display.

Requirements:
One MariaDB Database
Coinmarketcap API Key for cfg.ini

You can change Currency and Coin to display also in cfg.ini

You need to start api.py this will create needed DB-Tables on initial startup if not there already.
api.py will update the Price and Display every 5 Minutes.
