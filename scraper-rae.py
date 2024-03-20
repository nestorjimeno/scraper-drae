from bs4 import BeautifulSoup
import requests, sys
from datetime import datetime

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

def main():
    if len(sys.argv) > 1:
        palabra = sys.argv[1]
        print(f'\nDefinición de {palabra}:\n')
    else:
        palabra = palabra_del_dia()
        if not palabra:
            print('No se pudo obtener la palabra del día.')
            return
        print(f'\nDefinición de {palabra} (palabra del día {datetime.now().strftime("%d/%m/%Y")}):\n')
    try:
        for acepcion in acepciones(palabra):
            print(acepcion)
    except Exception as e:
        print(f"Error al obtener las acepciones de '{palabra}': {e}")
        return


def palabra_del_dia():
    try:
        request = requests.get('https://dle.rae.es/', headers=HEADER)
        soup = BeautifulSoup(request.text, 'lxml')
        wotd = soup.find(attrs={'id':'wotd'})
        return wotd.text.strip() if wotd else None
    except Exception as e:
        print(f"Error al obtener la palabra del día: {e}")
        return None


def acepciones(palabra):
    try:
        request = requests.get(f'https://dle.rae.es/{palabra}', headers=HEADER)
        soup = BeautifulSoup(request.text, 'lxml')
        aceps_text = [a.text for a in soup.find_all(attrs={'class':'j'})]
        return aceps_text if aceps_text else ['La palabra que has indicado no está recogida en la RAE.',]
    except Exception as e:
        print(f"Error al obtener las acepciones de '{palabra}': {e}")
        return

if __name__ == '__main__':
    main()
    print('\n')