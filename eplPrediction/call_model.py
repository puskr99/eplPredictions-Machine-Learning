import pickle , pandas as pd,numpy as np
import dataset.stats_gen 

# open a file, where you stored the pickled data
file = open('epl_prediction_random_forest', 'rb')

data = pickle.load(file)
file.close()

# df = pd.read_csv('dataset/test.csv')
# test_df =  df.drop(['Season','DateTime','FTR','HTR','FTAG','FTHG','HTAG','HTHG','home_team_name','away_team_name'],axis = 1)
# print(test_df)
# print(type(test_df))
# team_stats = dataset.stats_gen.stats('Man City','Liverpool')
def pre_function(team_stats):
    cols = ['HS','AS','HST','AST','HC','AC','HF','AF','HY','AY','HR','AR']
    val = team_stats

    d = {cols[0] : [val[0]],cols[1] : [val[1]],cols[2] : [val[2]],cols[3] : [val[3]],
        cols[4] : [val[4]],cols[5] : [val[5]],cols[6] : [val[6]],cols[7] : [val[7]],
        cols[8] : [val[8]],cols[9] : [val[9]],cols[10] : [val[10]],cols[11] : [val[11]],}
    test_df = pd.DataFrame(data=d)

    # test_df = team_stats
    pre_results = data.predict(test_df)
    # print(type(pre_results))
    # print('Predicted Result',   (pre_results))
    pre_probs  = data.predict_proba(test_df)
    pre_odds = (1 / pre_probs)
    # print(pre_odds)
    return pre_odds

