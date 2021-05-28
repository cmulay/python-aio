# decoration
print('Amoung Us Logic')

get_imposters = int(input('What is the imposter count? (1-3 possible)\n'))
get_players = int(input('What is the player count? (1-10 possible)\n'))


def prob_imposter(get_imposters, get_players):
    return 100 * (get_imposters / get_players)


are_you_an_imposter = (str(round(prob_imposter(get_imposters, get_players), 2)) + "%")
print(f'\nThe chance of becoming an imposter are {are_you_an_imposter}.\n')
