import csv
teams = []
with open ("5laliga_raw.csv","r") as file :
    reader = csv.DictReader(file)

    for row in reader : 
        row["Points"] = int(row["Points"])
        teams.append(row)

sorted_team = sorted(teams,key=lambda x : (x["Points"],
                                           x["Goals_For"])
                     ,reverse=True)

for team in sorted_team :
    print(team["Team"],team["Points"])