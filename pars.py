import mechanize
from bs4 import BeautifulSoup
import hashlib
from urllib import error
from mechanize import HTTPError
from multiprocessing import Pool
import os


class Parser:
    def __init__(self, url, depth, folder="images"):
        self.folder = folder
        self.url = url
        self.depth = depth
        self.links = set()
        self.processes = 60
        self.add_links([[url]])

    @property
    def br(self):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-agent', 'Firefox')]
        return br

    def add_links(self, links):
        for links_ in links:
            for link in links_:
                self.links.add(link)

    def find_links(self, url):
        try:
            html = self.br.open(url, timeout=5).read()
        except error.HTTPError:
            return []
        except error.URLError:
            return []
        soup = BeautifulSoup(html, features="html5lib")
        links = []
        for link in soup.findAll("a", href=True):
            link = link["href"]
            if "http://" in link or "https://" in link:
                links.append(link)
            else:
                links.append(f"{self.url}{link}")
        return links

    def find_all_links(self):
        for level in range(self.depth):
            links = self.links.copy()
            with Pool(processes=self.processes) as pool:
                self.add_links(pool.map(self.find_links, links))
            print(f"Level {level} is finished!")

    def save_images_in_link(self, url):
        formats = ["jpg", "png", "svg", "png"]
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        try:
            html = self.br.open(url, timeout=5).read()
        except HTTPError:
            return
        except error.URLError:
            return
        soup = BeautifulSoup(html, features="html5lib")
        for link in soup.findAll("img"):
            link = link.get("src")
            if link:
                if link[-3:] in formats:
                    if link[0] == "/":
                        link = f"{self.url}{link}"
                    try:
                        data = self.br.open(link).read()
                        form = link[-3:]
                        name = hashlib.md5(data).hexdigest()
                        save = open(f"{self.folder}/{name}.{form}", 'wb')
                        save.write(data)
                        save.close()
                        print(f"{name} is Done!")
                    except error.HTTPError:
                        pass
                    except TimeoutError:
                        pass
                    except error.URLError:
                        pass
                    except mechanize.BrowserStateError:
                        pass

    def save_images(self):
        with Pool(processes=self.processes) as pool:
            pool.map(self.save_images_in_link, self.links)


if __name__ == '__main__':
    Parser(
        "https://yummyanime.club/catalog",
        3,
        "images"
    ).save_images()
