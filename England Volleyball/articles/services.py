import requests


def get_books(year, author):
    url = 'http://api.example.com/books'
    params = {'year': year, 'author': author}
    r = requests.get(url, params=params)
    books = r.json()
    books_list = {'books': books['results']}
    return books_list

###stuff

def home(request):
    parsedData = []
    response = requests.get('http://127.0.0.1:8000/api/posts/')
    jsonData = json.loads(response.content.decode())
    jsonList = jsonData["url"]
    for cards in jsonList:
        cardData = {}  # move this line inside the loop
        cardData['title'] = cards['title']
        ...
        # make sure this line is inside the loop so that you append
        # every card to parsedData
        parsedData.append(cardData)
    return render(request, 'articles/home.html', {'data': parsedData})
