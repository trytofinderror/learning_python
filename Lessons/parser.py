import requests
from bs4 import BeautifulSoup as bs4


def get_html(url: str) -> str:
    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    }
    session = requests.Session()
    request = session.get(url, headers=headers)
    try:
        if request.status_code == 200:
            return str(request.content)
        else:
            return f"Сервер сайта вернул ошибку {request.status_code}"
    except Exception:
        return "Что-то пошло не так, проверьте правильность введенного URL"


def get_node_content(html: str) -> str:
    if not bool(bs4(html, "html.parser").find()):
        return "В полученной строке html-тегов не обнаружено"
    else:
        node = bs4(html, "html.parser").select_one("*[itemprop='headline']")
        return node.text


html = get_html("https://ria.ru/20240106/solntse-1919941148.html")
text = get_node_content(html)

print(text)
