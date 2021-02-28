import web
import json
import datetime

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
      
        parameters = web.input() 
        name = str(parameters.name)
        day = int(parameters.day)
        month = int(parameters.month)
        year = int(parameters.year)
        action = str(parameters.action)

        borndate = (str(day)+"/"+str(month)+"/"+str(year))
        currentAge = str(self.howolrdareyou(year, month, day))
        
        json_file = {}
        with open("static/data.json") as file:
          json_file = json.load(file)
        content = {"name": name, "borndate": borndate, "age": currentAge}

        if action == "put":            
            json_file["log"].append(content)
            with open('static/data.json','w') as file:
                json.dump(json_file, file)
            data = {}
            data["register"] = "success"
            return json.dumps(data)

        elif action == "get":
            return json.dumps(json_file)   

        else:
            data = {}
            data["status"] = "something went wrong :p "
            return json.dumps(data)

if __name__ == "__main__":
    app.run()