import web
import requests
import json

#/lol/league/v4/challengerleagues/by-queue/{queue}
#la api key cambia cada 24 hrs
api_key = 'RGAPI-1543e424-893f-42d9-8fac-c75e417effd4'
render = web.template.render("riotgames_api/")

class Index():
    def GET(self):
        summoner = None
        return render.index(summoner)

    def POST(self):

        form = web.input()
        tier = form['tier']
        queue = form['queue']
        result = requests.get(
          'https://la1.api.riotgames.com/lol/league/v4/'+str(tier)+'leagues/by-queue/RANKED_'+str(queue)+'?api_key='+str(api_key))
        summoners = result.json()
        items = summoners['entries']
        encoded = json.dumps(items)
        decoded = json.loads(encoded)
        summoner = []

        for summ in decoded:
          summonerName = summ['summonerName']
          leaguePoints = summ['leaguePoints']
          wins = summ['wins']
          hotStreak = summ['hotStreak']
          TD = {"summonerName": summonerName,'leaguePoints':leaguePoints,'wins':wins,'hotStreak':hotStreak}
          summoner.append(TD)

        return render.index(summoner)