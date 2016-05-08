
import bs4, requests
from match import Match

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
		league_schedule_urls.append("https://events.gotsport.com/events/" + link.get('href'))
	return league_schedule_urls

#parse individual matches from schedule url
def get_matches(url):
	matches = []
	matches_page = requests.get(url)
	matches_page.raise_for_status()
	matches_soup = bs4.BeautifulSoup(matches_page.text, 'lxml')
	division = matches_soup.find('h3', {'class':"bracket"}).text
	match_tables = matches_soup.find_all('table',{'class':"standings"})
	for match_table in match_tables:
		date = match_table.find('th', {'class':"GroupBoxHeading"}).text
		match = match_table.find_all('tr')[2:]
		for row in match:
			cell = row.find_all('td')
			match_num = cell[0].text
			time = cell[1].text
			hometeam = cell[2].text
			score = cell[3].text
			awayteam = cell[4].text
			location = cell[5].text
			score = score.partition('-')
			hometeam_goals = score[0].strip(' ')
			awayteam_goals = score[2].strip(' ')
			new_match = Match(division, date, match_num, time, hometeam, awayteam, 
				hometeam_goals, awayteam_goals, location)	
			matches.append(new_match)
	return matches

soccer_url = get_soccerlink()
league_schedule_urls = get_resultslinks(soccer_url)
print(league_schedule_urls)
matches = []
for url in league_schedule_urls:
	matches.extend(get_matches(url))
for match in matches:
	match.print_match()
