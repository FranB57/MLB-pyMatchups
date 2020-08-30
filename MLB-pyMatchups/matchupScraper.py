import requests, json, re
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
from player_lookup import pitcher_vs_batter, pitcher_lookup, batter_lookup

URL = 'https://baseballsavant.mlb.com/daily_matchups'

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
data = re.findall("var matchups_data =(.+?);\n", page.content.decode("utf-8"), re.S) #parse website and and find the matchup data
pd.set_option('display.max_rows',None)

if data: 
    ls = json.loads(data[0])   #load data into a list dict



def stat_sort(list,sort,category="abs"): 
    datad = []
    colmn = ("{}")
    colmn = colmn.format(category)
    for i in list:
        try: x = float(i[colmn]) #assign the value of x to a float to deal with batting average and similar stats and deal with TypeError when the value is none  
        except TypeError: pass 
        if x >= sort:     
            datad.append(i) 
            
    return datad


def get_historical_matchup(index):  #get historical Pitcher vs Batter Matchup when specifying the index printed from the df dataFrame
    p_id= df.at[index,"pitcher_id"]
    b_id= df.at[index,"player_id"]

    print("\n\n",df.at[index,"pitcher"], "VS",df.at[4,"player_name"], "  Career Stats (Only Events): \n")
    pitcher_vs_batter(b_id,p_id)



def player_historical(p_type,index):
    if p_type == "P":
        p_id= df.at[index,"pitcher_id"]
        pitcher_lookup(p_id)
    if p_type =="B": 
        b_id= df.at[index,"player_id"]
        batter_lookup(b_id)

df = pd.DataFrame(stat_sort(ls,10,"abs"), columns=['player_name','player_id',"pitcher","pitcher_id","abs","pa","hits","ba","slg","woba","xwoba","xslg"])  #set dataframe and specify the columns you want displayed. To customize the columns just add "",
print(df)
player_historical("B",1)
