from flask import Blueprint, redirect, render_template, request
from bson.json_util import dumps, loads
from .llm_processor import parse_nl_query
from .sql_handler import handle_sql_query
from .nosql_handler import handle_nosql_query
from flask import session
import json
main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        nl_query = request.form["query"]
        db_type = request.form["db_type"]
        parsed_query = parse_nl_query(nl_query, db_type)
        print(parsed_query)

        if db_type == "mysql":
            result = handle_sql_query(parsed_query)
        else:
            result = handle_nosql_query(parsed_query)
        
        if not isinstance(result, str):
            result = json.loads(json.dumps(result, default=str))

        session["history"].append({"role": "user", "text": nl_query})
        session["history"].append({"role": "bot", "text": result})
        session.modified = True


        return render_template(
            "index.html",
            query=nl_query,
            result=result,
            is_table=isinstance(result, list),
            history=session.get("history", [])
        )

    
    return render_template("index.html", history=session.get("history", []))


@main.route("/clear", methods=["POST"])
def clear():
    session.pop("history", None)
    return redirect("/")

