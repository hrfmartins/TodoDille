import uvicorn
from fastapi import FastAPI
from pysondb import db
from routers import lists_router, tasks_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(lists_router.router)
app.include_router(tasks_router.router)

database = db.getDb("./database.json")

#
# @app.route("/complete", methods=["POST"])
# def complete_task():
#     incoming_data = request.get_json()
#     id = incoming_data["id"]
#     task = database.getByQuery({"id": id})[0]
#
#     database.updateByQuery({"id": id},
#                            {"completed": not task["completed"]})
#
#     is_successful = True
#     return jsonify({"update": is_successful})
#
#
# @app.route("/update", methods=["GET", "POST"])
# def update_task():
#     is_successful = False
#     if request.method == "POST":
#         incoming_data = request.get_json()
#         id_to_update = incoming_data["id"]
#         new_title = incoming_data["title"]
#         new_desc = incoming_data["desc"]
#         is_completed = incoming_data["completed"]
#         database.updateByQuery({"id": id_to_update},
#                                {"title": new_title,
#                                 "desc": new_desc,
#                                 "completed": is_completed}
#                                )
#         is_successful = True
#     return jsonify({"update": is_successful})


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
