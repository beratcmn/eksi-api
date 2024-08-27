from playwright.sync_api import sync_playwright
import logging
from bs4 import BeautifulSoup

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class EksiParser:
    BASE_URL = "https://eksisozluk.com"

    def __init__(self, debug=False):
        self.debug = debug

    def get_eksi_page(self, url):
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True, args=["--disable-blink-features=AutomationControlled"]
            )
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            )
            page = context.new_page()
            response = page.goto(url, wait_until="domcontentloaded")

            if response.ok:
                logging.info(f"Page retrieved successfully: {response.url}")
            else:
                logging.error(
                    f"Failed to retrieve the page. Status code: {response.status}"
                )
                return {
                    "url": url,
                    "status": response.status,
                    "error": response.status_text,
                }

            content = page.content()
            browser.close()
            return content

    def get_trending_topics(self):
        html = self.get_eksi_page(self.BASE_URL + "/basliklar/gundem")
        soup = BeautifulSoup(html, "html.parser")
        entries_h1 = soup.find_all("h1", id="title")
        entry_titles = []
        entry_slugs = []
        entry_links = []
        for entry in entries_h1:
            title = entry.get("data-title")
            slug = entry.get("data-slug")
            link = self.BASE_URL + entry.find("a").get("href")
            entry_titles.append(title)
            entry_slugs.append(slug)
            entry_links.append(link)
        entries = []
        for title, slug, link in zip(entry_titles, entry_slugs, entry_links):
            entries.append({"title": title, "slug": slug, "link": link})
        return entries

    def get_topic(self, url, page=1):
        url = f"{url}&p={page}" if page > 1 else url
        logging.info(f"Getting entry: {url}")
        html = self.get_eksi_page(url)
        if self.debug:
            with open("eksi_search.html", "w", encoding="utf-8") as file:
                file.write(html)

        soup = BeautifulSoup(html, "html.parser")

        pager_div = soup.find("div", class_="pager")
        page_count = -1
        if pager_div:
            page_count = pager_div.get("data-pagecount")
            # logging.info(f"Total pages: {page_count}")
        else:
            logging.warning("Pager div not found")

        title = soup.find("title").text
        # logging.info(f"Title: {title}")

        return {"url": url, "title": title, "page": page, "page_count": page_count}

    def search_topic(self, query, page=1):
        query = query.replace(" ", "+")
        query = (
            query.replace("ı", "i")
            .replace("ğ", "g")
            .replace("ç", "c")
            .replace("ş", "s")
            .replace("ö", "o")
            .replace("ü", "u")
        )
        url = self.BASE_URL + f"/?q={query}"
        logging.info(f"Searching for: {url}")

        return self.get_topic(url, page)

    def get_entries_from_url(self, url):
        html = self.get_eksi_page(url)
        soup = BeautifulSoup(html, "html.parser")
        entries_ul = soup.find("ul", id="entry-item-list")
        entries = []
        if entries_ul:
            logging.info("Entries found")
            entries_li = entries_ul.find_all("li", id="entry-item")
            for entry_li in entries_li:
                id = entry_li.get("data-id")
                author = entry_li.get("data-author")
                author_id = entry_li.get("data-author-id")
                content = entry_li.find("div", class_="content")
                if content:
                    content = content.text.strip()
                entries.append(
                    {
                        "id": id,
                        "author": author,
                        "author_id": author_id,
                        "content": content,
                    }
                )
        return entries


if __name__ == "__main__":
    eksi = EksiParser()
    page = eksi.search_topic("elon musk", 1)
    entries = eksi.get_entries_from_url(page["url"])
    for entry in entries:
        print(entry)
