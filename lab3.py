import requests
from datetime import datetime, date, time
output = open('meetup.html',  'w+', encoding='utf-8')
output.write('<!DOCTYPE html><html><head></head><body><h1>EVENTS</h1>')
response = requests.get('https://api.meetup.com/2/open_events?&sign=true&photo-host=public&country=ca&topic=newtech&city=Montreal&key=353f12387d366674666a864273a50').json()
dow = ['Monday',  'Tuesday',  'Wednesday',  'Thursday',  'Friday',  'Saturday',  'Sunday']
for i in range(7):
        output.write('<h2>' + dow[i] + '</h2>')
        for item in response['results']:
                d = datetime.fromtimestamp(int(item['time']) / 1000).weekday()
                if d == i:
                        try:
                                output.write('<div><p>Time: ' + str(datetime.fromtimestamp(int(item['time']) / 1000)) + '</p>')
                        except KeyError:pass
                        try:
                                output.write('<p>Name: ' + str(item['name'] + '</p>'))
                        except KeyError:pass
                        try:
                                output.write('<p>Organizer: ' + str((item['group'])['name']) + '</p>')
                        except KeyError:pass
                        try:
                                output.write('<p>Description: ' + str(item['description']) + '</p>')
                        except KeyError:pass
                        try:
                                output.write("<p>Phone: " + str((item['venue'])['phone']) + '</p>')
                        except KeyError:pass
                        try:
                                output.write("<p>Country: " + str((item['venue'])['localized_country_name']) + '</p>')
                        except KeyError:pass
                        try:
                                output.write('<p>City: ' + str((item['venue'])['city']) + '</p>')
                        except KeyError:pass
                        try:
                                output.write('<p>Address: ' + str((item['venue'])['address_1']) + '</p>')
                        except KeyError:pass
output.write('</div>')
output.write('</body></html>')
output.close()
