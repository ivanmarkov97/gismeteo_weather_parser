import os
import argparse

from datetime import datetime


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--start_year', type=int, default=2019, help='Start year')
	args = parser.parse_args()

	all_cities = ['Moscow', 'St. Petersburg', 'Yekaterinburg', 'Samara',
				  'Krasnodar', 'Nizhny Novgorod', 'Novosibirsk', 'Tula',
				  'Ufa', 'Karan', 'Rostov-on-Don', 'Krasnoyarsk', 'Grozny']

	current_month = datetime.now().month
	current_year = datetime.now().year
	# print(current_month, current_year)

	for city in all_cities:
		for year in range(args.start_year, current_year + 1):
			file_name = f'data/weather_{city}_{year}.json'
			start_month = 1
			if year == current_year:
				end_month = current_month + 1
			else:
				end_month = 12
			print(f'Command: python app.py "{city}" {year} {start_month} {end_month} "{file_name}"')
			os.system(f'python app.py "{city}" {year} {start_month} {end_month} "{file_name}"')
