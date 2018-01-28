import sqlite3 
import sys

try:
	con = sqlite3.connect('burnspark_league.db')

	cur = con.cursor()

	cur.executescript("""
		CREATE TABLE Matches(Division TEXT, Date TEXT, Match_Number INT, Time TEXT, HomeTeam TEXT, 
		AwayTeam TEXT, HomeGoals INT, AwayGoals INT, Location TEXT, PRIMARY KEY (Division, Date, Match_Number));
		""")

	con.commit()

except sqlite3.Error, e:
		
	if con:
		con.rollback()

	print "Error %s:" % e.args[0]
	sys.exit(1)

finally:
	if con:
		con.close()
		

