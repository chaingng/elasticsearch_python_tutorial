import requests
import json
import time
import os

URL = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"

payload = {
    'format': 'json',
    'applicationId': os.environ.get('ES_RAKUTEN_APP_ID'),
    'booksGenreId': '000',
    'keyword': 'Python',
    'page': 1
}

books = []
while True:
    response = requests.get(URL, params=payload)
    data = json.loads(response.text)
    books.extend(data['Items'])
    if data['pageCount'] == data['page']:
        break
    payload['page'] = data['page'] + 1
    time.sleep(1)


with open('rakuten_books.json', 'w') as f:
    json.dump(books, f)
