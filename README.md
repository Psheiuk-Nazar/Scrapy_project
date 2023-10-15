# Planet Spider

This is a web scraping spider built with Scrapy to collect data about planets from a specific website. It extracts information about planets, including their coordinates, nakshatras, padams, and more.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your local machine.
- Required Python packages, which you can install with `pip`:
  - Scrapy
  - dotenv

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/planet-spider.git
2. cd planet-spider
3. pip install -r requirements.txt

## Usage
To use the Planet Spider, follow these steps:

Make sure you have set up the necessary environment variables. Create a .env file in your project directory and define the following variables:
   ```
ALLOWED_DOMAINS=your_allowed_domain
START_URL=your_start_url
MAIN_PAGE=your_main_page
   ```

1. scrapy crawl planet
## Data Collected
The spider extracts the following information from the website:
1. Planet name
2. Longitude
3. Nakshatra
4. Padam
5. Nakshatra Lord
6. Full Degree
7. Latitude/Shara
8. Speed (degrees per day)
9. Right Ascension
10. Declination/Kranti
11. Date and Time of data collection
