import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS
from query import QueryDataFrame


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


QDF = {"ntust": QueryDataFrame(pd.read_csv("ntust/student.csv"))}


@app.route("/api/<string:school>/student", strict_slashes=False)
def student(school: str, **kwargs):
    school_qdf = QDF[school]
    if kwargs:
        kwargs = {k: v.strip() for k, v in kwargs.items()}
        school_qdf = QDF[school].search(**kwargs)
    return jsonify(school_qdf.to_query_list().random())


@app.route(
    "/api/<string:school>/student/<string:id>/<string:name>",
    strict_slashes=False,
)
def auth_student(school: str, *args, **kwargs):
    # TODO: verify request to ensure the user is logged
    pass


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=False)
