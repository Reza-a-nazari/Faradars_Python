teams = [
    {
        "Team": "Villarreal",
        "Points": 70,
        "Goals_For": 71,
        "Goals_Against": 45
    },
    {
        "Team": "Barcelona",
        "Points": 92,
        "Goals_For": 92,
        "Goals_Against": 35
    },
    {
        "Team": "Real Madrid",
        "Points": 89,
        "Goals_For": 85,
        "Goals_Against": 30
    },
    {
        "Team": "Atletico Madrid",
        "Points": 79,
        "Goals_For": 70,
        "Goals_Against": 30
    },
    {
        "Team": "Athletic Bilbao",
        "Points": 63,
        "Goals_For": 61,
        "Goals_Against": 44
    },
    {
        "Team": "Real Sociedad",
        "Points": 60,
        "Goals_For": 51,
        "Goals_Against": 39
    },
    {
        "Team": "Sevilla",
        "Points": 60,
        "Goals_For": 54,
        "Goals_Against": 47
    },
    {
        "Team": "Betis",
        "Points": 57,
        "Goals_For": 48,
        "Goals_Against": 45
    },
    {
        "Team": "Osasuna",
        "Points": 51,
        "Goals_For": 45,
        "Goals_Against": 50
    },
    {
        "Team": "Mallorca",
        "Points": 49,
        "Goals_For": 42,
        "Goals_Against": 48
    }
]



data = teams

# print(data[1]["Points"])
print(sorted(data,key=lambda x : x["Points"]))