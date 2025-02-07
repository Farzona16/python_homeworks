from bs4 import BeautifulSoup
#open and read file
with open("weather.html", 'r') as f:
    html_doc=f.read()
#parser file 
soup=BeautifulSoup(html_doc,"html.parser")

#task-2 and 3
forecast_table=soup.find("table")
rows=forecast_table.find_all("tr")[1:]
records=[]
temperatures=[]
for row in rows:
    cols=row.find_all("td")
    day=cols[0].text.strip()
    temperature=cols[1].text.strip()
    condition=cols[2].text.strip()
    print(f"Day: {day}, temperature: {temperature}, condition: {condition}")
    temperatures.append(temperature)
    if condition=='Sunny':
        records.append({day})
print(f"Sunny day(s) are {records} ")
cleaned_temperatures = [int(temp.replace('°C', '').replace('В', '').strip()) for temp in temperatures]
print(f"The hottest temperature is: {max(cleaned_temperatures)}")
avg_temp=sum(cleaned_temperatures)/len(cleaned_temperatures)
print(f"Average temperature: {avg_temp}")