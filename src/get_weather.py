import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime

def get_weather_istanbul():
    url = "https://www.mgm.gov.tr/?il=Istanbul"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table")

    rows = []
    for tr in table.find_all("tr")[1:]:
        tds = tr.find_all("td")
        if len(tds) < 4:
            continue
        day = tds[0].text.strip()
        temp = tds[1].text.strip()
        rain = tds[2].text.strip()
        hum = tds[3].text.strip()

        date = datetime.datetime.strptime(day, "%d.%m.%Y").date()

        rows.append([date, temp, rain, hum])

    df = pd.DataFrame(rows, columns=["date", "temperature", "rainfall", "humidity"])
    df.to_csv("data/weather_clean.csv", index=False)
    print("✓ Weather data saved → data/weather_clean.csv")

if __name__ == "__main__":
    get_weather_istanbul()
