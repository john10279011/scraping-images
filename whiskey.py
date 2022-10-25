from bs4 import BeautifulSoup
import requests
import os

url = "https://www.jessops.com/drones"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
images = soup.find_all("img")


try:
    os.mkdir(os.path.join(os.getcwd(), "drones"))
except:
    pass
os.chdir(os.path.join(os.getcwd(), "drones"))
for image in images:

    try:
        name = image["alt"]
    except:
        name = ""
    link = image["src"]
    try:
        with open(name + ".jpg", "wb") as f:
            im = requests.get(link)
            f.write(im.content)
            print("writting", name)
    except:
        pass
