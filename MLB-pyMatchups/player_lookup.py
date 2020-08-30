import pandas as pd 


pd.set_option('display.max_rows',None)
def batter_lookup(batter_id):
    batter_id= str(batter_id)

    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7C&hfC=&hfSea=2020%7C&hfSit=&player_type=batter&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfInfield=&team=&position=&hfOutfield=&hfRO=&home_road=&batters_lookup%5B%5D={}&hfFlag=&hfPull=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_pas=0&type=details&")
    
    df = pd.read_csv(url.format(batter_id))
    df_pretty = pd.DataFrame(df,columns=['pitch_type','description','zone','bb_type',"events"]) #customize / think about adding more columns to make the printed data more relevant 
                                                                                        #maybe think about adding a direct link to the player graphs / hotzones 
    df_pretty = df_pretty.dropna() #drops all the null values (typically found in the events column) since we only want to see pitches were player got a hit
    print(df_pretty)
  
def pitcher_lookup(pitcher_id):
    pitcher_id= str(pitcher_id)
    
    
    url = ("https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7CPO%7CS%7C=&hfSea=&hfSit=&player_type=pitcher&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&pitchers_lookup%5B%5D={}&team=&position=&hfRO=&home_road=&hfFlag=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_abs=0&type=details&")
    
    df = pd.read_csv(url.format(pitcher_id))
    df_pretty = pd.DataFrame(df,columns=['pitch_name','description','zone',"bb_type","events"]) #same added functionality from batter_lookup 
    df_pretty = df_pretty.dropna()
    print(df_pretty)
 
def pitcher_vs_batter(b_id, p_id):
    p_id= str(p_id)
    b_id= str(b_id)
    url= ("https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7C&hfC=&hfSea=2020%7C2019%7C2018%7C2017%7C2016%7C2015%7C2014%7C2013%7C2012%7C2011%7C2010%7C2009%7C2008%7C&hfSit=&player_type=batter&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfInfield=&team=&position=&hfOutfield=&hfRO=&home_road=&batters_lookup%5B%5D={}&hfFlag=&hfPull=&pitchers_lookup%5B%5D={}&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_pas=0&type=details&")
    #same added functionality for graphing and visualization
    # trout: 545361 kersh: 477132 -> first batter then pitcher 
    df = pd.read_csv(url.format(b_id,p_id))

    df_pretty = pd.DataFrame(df,columns=['pitch_name','description','zone',"events"])

    df_pretty = df_pretty.dropna()
    print(df_pretty)

