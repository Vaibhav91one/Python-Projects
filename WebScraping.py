import requests as request
from bs4 import BeautifulSoup as bs

options = {1: "https://thehackernews.com/", 2: "https://thehackernews.com/search/label/data%20breach",
           3: "https://thehackernews.com/search/label/Cyber%20Attack",
           4: "https://thehackernews.com/search/label/Vulnerability",
           5: "https://thehackernews.com/search/label/Malware"}


def print_options():
    print(
        "Press 1 for Hacker news Home\n Press 2 for Data Breaches News\n Press 3 for Cyber Attacks News\n Press 4 for "
        "Vulnerability News\n Press 5 for Malware News\n")

print_options()
user_input = int(input("What do you want to know about? "))
data_url = options.get(user_input)


def data_collector(data_url_f):
    r = request.get(data_url)
    soup = bs(r.content, "html.parser")
    for link in soup.find_all('a', class_="story-link"):
        print(link.get('href'))
    More_data()


def More_data():
    user_input2 = str(input("Do you want more news related to the topic? (1/0)"))
    while user_input2 == "1":
        r = request.get(data_url)
        soup = bs(r.content, "html.parser")
        next_page_element = soup.find("a", title="Older Posts")
        next_page = next_page_element.get("href")
        data_collector(next_page)

    else:
        user_input3 = str(input("Do you want news about some other topics? (1/0)"))
        if user_input3 == "1":
            print_options()
            user_input4 = int(input("What do you want to know about? "))
            data_url_d = options.get(user_input)
            data_collector(data_url_d)
        else:
            exit()


data_collector(data_url)
