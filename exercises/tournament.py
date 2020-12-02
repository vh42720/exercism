def tally(rows):
    # initiate parameters to use
    point_dict = {}
    team_dict = {'MP': 0, 'win': 0, 'draw': 0, 'loss': 0, 'P': 0}
    reverse_dict = {'win': 'loss', 'loss': 'win', 'draw': 'draw'}
    header = ["Team                           | MP |  W |  D |  L |  P"]
    table = []
    # There are exactly 31 spaces including team's name
    for row in rows:
        # split into 3 parts
        team_1, team_2, outcome_1 = row.split(';')
        outcome_2 = reverse_dict[outcome_1]
        # adding point to using counter
        for team, outcome in zip([team_1, team_2], [outcome_1, outcome_2]):
            if team not in point_dict:
                point_dict[team] = team_dict.copy()
            point_dict[team][outcome] += 1
            point_dict[team]['MP'] += 1
            point_dict[team]['P'] = point_dict[team]['win'] * 3 + point_dict[team]['draw']

    for team, result in point_dict.items():
        return_string = f"{team.ljust(31)}" \
              f"|  {result['MP']} " \
              f"|  {result['win']} " \
              f"|  {result['draw']} " \
              f"|  {result['loss']} " \
              f"|  {result['P']}"
        table.append(return_string)

    # double sort the table using negative (ascending)
    table.sort(key=lambda x: (-int(x[-2:]), x[:2]))
    return header + table


print(tally(["Allegoric Alaskans;Blithering Badgers;win",
             "Devastating Donkeys;Courageous Californians;draw",
             "Devastating Donkeys;Allegoric Alaskans;win",
             "Courageous Californians;Blithering Badgers;loss",
             "Blithering Badgers;Devastating Donkeys;loss",
             "Allegoric Alaskans;Courageous Californians;win"]))
