import os
import re
from datetime import datetime, timedelta

import scrapy
from scrapy.http import Response
from dotenv import load_dotenv

load_dotenv()


class PlanetSpider(scrapy.Spider):
    name = "planet"
    allowed_domains = os.getenv("ALLOWED_DOMAINS")
    start_urls = os.getenv("START_URL")
    main_page = os.getenv("MAIN_PAGE")

    def parse(self, response: Response, **kwargs):
        for planet in response.css(".dpPlanetCardContent")[1:16]:
            yield {
                "Planet": planet.css(".dpPlanetCell::text").get(),
                "Longitude": self._parse_coordinate(
                    planet, clas_name=".dpLongitudeCell"
                ),
                "Nakshatra": planet.css(".dpNakshatraCell::text").get(),
                "Padam": int(planet.css(".dpPadamCell::text").get()),
                "Nakshatra Lord": planet.css(".dpNakshatraLordCell::text").get(),
                "Full Degree": float(planet.css(".dpFullDegreeCell::text").get()),
                "Latitude/Shara": self._parse_coordinate(
                    planet, clas_name=".dpLatitudeCell"
                ),
                "Speed(deg/day)": float(planet.css(".dpSpeedCell::text").get()),
                "RightAscension": float(planet.css(".dpAscensionCell::text").get()),
                "Declination/Kranti": float(
                    planet.css(".dpDeclinationCell::text").get()
                ),
                "DateTime": self._date_in_table(response=response),
            }

        list_of_date = self._made_date()

        for key, value in list_of_date.items():
            date = key.strftime("%d/%m/%Y")
            for time in value:
                date_time = f"{date}&time={time}:00"
                next_page = self.main_page[0] + f"?date={date_time}"
                yield scrapy.Request(next_page, callback=self.parse)

    def _parse_coordinate(self, response: Response, clas_name: str) -> str:
        element = response.css(clas_name).extract_first()
        if element:
            text = re.search(r"(\d+°) <strong>(\w+)</strong> (\d+′ \d+″)", element)
            if text:
                result = f"{text.group(1)}{text.group(2)}{text.group(3)}"
                return result
        else:
            pass

    def _made_date(self):
        start_date = datetime(1991, 1, 1)
        end_date = datetime(1991, 3, 1)

        date_time_list = {}

        current_date = start_date

        while current_date <= end_date:
            date_time_list[current_date] = [
                "00:00",
                "00:30",
                "01:00",
                "01:30",
                "02:00",
                "02:30",
                "03:00",
                "03:30",
                "04:00",
                "04:30",
                "05:00",
                "05:30",
                "06:00",
                "06:30",
                "07:00",
                "07:30",
                "08:00",
                "08:30",
                "09:00",
                "09:30",
                "10:00",
                "10:30",
                "11:00",
                "11:30",
                "12:00",
                "12:30",
                "13:00",
                "13:30",
                "14:00",
                "14:30",
                "15:00",
                "15:30",
                "16:00",
                "16:30",
                "17:00",
                "17:30",
                "18:00",
                "18:30",
                "19:00",
                "19:30",
                "20:00",
                "20:30",
                "21:00",
                "21:30",
                "22:00",
                "22:30",
                "23:00",
                "23:30",
            ]
            current_date += timedelta(days=1)
        return date_time_list

    def _date_in_table(self, response):
        date_format = "%d/%m/%Y"
        time_format = "%H:%M:%S"

        date = datetime.strptime(str(response.url[84:94]), date_format)
        time = datetime.strptime(str(response.url[100:]), time_format)

        return date.replace(hour=time.hour, minute=time.minute, second=time.second)
