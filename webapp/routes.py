import flask

from robot.getting_loc import ResearchLoc

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("site.html")


@app.route("/result")
def get_information():
    """this is a variable that
    gets informations from text (site.html)
    a
    nd blablabla (complete later on)"""
    #flask.request['get_info']
#    get_info = requests.get(url = "/result", params="get_info")
    sentence = flask.request.args.get("get_info")

    parsing = ResearchLoc(sentence)
    dico = parsing.return_answer()

    return flask.jsonify(dico)
    #return flask.render_template("site.html")

if __name__ == '__main__':
    app.run(debug = True)