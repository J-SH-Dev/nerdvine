import userFunctions as uF
from flask import Flask

app = Flask(__name__)

@app.route("/api/helloWorld")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    users_name = uF.get_users_name()
    current_full_date, current_time, current_date = uF.get_current_time()
    uF.greet_users (users_name=users_name,current_time=current_time,current_date=current_date)