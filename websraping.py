from bs4 import BeautifulSoup
from selenium import webdriver
import time 
import csv
import requests
Start_url = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("chromedriver.exe")

browser.get(Start_url)

time.sleep(10)

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date","hyperlink", "planet_type", "planet_radius", "orbital_radius", "orbital-period", "eccentricity"]
planetdata = []
new_planet_data = []

def scrape():
    for i in range(0, 457):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class": "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov" + hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            planetdata.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()


def scrape_more_data(hyperlink):
    try:
        page_source = requests.get(hyperlink)
        soup = BeautifulSoup(page_source.content, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr", attrs = {"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs = {"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)
        
scrape()    
for index, data in enumerate(planetdata):
    scrape_more_data(data[5])

final_exoPlanet_data = []


for index,data in enumerate(planetdata):
    final_exoPlanet_data.append(planetdata[index]+new_planet_data[index])

with open("WebScrapping.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_exoPlanet_data)