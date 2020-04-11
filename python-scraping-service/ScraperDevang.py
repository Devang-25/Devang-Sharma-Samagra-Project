# All Rights Reserved By: Devang Sharma

    import requests
    from lxml import html
    import requests
	from bs4 import BeautifulSoup
	import csv
	import json



    with requests.Session() as session:
    page = session.get('https://swayam.gov.in/explorer')
    tree = html.fromstring(page.text)
  
      # get the Course Details

    response = session.get("https://swayam.gov.in/explorer/component.action", params={
   		"component": "course-explorer",
        "t": "XNAS:AAPL",
        "region": "usa",
        "culture": "en-US",
        "cur": "",
        "_": "1444848178406"
    })    
        
     doc = html.fromstring(response.content)
  
    upcoming = doc.xpath('//div[@id=\"Upcoming (Enrollment Open)\"]')
    ongoing = doc.xpath('//div[@id=\"Ongoing (Enrollment Closed)\"]') 

    title = upcoming.xpath('.//div[@class="course-name"]/text()')

    professor = upcoming.xpath('.//div[@class="professor"]/text()')

    layout = [tag.text_content() for tag in upcoming.xpath('.//div[@class="schedule"]')]
	layout = [tag.split(', ') for tag in tags]


	description = upcoming.xpath('.//div[@class="description"]')

	output = []

	for info in zip(title,professor, layout, description):
    	resp = {}
    	resp['title'] = info[0]
    	resp['professor'] = info[1]
    	resp['layout'] = info[2]
    	resp['description'] = info[3]
    	output.append(resp)


    y = json.dumps(resp.title.text)
	with open('JSONFile.txt', 'wt') as outfile:
   		json.dump(y, outfile)