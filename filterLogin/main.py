from flask import Flask, request, render_template, redirect
import os
import sqlite3

#экземпляр класса с аргументом ввиде имени
currentLocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


#для отображения менюшки
menu = [{"name": "Главная", "url": "/"},
        {"name": "Авторизация", "url": "login"},
        {"name": "Обратная связь", "url": "contact"},
        {"name": "О сайте", "url": "about"}]


@app.route("/")
def home():
    return render_template(("index.html"))

# обработчик для проверки авторизации
@app.route("/", methods = ["POST"])
def checkLogin():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(currentLocation + "\Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password From Users WHERE Username = {un} AND Password = {pw}".format( un = un, pw = PW )

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
        return render_template("logged.html")
    else:
        return redirect("/register")

#обработчик для страницы регистрации
@app.route("/register", methods = ["GET", "POST"])
def registerPage():
    if request.method == "POST":
        dUN == request.form['DUsername']
        dPW == request.form['Dpassword']
        sqlconnection = sqlite3.Connection(currentLocation + "\Login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES('{u}', '{p}')".format(u = dUN, p = dPW)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("register.html")


#для запуска локалки
if __name__ == "__main__":
    app.run()