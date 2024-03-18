from flask import Flask, render_template, request
from os.path import join, dirname, realpath
import json
import sqlite3

app = Flask(__name__)
app.config['DATA_DIR'] = join(dirname(realpath(__file__)),'static')


@app.route("/")
def index():
    with open(join(app.config['DATA_DIR'],"data.json"), "r") as data:
        donnees = json.load(data)
        classes = donnees["eleve"]["classe"]
        option_art = donnees["eleve"]["option_art"]
        genre = donnees["eleve"]["genre"]
        boucle_oreille = donnees["accessoire"]["reg"]["boucle_or"]
        accessoire = donnees["accessoire"]["reg"]["autre_accessoire"]
        maquillage = donnees["accessoire"]["maquillage"]
        nb_vetement = donnees["vetement"]["combien_vet"]
        type_vetement = donnees["vetement"]["type"]
        nb_coul = donnees["vetement"]["combien_coul"]
        critere_choix = donnees["vetement"]["crit_choix_vet"]
        type_chaussure = donnees["chaussure"]["type"]
        style= donnees["style_vest"]["type"]
    return render_template('index.html',classes=classes, option_art=option_art, genre=genre, boucle_oreille=boucle_oreille, accessoire=accessoire, maquillage=maquillage, nb_vetement=nb_vetement, type_vetement=type_vetement, nb_coul=nb_coul, critere_choix=critere_choix, type_chaussure=type_chaussure, style=style)

@app.route("/traitement", methods = ['POST'])
def traitement():
    don = request.form
    res = {}
    res["classe"] = don.get('classe')
    res["opt"] = don.get('option_art')
    res["genre"] = don.get('genre')
    res["boucle_oreille"]=don.get('boucle_oreille') 
    res["maquillage"]=don.get('maquillage')
    res["accessoire"]=don.getlist('accessoire')
    res["nb_vetement"]=don.get('nb_vetement')
    res["type_vetement"] = don.getlist('type_vetement')
    res["nb_coul"] = don.get('nb_coul')
    res["critere_choix"] = don.getlist('critere_choix')
    res["type_chaussure"] = don.getlist('chaussure')
    res["style"]=don.getlist('style')
    
    con = sqlite3.connect(join(app.config['DATA_DIR'],"gv.db"))
    cur = con.cursor()
    id_lv = int(cur.execute("""SELECT COUNT (*) FROM questionnaire;""").fetchone()[0]) + 1
    cur.execute(
        """INSERT INTO questionnaire VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(
            id_lv,
            res["classe"],
            res["opt"],
            res["genre"],
            res["boucle_oreille"], 
            res["maquillage"],
            res["nb_vetement"],
            res["nb_coul"]
            )    
        )
    id_rec = int(cur.execute("""SELECT COUNT (*) FROM accessoire;""").fetchone()[0]) + 1
    for a in res["accessoire"]:
        cur.execute(
        """INSERT INTO accessoire VALUES (?, ?, ?)""",(id_rec, id_lv, a)    
        )
        id_rec += 1
        
    id_rec = int(cur.execute("""SELECT COUNT (*) FROM type_vetement;""").fetchone()[0]) + 1
    for t in res["type_vetement"]:
        cur.execute(
        """INSERT INTO type_vetement VALUES (?, ?, ?)""",(id_rec, id_lv, t)    
        )
        id_rec += 1
    
    id_rec = int(cur.execute("""SELECT COUNT (*) FROM critere_choix;""").fetchone()[0]) + 1
    for c in res["critere_choix"]:
        cur.execute(
        """INSERT INTO critere_choix VALUES (?, ?, ?)""",(id_rec, id_lv, c)    
        )
        id_rec += 1
    
    id_rec = int(cur.execute("""SELECT COUNT (*) FROM type_chaussure;""").fetchone()[0]) + 1
    for c in res["type_chaussure"]:
        cur.execute(
        """INSERT INTO type_chaussure VALUES (?, ?, ?)""",(id_rec, id_lv, c)    
        )
        id_rec += 1
    
    id_rec = int(cur.execute("""SELECT COUNT (*) FROM style;""").fetchone()[0]) + 1
    for c in res["style"]:
        cur.execute(
        """INSERT INTO style VALUES (?, ?, ?)""",(id_rec, id_lv, c)    
        )
        id_rec += 1
    
    con.commit()
    con.close()
    """
    res["boucle_oreille"] = don.get('boucle_oreille')
    res["accessoire"] = don.getlist('accessoire')
    res["maquillage"] = don.get('maquillage')
    res["nb_vetements"] = don.get('nb_vetements')
    res["style"] = don.getlist('style')
    """
    return render_template('traitement.html', res=res)

app.run(host="127.0.0.1", port=5000, debug=True)