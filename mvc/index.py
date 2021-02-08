import web
import requests
import json

render = web.template.render("mvc/")


class Index():
    def GET(self):
        books = None
        return render.index(books)

    def POST(self):
        form = web.input()
        book_name = form["book_name"]
        result = requests.get(
            'https://www.googleapis.com/books/v1/volumes?q=' + book_name)
        books = result.json()
        items = books["items"]
        encoded = json.dumps(items)
        decoded = json.loads(encoded)
        #imp = []
        books = []

        for book in decoded:

            url = book["volumeInfo"]["infoLink"]
            key1 = book["volumeInfo"]["title"]
            key2 = book["volumeInfo"]["authors"]
            key3 = book["volumeInfo"]["infoLink"]
            key4 = book["volumeInfo"]["imageLinks"]["thumbnail"]
            #impD = {"title": key1,"authors":  key2,"infolink": key3, "thumbnail": key4}
            #imp.append(impD)

            datos = {"book_name": book_name, "url": url,"title": key1,"authors":  key2,"infolink": key3, "thumbnail": key4}
            books.append(datos)


            
        print("15")
        print(books)
        print("15")

        #print(imp)



        return render.index(books)
