import sports

sport_input = input.capitalize("Please enter the name of the sport you are looking for: ")
team_input = input.capitalize("Please enter the name of the team you are looking for: ")

while sport_input == "Football":
    match = sports.home_score(sports.Football, team_input)