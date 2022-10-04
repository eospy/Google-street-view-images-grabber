import os
import urllib.parse
import urllib.request
import json
class Main(object):
    myloc = r"YOUR_LOCATION"
    #google street view api key
    key = "&key=" + "AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg" 
    #image getting function
    def GetStreet(self,Add,SaveLoc):
        if self.Checkresponsestatus(Add=Add):
            base = "https://maps.googleapis.com/maps/api/streetview?size=1200x800&location="
            MyUrl = base + urllib.parse.quote_plus(Add) + self.key #added url encoding
            fi = Add + ".jpg"
            urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))
        else:print('image is not available',end=' ')
    #check if image is available
    def Checkresponsestatus(self,Add):
         base = "https://maps.googleapis.com/maps/api/streetview/metadata?location="
         MyUrl = base + urllib.parse.quote_plus(Add) + self.key #added url encoding
         req=urllib.request.Request(url=MyUrl)
         with urllib.request.urlopen(req) as resp:
             data = json.loads(resp.read().decode("utf-8"))
             if data["status"]=="ZERO_RESULTS":
                 return False
             else: return True
   
    #test for some locations
    def Testmethod(self):
        Tests = ["457 West Robinwood Street, Detroit, Michigan 48203",
         "1520 West Philadelphia, Detroit, Michigan 48206",
         "2292 Grand, Detroit, Michigan 48238",
         "15414 Wabash Street, Detroit, Michigan 48238",
         "15867 Log Cabin, Detroit, Michigan 48238",
         "3317 Cody Street, Detroit, Michigan 48212",
         "14214 Arlington Street, Detroit, Michigan 48212"]
        for i in Tests:
          self.GetStreet(Add=i,SaveLoc=self.myloc)
          print (i)
    #deserialization of geojson and appliing image getting function
    def Parseaddr(self):
        data = [json.loads(line) for line in open('geo.geojson', 'r')]
        for i in range(len(data)):
            self.GetStreet(Add=(" ".join((data[i]['properties']['number'],data[i]['properties']['street'],data[i]['properties']['region'],data[i]['properties']['city'],data[i]['properties']['postcode']))),SaveLoc=self.myloc)
            print(data[i]['properties']['street'])
         
testobj = Main()
testobj.Parseaddr()


