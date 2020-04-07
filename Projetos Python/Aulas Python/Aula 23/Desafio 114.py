import urllib
import urllib.request

try:
    site = 'http://pudim.com.br'
    urllib.request.urlopen(site)
except urllib.error.URLError:
    print(f'O site {site} não está acessível.')
else:
    print(f'Consegui acessar o {site}')
