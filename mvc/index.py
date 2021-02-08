import web
import requests
import json

render = web.template.render('mvc/')

class Index:

    def GET(self):
        return render.index()

    def POST(self):
        form = web.input()
        book = form.book
        result = requests.get('https://www.googleapis.com/books/v1/volumes?q='+book)
        
        books = result.json()
        print(type(books))

        items = books["items"]

        coded = json.dumps(items)
        decoded = json.loads(coded)

        print(decoded[0]["volumeInfo"]["infoLink"])
        
        url = decoded[0]["volumeInfo"]["infoLink"]

        link = "<a target='blank' href='"+url+"'>"+book+"</a>"

        return link