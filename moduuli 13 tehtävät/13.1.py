from flask import Flask
#http://127.0.0.1:3000/alkuluku/

primeapp = Flask(__name__)


@primeapp.route("/alkuluku/<luku>")
def prime(luku):
    num = int(luku)
    if num == 2:
        vastaus = {
            "Number": int(luku), "isPrime": True
        }
        return vastaus
    for n in range(2, num):
        if num % n != 0:
            vastaus = {
                "Number": int(luku), "isPrime": True
            }
        else:
            vastaus = {
                "Number": int(luku), "isPrime": False
            }
            return vastaus
    return vastaus


if __name__ == "__main__":
    primeapp.run(use_reloader=True, host="127.0.0.1", port=3000)
