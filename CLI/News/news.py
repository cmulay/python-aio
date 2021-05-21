import requests

print('BBC News\n'
      'Fetching news \t⌛')


def get_news(key):
    # You can change this url on https://newsapi.org/
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2021-04-09&sortBy=publishedAt&apiKey={key}'

    contents = requests.get(url).json()
    articles = contents["articles"]
    headlines = []

    for a in articles:
        if len(headlines) == 5:
            break
        headlines.append(a['title'])
    return headlines


class News:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        counter = 1
        for headline in get_news(self.key):
            print(f"{str(counter)}. {headline}")
            counter += 1
        return ""


if __name__ == '__main__':
    api_key = input("Enter your API key: ")
    print('\n')
    print(News(api_key))
