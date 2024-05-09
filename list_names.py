from fake_headers import Headers
import bs4
from requests_html import HTMLSession


def get_list_names(tag):
    session = HTMLSession()
    headers_gen = Headers(on = 'win', browser = 'yandex')
    HOST = f'https://names.neolove.ru/national/russkoe/{tag}/'
    response = session.get(url = HOST, headers = headers_gen.generate())
    main_html_data =response.text
    soup = bs4.BeautifulSoup(main_html_data, 'lxml')
    data_names = soup.find_all('a', class_ = "blue")
    list_names = [i.text for i in data_names]
    list_names.sort()
    return list_names