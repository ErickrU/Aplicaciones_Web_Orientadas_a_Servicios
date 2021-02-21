import web
import json
import datetime

ruteTXT = "static/log.txt"
urls = (
    '/parameters?', 'parameters'
)

app = web.application(urls, globals())

class parameters:
   
    def howolrdareyou(self, year, month, day):
        today = datetime.date.today()
        born = datetime.date(year, month, day)
        currentAge = 0
        while born < today:
            currentAge += 1
            born = datetime.date(year+currentAge, month, day)
        currentAge -= 1
        return currentAge
      
    def GET(self):
        try:
              parameters = web.input() 
              name = str(parameters.name)
              day = int(parameters.day)
              month = int(parameters.month)
              year = int(parameters.year)
              logCon = parameters.logCon

              logtxt = (str(day)+"/"+str(month)+"/"+str(year))
              result = self.howolrdareyou(year, month, day)

              file = open(ruteTXT, 'a')
              file.write(str(name)+'<>'+str(logtxt)+'<>'+str(result)+"\n")
              file.close()    

              if logCon == 'True':
                  file = open(ruteTXT, 'r')
                  dataFile = []
                  elements = {
                      "logs":[
                      ]
                    }
                  elmGG = elements["logs"]

                  for line in file:
                      line=line.replace("\n","")
                      line=line.split("<>")
                      writeInLine = line
                      dataFile.append(writeInLine)
                  file.close()

                  for xqc in dataFile:
                      name = line[0]
                      borndate = line[1]
                      age = line[2]
                      app ={
                          "name":name,
                          "borndate" : borndate,
                          "age": age
                      }
                      elmGG.append(app)
                  return json.dumps(elements)

              else:
                  data = {}
                  data["Edad"] = result
                  return json.dumps(data)

        except:
              data = {}
              data["error"] = "ups alguno de los valores son invalidos o excende el limite :(  \n"
              return json.dumps(data)

if __name__ == "__main__":
    app.run()