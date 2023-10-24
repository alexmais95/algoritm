states_needed = set(['kievska', 'dneprovska', 'lvivska', 'poltavska', 'odeska', 'nikolaevskaya'])

station = {}
station['mix_fm'] = set(['kievska', 'dneprovska', 'lvivska'])
station['lux'] = set(['lvivska', 'poltavska', 'odeska'])
station['kiss'] = set(['odeska', 'nikolaevskaya', 'kievska'])
station['energy'] = set(['dneprovska', 'lvivska', 'poltavska'])

#конечный результат
finall_state = set()

#пока множество областей не станет пустым
while states_needed:

    best_st = None
    station_covered = set()
    #state: {'kievska', 'dneprovska', 'lvivska'} | statin {'mix_fm'}
    for statin, state in station.items():
        #cowered: {'kievska', 'dneprovska', 'lvivska'}
        cowered = states_needed & state
        # 3 > 0
        if len(cowered) > len(station_covered):
            # best_st = 'mix_fm
            best_st = statin
            #station_covered = {'kievska', 'dneprovska', 'lvivska'}
            station_covered = cowered
    states_needed -= station_covered
    finall_state.add(best_st)

