from itertools import combinations, permutations


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return list(permutations(friends, team_size))
    else:
        return list(combinations(friends, team_size))
