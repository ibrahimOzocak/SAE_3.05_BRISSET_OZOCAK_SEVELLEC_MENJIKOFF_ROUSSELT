from flask import redirect, render_template, request, url_for
from .app import app
import datetime

ARTISTES = [{"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}]
CONCERTS = [{"artiste": "Lucie", "date_debut": datetime.datetime.strptime("2023-10-26", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("10:00", "%H:%M").time(), "salle": "Bercy", "url": "test.png", "nom": "yaaa", "heure_duree":2, "minute_duree":25, "jour":4}, {"artiste": "Mira", "date_debut": datetime.datetime.strptime("2023-10-24", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("8:30", "%H:%M").time(), "salle": "Bercy", "url": "test.png", "nom": "test", "heure_duree":3, "minute_duree":00, "jour":1}, {"artiste": "Muse", "date_debut": datetime.datetime.strptime("2023-10-29", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("10:00", "%H:%M").time(), "salle": "Bercy", "url": "test.png", "nom": "concert 1", "heure_duree":1, "minute_duree":35, "jour":6}, {"artiste": "Daft Punk", "date_debut": datetime.datetime.strptime("2023-10-23", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("14:20", "%H:%M").time(), "salle": "Stade de France", "url": "test.png", "nom": "concert 2", "heure_duree":4, "minute_duree":00, "jour":1}, {"artiste": "Beyoncé", "date_debut": datetime.datetime.strptime("2023-10-24", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("11:00", "%H:%M").time(), "salle": "Madison Square Garden", "url": "test.png", "nom": "concert 3", "heure_duree":1, "minute_duree":30, "jour":4}, {"artiste": "The Beatles", "date_debut": datetime.datetime.strptime("2019-04-10", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("12:30", "%H:%M").time(), "salle": "Royal Albert Hall", "url": "test.png", "nom": "concert 4", "heure_duree":00, "minute_duree":45, "jour":1}, {"artiste": "Ed Sheeran", "date_debut": datetime.datetime.strptime("2019-05-05", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("9:00", "%H:%M").time(), "salle": "Wembley Stadium", "url": "test.png", "nom": "concert 5", "heure_duree":3, "minute_duree":30, "jour":3}, {"artiste": "Adele", "date_debut": datetime.datetime.strptime("2019-06-12", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("22:00", "%H:%M").time(), "salle": "The O2 Arena", "url": "test.png", "nom": "concert 6", "heure_duree":1, "minute_duree":25, "jour":7}, {"artiste": "Michael Jackson", "date_debut": datetime.datetime.strptime("2023-10-18", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("8:45", "%H:%M").time(), "salle": "Tokyo Dome", "url": "test.png", "nom": "concert 7", "heure_duree":2, "minute_duree":00, "jour":1}, {"artiste": "Taylor Swift", "date_debut": datetime.datetime.strptime("2019-08-25", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("15:30", "%H:%M").time(), "salle": "Arrowhead Stadium", "url": "test.png", "nom": "concert 8", "heure_duree":2, "minute_duree":25, "jour":3}, {"artiste": "Coldplay", "date_debut": datetime.datetime.strptime("2019-09-14", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("11:11", "%H:%M").time(), "salle": "Estadio Wanda Metropolitano", "url": "test.png", "nom": "concert 9", "heure_duree":5, "minute_duree":00, "jour":5}, {"artiste": "Kanye West", "date_debut": datetime.datetime.strptime("2023-10-23", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("13:30", "%H:%M").time(), "salle": "American Airlines Center", "url": "test.png", "nom": "concert 10", "heure_duree":1, "minute_duree":30, "jour":2}]
SALLES = [{"nom": "Bercy", "nbPlaces": 130, "photo":"test.png"}, {"nom": "Stade de France", "nbPlaces": 80000, "photo":"test.png"}, {"nom": "Madison Square Garden", "nbPlaces": 20000, "photo":"test.png"}, {"nom": "Royal Albert Hall", "nbPlaces": 5000, "photo":"test.png"}, {"nom": "Wembley Stadium", "nbPlaces": 90000, "photo":"test.png"}, {"nom": "The O2 Arena", "nbPlaces": 20000, "photo":"test.png"}, {"nom": "Tokyo Dome", "nbPlaces": 55000, "photo":"test.png"}, {"nom": "Arrowhead Stadium", "nbPlaces": 80000, "photo":"test.png"}, {"nom": "Estadio Wanda Metropolitano", "nbPlaces": 68000, "photo":"test.png"}, {"nom": "American Airlines Center", "nbPlaces": 21000, "photo":"test.png"}]
LOGEMENTS = [{"nom_etablissement":"yaaaa", "adresse_ville_codepostal":"rue du yaaa", "nb_etoile": 3}]

HEURES1 = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
PAS1 = 1
HEURES2 = [8, 10, 12, 14, 16, 18, 20, 22]
PAS2 = 2
JOUR_VOULU = datetime.datetime.now() # -datetime.timedelta(days=7) ou +datetime.timedelta(days=7) --> pour changer de semaine (- ou + 1 semaine)

@app.route('/')
def accueil():
    heures = HEURES2
    pas = PAS2
    jour = JOUR_VOULU
    agenda = concerts_agenda(heures, pas)
    lundi = jour + datetime.timedelta(days=-(jour.weekday()+1)) + datetime.timedelta(days=1)
    dimanche = jour + datetime.timedelta(days=7-(jour.weekday()+1))
    return render_template(
        "accueil.html",
        concerts=get_prochains_concerts(),
        agenda=agenda,
        heures=heures,
        date_lundi=lundi.strftime("%d/%m/%Y"),
        date_dimanche=dimanche.strftime("%d/%m/%Y")
    )

# concert
@app.route('/creer_concert')
def creer_concert():
    return render_template(
        "creer_concert.html",
        artistes=ARTISTES,
        salles=SALLES
    )

@app.route('/voir_prochains_concerts')
def voir_prochains_concerts():
    return render_template(
        "voir_prochains_concerts.html",
        concerts=get_prochains_concerts()
    )

@app.route('/historique_concert')
def historique_concerts():
    return render_template(
        "historique_concerts.html",
        concerts = get_historique_concerts()
    )

@app.route('/save_concert', methods=("POST",))
def save_concert():
    concert = {}
    concert["artiste"] = request.form['artiste']
    concert["date_debut"] = datetime.datetime.strptime(request.form['date_debut'], "%Y-%m-%d")
    concert["salle"] = request.form['salle']
    concert["nom"] = request.form['titre']
    concert["heure_debut"] = datetime.datetime.strptime(request.form['heure_debut'], "%H:%M").time()
    concert["heure_duree"] = int(request.form['heure_duree'])
    concert["minute_duree"] = int(request.form['minute_duree'])
    concert["jour"] = 7
    CONCERTS.append(concert)
    return redirect(url_for('concert', nom=concert["nom"]))

@app.route('/concert/<nom>')
def concert(nom):
    concert = get_concert(nom)
    return render_template(
        "concert.html",
        concert=concert
    )

# salle
@app.route('/ajout_nouvelle_salle')
def ajout_nouvelle_salle():
    return render_template(
        "ajout_nouvelle_salle.html"
    )

@app.route('/voir_salles')
def voir_salles():
    return render_template(
        "voir_salles.html",
        salles = SALLES
    )

@app.route('/salle/<nom>')
def salle(nom):
    salle = get_salle(nom)
    return render_template(
        "salle.html",
        salle=salle
    )

# artiste
@app.route('/ajout_artiste')
def ajout_artiste():
    return render_template(
        "ajout_artiste.html"
    )

@app.route('/voir_artistes')
def voir_artistes():
    return render_template(
        "voir_artistes.html",
        artistes = ARTISTES
    )

@app.route('/artiste/<nom>')
def artiste(nom):
    artiste = get_artiste(nom)
    return render_template(
        "artiste.html",
        artiste=artiste
    )

@app.route('/save_artiste', methods=("POST",))
def save_artiste():
    artiste = {}
    artiste["nom_artiste"] = request.form['nom']
    artiste["prenom_artiste"] = request.form['prenom']
    artiste["mail"] = request.form['mail']
    artiste["telephone"] = request.form['telephone']
    artiste["date_de_naissance"] = request.form['date_naissance']
    artiste["lieu_de_naissance"] = request.form['lieu_naissance']
    artiste["adresse"] = request.form['adresse']
    artiste["securite_sociale"] = request.form['num_secu_sociale']
    artiste["cni"] = request.form['cni']
    artiste["date_delivrance_cni"] = request.form['date_delivrance']
    artiste["date_expiration_cni"] = request.form['date_expiration']
    artiste["carte_reduction"] = request.form['carte_train']
    ARTISTES.append(artiste)
    return redirect(url_for('artiste', nom=artiste["nom_artiste"]))

# logement
@app.route('/logement/<nom_etablissement>')
def logement(nom_etablissement):
    logement = get_logement(nom_etablissement)
    return render_template(
        "logement.html",
        logement=logement
    )

@app.route('/ajout_logement')
def ajout_logement():
    return render_template(
        "ajout_logement.html"
    )

@app.route('/voir_logements')
def voir_logements():
    return render_template(
        "voir_logements.html",
        logements = LOGEMENTS
    )

@app.route('/save_logement', methods=("POST",))
def save_logement():
    logement = {}
    logement["nom_etablissement"] = request.form['Entrer_nometablissement']
    logement["adresse_ville_codepostal"] = request.form['Entrer_adresse']
    logement["nb_etoile"] = request.form['Entrer_nbetoiles']
    LOGEMENTS.append(logement)
    return redirect(url_for('logement', nom_etablissement=logement["nom_etablissement"]))

# fonctions utiles pour les templates
def get_concert(nom):
    for c in CONCERTS:
        if c["nom"] == nom:
            return c
    return None

def get_salle(nom):
    for s in SALLES:
        if s["nom"] == nom:
            return s
    return None

def get_logement(nom_etablissement):
    for e in LOGEMENTS:
        if e["nom_etablissement"] == nom_etablissement:
            return e
    return None

def get_artiste(nom):
    for a in ARTISTES:
        if a["nom_artiste"] == nom:
            return a
    return None

def get_prochains_concerts():
    prochains_concerts = []
    now = datetime.datetime.now()
    for c in CONCERTS:
        if datetime.datetime.combine(c["date_debut"],c["heure_debut"]) > now:
            prochains_concerts.append(c)
    prochains_concerts = sorted(prochains_concerts, key=lambda concert: datetime.datetime.combine(concert["date_debut"],concert["heure_debut"]))
    return prochains_concerts

def get_historique_concerts():
    prochains_concerts = []
    now = datetime.datetime.now()
    for c in CONCERTS:
        if datetime.datetime.combine(c["date_debut"],c["heure_debut"]) < now:
            prochains_concerts.append(c)
    return prochains_concerts

def concerts_agenda(heures=HEURES1,pas=PAS1,jour_voulu=JOUR_VOULU):
    #initialisation de l'agenda
    agenda = {}
    for i in range(1,8):
        agenda[i] = {}
        for heure in heures:
            agenda[i][heure] = []
    #remplissage de l'agenda
    for concert in CONCERTS:
        jour = jour_voulu
        if datetime.timedelta(days=-(jour.weekday()+1))<concert["date_debut"]-jour<datetime.timedelta(days=7-(jour.weekday()+1)):
            for h in heures:
                fin_horaire = h+pas
                # format 24h obligatoire
                if fin_horaire > 23:
                    fin_horaire = datetime.time(hour=h+pas-1, minute=59)
                else:
                    fin_horaire = datetime.time(hour=h+pas)
                debut_horaire = datetime.time(hour=h)
                minutesC = (concert["heure_debut"].minute+concert["minute_duree"])%60
                heuresC = concert["heure_debut"].hour+concert["heure_duree"]+(concert["heure_debut"].minute+concert["minute_duree"])//60
                fin_concert = datetime.time(hour=heuresC, minute=minutesC)
                debut_concert = concert["heure_debut"]
                # ajouter le concert si il est dans l'intervalle horaire
                if not(debut_concert >= fin_horaire or fin_concert <= debut_horaire):
                    agenda[concert["date_debut"].weekday()+1][h].append(concert["nom"])
    return agenda
