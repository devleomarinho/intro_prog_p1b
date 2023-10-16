lista_de_times = ['São Paulo',
                  'Palmeiras',
                  'Botafogo',
                  'Vasco',
                  'Corinthians',
                  'Santos',
                  'Cruzeiro',
                  'Santa Cruz',
                  'Sport',
                  'Botafogo PB']
time_user = input('Qual time você deseja saber se está na lista? ')
for time in lista_de_times:
    if time_user == time:
        print('ACHEI!')
        break
    else:
        print('Não achei!')