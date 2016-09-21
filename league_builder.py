import csv

players = []
experienced_players = []
inexperienced_players = []
guardians = []
player_dict = []
dragons = []
sharks = []
raptors = []
raptor_practice = ["March 18", "1pm"]
dragon_practice = ["March 17", "1pm"]
shark_practice = ["March 17", "3pm"]

if __name__ == '__main__':
    with open('soccer_players.csv', 'r') as csvfile:
        fieldnames = ['name', 'height', 'experience', 'guardian']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for line in reader:
            if line['name'] != 'Name':
                player_dict.append(line)
                players.append(line['name'])
                guardians.append(line['guardian'])
                if line['experience'] == 'NO':
                    inexperienced_players.append(line['name'])
                else:
                    experienced_players.append(line['name'])

    exp_players_per_team = len(experienced_players)/3
    for i in range(exp_players_per_team):
        dragons.append(experienced_players[i])
        sharks.append(experienced_players[i + exp_players_per_team])
        raptors.append(experienced_players[i + (exp_players_per_team * 2)])

    inexp_per_team = len(inexperienced_players)/3
    for i in range(inexp_per_team):
        dragons.append(inexperienced_players[i])
        sharks.append(inexperienced_players[i + exp_players_per_team])
        raptors.append(inexperienced_players[i + (exp_players_per_team * 2)])


    def create_file_name(person):
        full_name = person.lower().split()
        first_name = full_name[0]
        last_name = full_name[1]
        return "{}_{}.txt".format(first_name, last_name)


    def find_parents(player_name):
        for person in player_dict:
            if person['name'] == player_name:
                return person['guardian']


    def write_letter(team, first_practice, team_name):
        for player in team:
            letter = create_file_name(player)
            parents = find_parents(player)
            with open(letter, 'w') as l:
                l.write("Dear {},\n\n".format(parents))
                l.write("Your child, {}, has been placed on the {} team this season!\n".format(player, team_name))
                l.write("The first team practice for the {} is on {} at {}. \n\n".format(team_name, first_practice[0], first_practice[1]))
                l.write("See you then!")

    write_letter(raptors, raptor_practice, "Raptors")
    write_letter(dragons, dragon_practice, "Dragons")
    write_letter(sharks, shark_practice, "Sharks")
