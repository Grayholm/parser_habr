import asyncio
from dataclasses import dataclass
from typing import List
from fake_useragent import UserAgent

import aiohttp
from bs4 import BeautifulSoup

@dataclass
class ArticleData:
    title: str
    views: str
    url: str

headers = {
    'User-Agent': UserAgent().random,
}

async def http_client(link: str, session: aiohttp.ClientSession) -> List[ArticleData]:
    async with session.get(link, headers=headers) as response:
        response.raise_for_status()
        html = await response.text()
        soup = BeautifulSoup(html, "lxml")

        articles = soup.find_all("article", class_="tm-articles-list__item")
        articles_data: List[ArticleData] = []

        for article in articles:
            title_element = article.find("a", class_="tm-title__link")
            views_element = article.find("span", class_="tm-icon-counter__value")

            title = title_element.get_text(strip=True) if title_element else "Нет заголовка"
            views = views_element.get_text(strip=True) if views_element else "N/A"
            url = title_element.get('href') if title_element else ""

            article_obj = ArticleData(
                title=title,
                views=views,
                url='https://habr.com' + url
            )
            articles_data.append(article_obj)

        return articles_data


async def main():
    link = "https://habr.com/ru/articles/top/daily/"
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            articles = await http_client(link, session)
            for index, article in enumerate(articles, 1):
                print(f"{index}. {article.title} | Просмотры: {article.views} | {article.url}")
    except aiohttp.ClientError as e:
        print(f"Ошибка сети: {e}")
    except Exception as e:
        print(f"Ошибка парсинга: {e}")


if __name__ == "__main__":
    asyncio.run(main())