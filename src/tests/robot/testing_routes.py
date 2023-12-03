from src.app import app
import src.tests.in_memory_db as test_db

@app.route("/db_initialize")
def db_initialize():
    test_db.setup_db()
    return "Database should now be initialized\n"

@app.route("/ping")
def ping():
    return "Pong"
