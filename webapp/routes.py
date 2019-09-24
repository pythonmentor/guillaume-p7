import os
import flask

from robot.getting_loc import ResearchLoc
from robot.gen_answers import WIKI_ERROR

app = flask.Flask(__name__)

@app.route("/")
def index():
    """displays website, gives front key, from environnement variable file"""
    return flask.render_template("site.html",FRONT_KEY=os.environ.get('FRONT_KEY'))

@app.route("/ajax", methods = ["POST"])
def ajax():
    """takes str from javascript, instanciates ResearchLoc class and returns
    dictionnary to js"""
    try :
        get_info = flask.request.form["get_info"]
        parsing = ResearchLoc(get_info)
        dico = parsing.return_answer()
        return flask.jsonify(dico)

    except:
        # if wiki or googlemaps are not working
        return flask.jsonify(WIKI_ERROR)

if __name__ == '__main__':
    app.run()
