import sqlite3
import requests 
from bs4 import BeautifulSoup
import csv
url="https://realpython.github.io/fake-jobs"
res=requests.get(url)
res.status_code

if res.status_code==200:
    soup=BeautifulSoup(res.text, "html.parser")
else:
    print(f"Error occurred. Status code: {res.status_code}")

titles=soup.find("body")
#get job title
rows_job_titles=titles.find_all("h2")  
job_titles=[row.text.strip() for row in rows_job_titles]
#get company name
rows_company_name=titles.find_all("h3")
company_name=[row.text.strip() for row in rows_company_name]
#get location
rows_location_title=titles.find_all("p",class_="location")
location=[row.text.strip() for row in rows_location_title]
#get job links
job_link=[]
rows_job_links=titles.find_all('footer', class_='card-footer')
for row in rows_job_links:
    links=row.find_all('a')
    if len(links)>1:
        link=links[1]['href']
        job_link.append(link)      
with sqlite3.connect("jobs.db") as data:
    cursor=data.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs(
    Job_Title TEXT NOT NULL,
    Company_Name TEXT NOT NULL,
    Location TEXT NOT NULL,
    Application_Link TEXT NOT NULL
    )
    """)
    for i in range(len(job_titles)):
        cursor.execute("""
        SELECT*FROM jobs WHERE Job_Title=? AND Company_Name=? AND Location=? 
        """,(job_titles[i],company_name[i],location[i])) #checking for unique data
        if not cursor.fetchone():
            cursor.execute("""
            INSERT INTO jobs (Job_Title,Company_Name,Location,Application_Link)
            VALUES (?,?,?,?)
            """,(job_titles[i],company_name[i],location[i],job_link[i]))
        else:
            cursor.execute("""
            UPDATE jobs
            SET Application_Link=?
            WHERE Job_Title=? AND Company_Name=? AND Location=?
            """, (job_titles[i], company_name[i], location[i], job_link[i]))
    data.commit()

def filter_jobs(location=None, company_name=None):
    with sqlite3.connect("jobs.db") as data:
        cursor = data.cursor()
        query = "SELECT * FROM jobs WHERE 1=1"
        params = []

        if location:
            query += " AND Location LIKE ?"
            params.append(f"%{location}%")
        if company_name:
            query += " AND Company_Name LIKE ?"
            params.append(f"%{company_name}%")

        cursor.execute(query, params)
        jobs = cursor.fetchall()
        return jobs

def export_to_csv(jobs, filename="filtered_jobs.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Job_Title", "Company_Name", "Location", "Application_Link"])
        writer.writerows(jobs)

# Example usage
filtered_jobs = filter_jobs(location="New York", company_name="Python")
export_to_csv(filtered_jobs)
data.commit()