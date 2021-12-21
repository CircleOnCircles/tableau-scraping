from tableauscraper import TableauScraper as TS

url= "https://public.tableau.com/views/moph_covid_v3/Story1"
ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

province_ws = workbook.getWorksheet("province_total")
province_ws.getTupleIds()