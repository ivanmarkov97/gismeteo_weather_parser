import re
import argparse

import scrapy

from scrapy.crawler import CrawlerProcess


class Weather(object):

	def __init__(self,
				 year: str,
				 month: str,
				 number: str,
				 t_day: str,
				 p_day: str,
				 cloudy_day: str,
				 phenomenon_day: str,
				 wind_day: str,
				 t_night: str,
				 p_night: str,
				 cloudy_night: str,
				 phenomenon_night: str,
				 wind_night: str) -> None:

		self.year = int(year)
		self.month = int(month)
		self.number = int(number)
		self.t_day = int(t_day.replace('+', ''))
		self.p_day = int(p_day.replace('+', ''))
		self.cloudy_day = cloudy_day
		self.phenomenon_day = phenomenon_day
		self.t_night = int(t_night)
		self.p_night = int(p_night)
		self.cloudy_night = cloudy_night
		self.phenomenon_night = phenomenon_night

		wind_day_info = wind_day.split()
		if len(wind_day_info) > 1:
			self.wind_day = int(wind_day_info[1].replace('м/с', ''))
		else:
			self.wind_day = 0

		wind_night_info = wind_night.split()
		if len(wind_night_info) > 1:
			self.wind_night = int(wind_night_info[1].replace('м/с', ''))
		else:
			self.wind_night = 0

	def __dict__(self):
		return {
			'year': self.year,
			'month': self.month,
			'number': self.number,
			't_day': self.t_day,
			'p_day': self.p_day,
			'cloudy_day': self.cloudy_day,
			'phenomenon_day': self.phenomenon_day,
			'wind_day': self.wind_day,
			't_night': self.t_night,
			'p_night': self.p_night,
			'cloudy_night': self.cloudy_day,
			'phenomenon_night': self.phenomenon_night,
			'wind_night': self.wind_night
		}


class MySpider(scrapy.Spider):
	name = 'gis_meteo'
	start_urls = []

	base_urls = {
		'Moscow': 'https://www.gismeteo.ru/diary/4368', # Moscow
		'St. Petersburg': 'https://www.gismeteo.ru/diary/4079', # Spb
		'Yekaterinburg': 'https://www.gismeteo.ru/diary/4517', # Ekaterinburg
		'Samara': 'https://www.gismeteo.ru/diary/4618', # Samara
		'Krasnodar': 'https://www.gismeteo.ru/diary/5136', # Krasnodar
		'Nizhny Novgorod': 'https://www.gismeteo.ru/diary/4355', # Nizhniy Novgorod
		'Novosibirsk': 'https://www.gismeteo.ru/diary/4690', # Novosibirsk
		'Tula': 'https://www.gismeteo.ru/diary/4392', # Tula
		'Ufa': 'https://www.gismeteo.ru/diary/4588', # Ufa
		'Karan': 'https://www.gismeteo.ru/diary/4364', # Kazan
		'Rostov-on-Don': 'https://www.gismeteo.ru/diary/5110', # Rostov-on-Don
		'Krasnoyarsk': 'https://www.gismeteo.ru/diary/4674', # Krasnoyark
		'Grozny': 'https://www.gismeteo.ru/diary/5256' # Grozniy
	}

	def __init__(self, city: str = 'msc', year: int = 2021, start_month: int = 0, end_month: int = 1, *args, **kwargs):

		assert start_month < end_month

		for month in range(start_month, end_month):
			base_url = self.base_urls[city]
			self.start_urls.append(f'{base_url}/{year}/{month}')

		super().__init__(*args, **kwargs)

	def parse(self, response, **kwargs):
		table = response.xpath('//div[@id="data_block"]/table/tbody[1]/tr')
		year = response.url.split('/')[-3]
		month = response.url.split('/')[-2]

		for row in table.css('tr'):
			item = []
			for child in row.css('td'):
				text = child.css('::text').get()
				if text:
					print('TEXT', text)
					item.append(text)
				else:
					image = child.css('img').get()
					if image is not None:
						re_result = re.findall('/[a-z]+.png', image)[0]
						if re_result:
							re_result = re_result.replace('/', '')
							re_result = re_result.replace('.png', '')
							item.append(re_result)
					else:
						item.append('sun')
			print('#' * 100)
			item = [year, month] + item
			yield Weather(*item).__dict__()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='GisMeteo Moscow Parser')

	parser.add_argument('city', type=str,
						help='city name',
						choices=['Moscow', 'St. Petersburg', 'Yekaterinburg', 'Samara',
				  				 'Krasnodar', 'Nizhny Novgorod', 'Novosibirsk', 'Tula',
				  				 'Ufa', 'Karan', 'Rostov-on-Don', 'Krasnoyarsk', 'Grozny'])
	parser.add_argument('year', type=int, help='Year to parse')
	parser.add_argument('start_month', type=int, help='Begin month to parse')
	parser.add_argument('end_month', type=int, help='End month to parse')
	parser.add_argument('file', type=str, help='file to write result')

	args = parser.parse_args()

	setting = {
		'FEED_FORMAT': 'json',
		'FEED_OVERWRITE': True,
		'FEED_URI': args.file
	}

	process = CrawlerProcess(setting)
	process.crawl(MySpider, city=args.city, year=args.year, start_month=args.start_month, end_month=args.end_month)
	result = process.start()
