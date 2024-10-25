import os
import string
from http import HTTPStatus
from string import punctuation

import requests
from bs4 import BeautifulSoup


def get_content_from_nature(path):
    url = "https://www.nature.com/nature" + path
    # headers = {'Accept': 'application/json'}
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if response.status_code == HTTPStatus.OK:
        return response
    else:
        print(f"The URL returned {response.status_code}!")


def save_content_to_file(file_name, file_content, directory_name):
    file = open(f'{directory_name}/{file_name}' + ".txt", 'wb')
    file.write(file_content.encode('utf-8'))
    file.close()


def search_for_articles_with_tag(soup, search_param):
    articles = soup.find_all("article")
    # print(articles)
    new_articles = []
    for article in articles:
        spans = article.find_all("span", {"data-test": "article.type"})
        for span in spans:
            if span.text == search_param:
                new_articles.append(article)
    return new_articles

def search_for_article_content(path):
    get_content_from_nature(path)
    article_content_response = get_content_from_nature(path)
    article_soup = BeautifulSoup(article_content_response.content, 'html.parser')
    article_content_title = article_soup.find("title")
    article_content_p = article_soup.find("p", {"class": "article__teaser"})
    return {article_content_title.text: article_content_p.text}


def parse_article_tite(title):
    return (title.translate(str.maketrans('', '', punctuation))
            .rstrip()
            .replace(" ", "_"))

def parse_article_content(article):
    return article.rstrip()

def read_user_search_query():
    number_of_pages = input()
    search_param = input()
    return search_param, number_of_pages

def scrape_for_article_content(article):
    path = article.find("a", {"data-track-action": "view article"}).get("href")
    return search_for_article_content(path)

def create_directory(directory_index):
    os.mkdir(f"Page_{directory_index}")
    return f"Page_{directory_index}"

def main():

    search_param, number_of_pages = read_user_search_query()

    for i in range(int(number_of_pages)):
        response = get_content_from_nature(f"/articles?sort=PubDate&year=2020&page={i + 1}")
        soup = BeautifulSoup(response.content, 'html.parser')
        founded_articles = search_for_articles_with_tag(soup, search_param)

        directory_name = create_directory(i  + 1)
        list_of_article_contents = []
        for article in founded_articles:
            article_content = scrape_for_article_content(article)
            # list_of_article_contents.append(article_content)
            parsed_article_title = parse_article_tite(list(article_content.keys())[0])
            parsed_article_content = parse_article_content(list(article_content.values())[0])

            save_content_to_file(parsed_article_title, parsed_article_content, directory_name)

    print("Saved all articles.")
main()
