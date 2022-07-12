import numpy as np
import pandas as pd

data=pd.read_csv("F:\players_22.csv")

def cheapReplacement(player, skillReduction = 0):
    
    
    replacee = data[data['short_name'] == player][['short_name','wage_eur','value_eur','player_positions','overall','age']]

    
    replaceePos = replacee['player_positions'].item()
    replaceeWage = replacee['wage_eur'].item()
    replaceeAge = replacee['age'].item()
    replaceeOverall = replacee['overall'].item() - skillReduction
    
    
    longlist = data[data['player_positions'] == replaceePos][['short_name','wage_eur','value_eur','player_positions','overall','age']]
    
    
    
    removals = longlist[longlist['overall'] <= replaceeOverall].index
    longlist.drop(removals , inplace=True)
    
    
    removals = longlist[longlist['wage_eur'] > replaceeWage].index
    longlist.drop(removals , inplace=True)

    
    removals = longlist[longlist['age'] >= replaceeAge].index
    longlist.drop(removals , inplace=True)
    
    
    return longlist.sort_values("overall", ascending=False)
cheapReplacement(input("Enter player name: "))
