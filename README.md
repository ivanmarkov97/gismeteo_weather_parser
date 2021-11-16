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
start_year [int] - start year to parse from (deefault = 2019)
