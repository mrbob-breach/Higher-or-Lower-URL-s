from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
            )


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return ('<h1 style="color: blue">Your guess was too high!</h1>'
                '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3FlZHFrZGpqb3g5ZzA5MG0xd2Q3ZjI1bXlxYjV5NG12OTlsM3dsNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zu8DrkFiuz8JO/giphy.gif">'
                )
    elif guess < random_number:
        return ('<h1 style="color: green">Your guess was too low!</h1>'
                '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGhzcXZrNHZ5bWIzdXQ1OGs2dHYwdmJoZ2ltcW13aDBuaXFxenV1MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12G1D7rPEV5Cfu/giphy.gif">'
                )
    elif guess == random_number:
        return ('<h1 style="color: purple">Your guess was correct!</h1>'
                '<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2V6ZzhkZmU4cjJxY2R4N2k1Y2dud3djN2s3NmZnZXlmemc4MmxqZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FPNiGHMGcsl6o/giphy.gif">'
                )


if __name__ == "__main__":
    app.run(debug=True)
