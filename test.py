# Importing all necessary Libraies

import requests
from selenium import webdriver
import folium
import datetime
import time


# this method will return us our actual coordinates
# using our ip address

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')

        print("="*50)
        print(f"lat: {lat}\nlong: {long}")
        print("="*50)

        return lat, long, city, state
    # return lat, long
    except:
        # Displaying ther error message
        print("Internet Not avialable")
        # closing the program
        exit()
        return False

# cc = 0
# g = True
# while g:
#     cc += 1
#     print(cc)
#     locationCoordinates()
#     if cc == 5:
#         g = False


# def gps_locator():
#     obj = folium.Map(location=[0, 0], zoom_start=2)
#
#     try:
#         lat,long,city,state = locationCoordinates()
#         print("You Are in {},{}".format(city,state))
#         print("Your latitude = {} and longitude = {}".format(lat,long))
#         folium.Marker([lat,long], popup='Current Location').add_to(obj)
#
#         #We have specified our folder location here
#         #You should change this with your folder location
#         #where you want your file
#         fileName = "C:/screengfg/Location" + str(datetime.date.today()) + ".html"
#
#         obj.save(fileName)
#
#         return fileName
#     except:
#         #Displaying ther error message
#         print("Internet Not avialable")
#         #closing the program
#         exit()
#         return False
#
#
# if __name__ == "__main__":
#     print("---------------GPS Using Python---------------\n")
#
#     page = gps_locator()
#     print("\nOpening File.............")
#     dr = webdriver.Chrome()
#     dr.get(page)
#     time.sleep(30)
#     dr.quit()
#     print("\nBrowser Closed..............")
