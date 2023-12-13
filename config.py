import configparser

conf = configparser.ConfigParser()
conf.read('cfg.ini')

key = conf.get('API', 'key')

subject = conf.get('MAIL', 'subject')
mailfrom = conf.get('MAIL', 'from')
smtp = conf.get('MAIL', 'smtp')
mail_usr = conf.get('MAIL', 'user')
mail_pwd = conf.get('MAIL', 'pwd')

duser = conf.get('DATABASE', 'user')
dpassword = conf.get('DATABASE', 'password')
dhost = conf.get('DATABASE', 'host')
ddatabase = conf.get('DATABASE', 'database')

conin2display = conf.get('CURRENCY', 'coin2display')
fiat_currency = conf.get('CURRENCY', 'fiat_currency')

print('CFG erfolgreich geladen')