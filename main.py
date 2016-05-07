
import bs4, requests

#This section of code finds the url where the data is stored
def get_soccerlink():
	res = requests.get('http://www.arcsa.co/standings/sunday-7-v-7-standings.html')
	res.raise_for_status()
	arcsa_soup = bs4.BeautifulSoup(res.text, 'lxml')
	soccer_url = str(arcsa_soup.find('iframe')['src'])
	return soccer_url

#Here we parse the html displaying the results
def get_resultslinks(soccer_url):
	results_page = requests.get(soccer_url)
	results_page.raise_for_status()
	results_soup = bs4.BeautifulSoup(results_page.text, 'lxml')
	links  = results_soup.find_all('a', {'class':"viewschedule"})
	league_schedule_urls = []
	for link in links:
		league_schedule_urls.append("events.gotsport.com/events/" + link.get('href'))
	return league_schedule_urls

soccer_url = get_soccerlink()
league_schedule_urls = get_resultslinks(soccer_url)
print(league_schedule_urls)

