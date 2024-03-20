from bs4 import BeautifulSoup
import requests
import lxml
import html5lib

def my_func(position):
        my_items=dict()
        for i in range(1,5):
            print(f"Page number is :  {i}")
            url=requests.get(f'''https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResult
                            Size=25&txtKeywords=0DQT0Data%20Analyst0DQT0&postWeek=60&searchType=personalizedSearch&act
                            ualTxtKeywords=0DQT0{position}0DQT0&searchBy=0&rdoOperator=OR&pDate=I&sequence=3&startPage={i}''').text
            soup=BeautifulSoup(url,"lxml")
            whole_page=soup.find("ul",class_="new-joblist")
            jobs=whole_page.find_all("li",class_="clearfix job-bx wht-shd-bx")
            for job in jobs:
                company_name=job.find("h3",class_="joblist-comp-name").text.replace(" ","").strip().strip("(MoreJobs)").strip()
                company_exp_req=job.find("ul",class_="top-jd-dtl clearfix").li.text.replace(" ","").strip().lstrip("card_travel").strip()
                dat=job.find("span",class_="sim-posted").text.replace(" ","").strip()
                my_items[f"{company_name}"]=[company_exp_req,dat]

        return (my_items)
if __name__=="__main__":
    aa=my_func("data analyst")
    print(aa)
