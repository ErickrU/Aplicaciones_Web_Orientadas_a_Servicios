import web

urls = ('/', 'zod.index.Index')

app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()


#from os import system
#system("pkill -9 python")
