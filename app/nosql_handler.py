from pymongo import MongoClient
import os
from bson.json_util import dumps, loads

def handle_nosql_query(query_code):
    try:
        client = MongoClient(os.getenv("MONGO_URI"))
        db = client[os.getenv("MONGO_DB")]

        local_env = {"db": db, "dumps": dumps}

       
        if query_code.startswith('"') and query_code.endswith('"'):
            query_code = query_code[1:-1]

        if "find" in query_code or "aggregate" in query_code or "list" in query_code:
            exec(f"result = list({query_code})", local_env)
            result = local_env.get("result", [])
            result = loads(dumps(result))
        else:
            exec(query_code, local_env)
            result = "Query Generated and executed successfully"

        return result

    except Exception as e:
        return {"error": str(e)}
