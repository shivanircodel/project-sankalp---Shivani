from flask import Blueprint

auth = Blueprint('views', __name__)

@auth.route('/About-Yourself')
def About_Yourself():
    return "<p>About Yourself</p>"

@auth.route('/Previous-Work-Experience')
def Previous_Work_Experience():
    return "<p>Previous Work Experience</p>"

@auth.route('/Hobbies')
def Hobbies():
    return "<p>Hobbies</p>"

@auth.route('/current/previous-education')
def current/previous-education():
    return "<p>Current/Previous Education</p>"

@auth.route('/Map')
def Map():
    return "<p>Map</p>"
