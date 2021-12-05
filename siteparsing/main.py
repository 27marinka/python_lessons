from urllib.parse import urljoin

from siteparsing.parsing import Parser

PROMOPAGEFILENAME = "mainPromoPage.html"
URL = "https://magnit.ru/promo"

def write_to_file(filename, text):
    try:
        file1 = open(filename, "w")
        file1.write(text)
    except Exception:
        pass
    finally:
        file1.close()


def save_page_to_file(url):
    main_page = magnit_parser.get_response_text()
    write_to_file(PROMOPAGEFILENAME, main_page)


def get_page_from_file(filename):
    try:
        file1 = open(filename, "r")
        return file1.read()
    except Exception:
        pass
    finally:
        file1.close()



def parse_all_links(links):
    for link in links:
        url = urljoin(URL, link)
        promo_parser = Parser(url)
        names = promo_parser.get_promo_name(url)
    print(names)

if __name__ == '__main__':

    magnit_parser = Parser(URL)
   # save_page_to_file(URL)
    main_page = get_page_from_file(PROMOPAGEFILENAME)
    links = magnit_parser.get_promo_links(main_page)


    print(links)


