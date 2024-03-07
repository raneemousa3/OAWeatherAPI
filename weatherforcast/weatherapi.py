import requests
import matplotlib.pyplot as plt
class WeatherinGermany:
    def __init__(self,days):
        self.apiurl= "https://api.open-meteo.com/v1/dwd-icon?latitude=52.52&longitude=13.41&current=temperature_2m&hourly=temperature_2m&forecast_days="+str(days)
        self.times={}
        self.temperatures={} #initialising attributes for the weather
        self.days=days
        self.hour_temp=None
        self.hourly_temp=None
        self.response=requests.get(self.apiurl).json() #getting back data as json
    def get_response(self):
        return(self.response) #returns json data
    def get_temp(self):
        self.hour_temp=self.response['hourly']
        print(self.hour_temp)
        self.hourly_temp=self.hour_temp['temperature_2m']
        for temperature, timestamp in zip(self.hourly_temp, self.hour_temp['time'] ):
            oflist=timestamp.split('T')
            if oflist[0] not in self.temperatures:
                self.temperatures[oflist[0]]=[temperature]
            else:
                self.temperatures[oflist[0]].append(temperature)
            
        print(self.temperatures) #getting temperatures of each day as dict

    def get_time(self):
        Timeofday=self.hour_temp['time']
        #print(Timeofday).
        for datetime in Timeofday:      #getting  time as dicts with the date as the key
            oflist=datetime.split('T')
            if oflist[0] not in self.times:
                self.times[oflist[0]]=[oflist[1]]
            else:
                self.times[oflist[0]].append(oflist[1])
        
        #print(self.times)
    def graph_it(self):
       for key in self.times:
         plt.plot(self.times[key],self.temperatures[key],label=str(key))
         plt.xlabel('Time of Day')
         plt.ylabel('Temperature (°C)')
         plt.title('Hourly Temperature')
         plt.xticks(rotation=45)  #graphing time vs temperature for each day 
         plt.legend()
       plt.show()
weather=WeatherinGermany(7) # plotting a tempurature for a particular number of days
weather.get_temp()
weather.get_time()
weather.graph_it()
