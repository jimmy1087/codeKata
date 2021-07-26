# Find players that play both sports in (N + M) execution rather than (N * M)

basketball_players = [
    {"first_name": "Jill", "last_name": "Huang", "team": "Gators"},
    {"first_name": "Janko", "last_name": "Barton", "team": "Sharks"},
    {"first_name": "Wanda", "last_name": "Vakulskas", "team": "Sharks"},
    {"first_name": "Jill", "last_name": "Moloney", "team": "Gators"},
    {"first_name": "Luuk", "last_name": "Watkins", "team": "Gators"},
    ]

football_players = [
{"first_name": "Hanzla", "last_name": "Radosti", "team": "32ers"},
{"first_name": "Tina", "last_name": "Watkins", "team": "Barleycorns"},
{"first_name": "Alex", "last_name": "Patel", "team": "32ers"},
{"first_name": "Jill", "last_name": "Huang", "team": "Barleycorns"},
{"first_name": "Wanda", "last_name": "Vakulskas", "team": "Barleycorns"}
]

# o( N + M) time execution
def mergeLists(teamA, teamB):

    twoTeams = []

    fullNameInBasket = {}
    for player in teamA:
        fullName = player["first_name"] + " " + player["last_name"]
        fullNameInBasket[fullName] = True

    for player in teamB:
        fullName = player["first_name"] + " " + player["last_name"]
        if fullName in fullNameInBasket:
            twoTeams.append(fullName)

    print(twoTeams)


mergeLists(football_players, basketball_players)