#!/usr/bin/python3
from flask import Flask,render_template,request
import  call_model
import dataset.stats_gen


app  = Flask(__name__)

@app.route('/')
def view_homepage():
    return render_template('index.html')

@app.route('/odds', methods =["GET", "POST"])
def pre_disp():
   b,p,q = form_data()
   pre_odds = call_model.pre_function(b)
   a = list(pre_odds)
#    print(a)
   new_list = list()
   for x in a[0]:
        new_list.append(x)
   temp = [round(new_list[0],3),round(new_list[1],3),round(new_list[2],3),p,q]
   return render_template('index.html', odds = temp)

def form_data():
    if request.method == "POST":
        home_team_name = request.form.get("team1")
        # print("Home team name", home_team_name)
        away_team_name = request.form.get("team2")
        # print("Away team name", away_team_name)
        team_stats = dataset.stats_gen.stats(home_team_name,away_team_name)
        return team_stats,home_team_name,away_team_name

if __name__ == "__main__":
    print("Starting Python Flask Server...")
    app.run()