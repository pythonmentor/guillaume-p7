import flask

from robot.getting_loc import ResearchLoc
from robot.gen_answers import wiki_error

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("site.html")

@app.route("/ajax", methods = ["POST"])
def ajax():
    try :
        get_info = flask.request.form["get_info"]
        parsing = ResearchLoc(get_info)
        dico = parsing.return_answer()
        print(dico)
        return flask.jsonify(dico)
    
    except:
        # if wiki or googlemaps are not working
        return flask.jsonify(wiki_error)

if __name__ == '__main__':
    app.run(debug = True)