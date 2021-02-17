# coding: utf-8

from flask import Flask
import os
import socket

app = Flask(__name__)
@app.route("/")

def hello():
    html = "<h3>Bonne fête JT!!</h3> Voici une petite et très modeste carte d'anniversaire de la part de quelques gailles de .Layer <br/> <br/> <b>Steph Caron</b> <br/> Joyeux 35e anniversaire mon JT. Si t'étais né 2 jours plus tôt, t'aurais la même date de fête que le covid québécois. Sur une note plus sérieuse et moins covideuse, je dois t'avouer que si j'avais a choisir la plus belle chose que .Layer m'a apporté, c'est d'avoir eu la chance de rencontrer et de devenir amis avec des gens comme toi! Je m'ennuie de passer du temps avec vous tous. J'espère que tout va bien de ton côté dans tous tes projets de vie. On se revoit bientot j'espere ... <br/> <br/> <b>Sam Perochkin</b> <br/> JeeTee, l'inventeur du nom .Layer quoi. On s'est pas trop vu dans la dernière année et ça c'est mauvais signe. J'espère que toi, tes proches et tes main/side projets vont bien et qu'on pourra organiser de quoi real life cet été. Je vais enfiler mon chandail catnip pour l'occasion. (En fait, je le mets presque toujours haha). Je t'en souhaite une bonne fellow .Layeurien!"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
