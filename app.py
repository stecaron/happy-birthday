from flask import Flask
import os
import socket

app = Flask(__name__)
@app.route("/")

def hello():
    html = "<h3>Bonne fete JT!!</h3> Voici une petite et tres modeste carte d'anniversaire de la part de quelques gailles de .Layer <br/> <b>Steph Caron</b> <br/> Joyeux 35e anniversaire mon JT. Si t'etais nee 2 jours plus tot, t'aurais la meme date de fete que le covid quebecois. Sur une note plus serieuse et moins covideuse, si j'avais a choisir la plus belle chose que .Layer m'a apporte, c'est d'avoir eu la chance de rencontrer et de devenir amis avec des gens comme toi! Je m'ennuie de passer du temps avec vous tous. J'espere que tout va bien de ton cote. On se revoit bientot j'espere ... <br/> <b>Sam Perochkin</b> <br/> Bla bla bla"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
