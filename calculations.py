

def calculatewinper(TotalMatchesPlayed:float,TotalWins:float) -> float:
    '''needs two inputs, the total matches played in a float and total wins in a float 
    in this order (TotalMatchesPlayed,TotalWins)'''

    try:
        return TotalWins/TotalMatchesPlayed * 100
    except ZeroDivisionError:
        print('ERROR: play some more games vro')