# from call_model import pre_odds,pre_results
# from dataset.stats_gen import team_stats
# import pandas as pd,numpy as nps

# def awayWin():
#     a = list(pre_odds)
#     new_list =list()
#     for x in a[0]:
#         new_list.append(x)
#     # print(new_list)
#     a = [round(new_list[0],3),new_list[2]]
#     print(a)
#     # print(a[0])

# awayWin()

# df = pd.read_csv('./dataset/col.csv')

# cols = ['HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR']
# val = team_stats
# # print(type(cols))
# # print((val[2]))

# # ok = np.array(val)

# d = {cols[0] : [val[0]],cols[1] : [val[1]],cols[2] : [val[2]],cols[3] : [val[3]],
#     cols[4] : [val[4]],cols[5] : [val[5]],cols[6] : [val[6]],cols[7] : [val[7]],
#     cols[8] : [val[8]],cols[9] : [val[9]],cols[10] : [val[10]],cols[11] : [val[11]],}
# test_df = pd.DataFrame(data=d)
# print(df)

import  call_model
import dataset.stats_gen

# team_stats = dataset.stats_gen.stats('Liverpool','Brighton')
# a = call_model.pre_function(team_stats)
# print(a)

def form_data():
       home_team_name = 'Liverpool'
       away_team_name = 'Chelsea'
       team_stats = dataset.stats_gen.stats(home_team_name,away_team_name)
       return team_stats,home_team_name,away_team_name

a = form_data()      

def pre_disp():
   b,x,y = form_data()
   pre_odds = call_model.pre_function(b)
   a = list(pre_odds)
   # print(a)
   print(b)
   print(x)
   print(y)
   return a 
a = pre_disp()
