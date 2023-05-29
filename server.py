import json
from sys import stderr
import datetime

from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return comp_validator(listOfCompetitions)


def comp_validator(l_of_comp):
    return [date_checker(comp) for comp in l_of_comp]


def date_checker(competition):
    competition['is_passed'] = datetime.datetime.strptime(competition['date'],
                                                          '%Y-%m-%d %H:%M:%S') < datetime.datetime.now()
    return competition


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


def club_by_email_getter(mail):
    for club in clubs:
        if club['email'] == mail:
            return club
    return None


def getter(iterable, champs, valeur):
    for c in iterable:
        if c[str(champs)] == valeur:
            return c
    return None


@app.route('/')
def index():
    return render_template('index.html', clubs=clubs)


@app.route('/showSummary', methods=['POST'])
def showSummary():
    club = club_by_email_getter(request.form['email'])
    if club:
        return render_template('welcome.html', club=club, clubs=clubs, competitions=competitions)
    flash('sorry, mail not found.')
    return render_template('index.html',clubs=clubs)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = getter(clubs, 'name', club)
    foundCompetition = getter(competitions, 'name', competition)
    # foundClub = [c for c in clubs if c['name'] == club ][0] # turn in infinite loop
    # foundCompetition = [c for c in competitions if c['name'] == competition][0] # turn in infinite loop 
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong please try again")
        return render_template('welcome.html', club=club, clubs=clubs, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    #   TODO : insure no booking in past competition
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    if competition['is_passed']:
        flash('error past competition booking')
        return render_template('welcome.html',clubs= clubs,competitions= competitions,club=club)
    if int(request.form['places']) <= int(club['points']):
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - int(request.form['places'])
        club['points'] = str(int(club['points']) - int(request.form['places']))
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions, clubs=clubs)
    else:
        flash('error too many place booked')
        return render_template('welcome.html', club=club, competitions=competitions, clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
