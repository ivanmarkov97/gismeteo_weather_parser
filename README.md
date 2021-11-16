### Parses weather from cities:
1. Moscow
2. St. Petersburg
3. Yekaterinburg
4. Samara
5. Krasnodar
6. Nizhny Novgorod
7. Novosibirsk
8. Tula
9. Ufa
10. Karan
11. Rostov-on-Don
12. Krasnoyarsk
13. Grozny

### Parse weather from city
`python app.py "{city}" {year} {start_month} {end_month} "{file_name}"`

#### args
1. city [str] - one of cities above
2. year [int] - year to parse
3. start_month [int] - month to parse from [1...12]
4. end_month [int] - month to parse to [1...12 ]
5. file_name [str] - output file

### Parse weather from all cities from start_year to current day
`python collect_all_weather.py start_year=2021`

#### args
start_year [int] - start year to parse from (default = 2019)

### Output format
`{"year": 2019, "month": 5, "number": 1, "t_day": 23, "p_day": 736, "cloudy_day": "sun", "phenomenon_day": "sun", "wind_day": 2, "t_night": 15, "p_night": 735, "cloudy_night": "sun", "phenomenon_night": "sun", "wind_night": 2}`

#### Fields
1. year [int] - parsed year
2. month [int] - parsed month
3. number [int] - day of month
4. t_{day | night} [int] - temperature in the morning / in the night
5. p_{day | night} [int] - atmosphere pressure in the morning / in the night
6. cloudy_{day | night} [str] - cloudy in the morning / in the night
7. phenomenon_{day | night} [str] - phenomenon in the morning / in the night
8. wind_{day | night} [int] - wind speed in the morning / in the night
