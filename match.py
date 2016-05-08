
class Match:
	def __init__(self, division, date, match_number, time, hometeam, awayteam, hometeam_goals, awayteam_goals, location):
		self.division = division
		self.date = date
		self.match_number = match_number
		self.time = time
		self.hometeam = hometeam
		self.awayteam = awayteam
		self.hometeam_goals = hometeam_goals
		self.awayteam_goals = awayteam_goals
		self.location = location
	
	def print_match(self):
		print(self.division, self.date, self.match_number, self.time, self.hometeam, 
			self.awayteam, self.hometeam_goals, self.awayteam_goals, self.location)
