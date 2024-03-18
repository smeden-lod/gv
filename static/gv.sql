CREATE TABLE IF NOT EXISTS questionnaire(
    id_eleve INTEGER PRIMARY KEY,
    classe TEXT NOT NULL,
    option_art TEXT NOT NULL,
    genre TEXT NOT NULL,
    boucle_oreille TEXT NOT NULL,
    maquillage TEXT NOT NULL,
    nb_vet INTEGER,
    nb_couleurs INTEGER);
    --critere_choix_vet TEXT NOT NULL
    --type_chaussure TEXT NOT NULL,
    --style_vest TEXT NOT NULL
    --);

CREATE TABLE IF NOT EXISTS accessoire(
id_record INTEGER PRIMARY KEY,
id_eleve INTEGER NOT NULL,
nom_accessoire TEXT NOT NULL,
FOREIGN KEY (id_eleve)
    REFERENCES questionnaire (id_eleve)
);

CREATE TABLE IF NOT EXISTS type_vetement(
id_record INTEGER PRIMARY KEY,
id_eleve INTEGER NOT NULL,
nom_type_vetement TEXT NOT NULL,
FOREIGN KEY (id_eleve)
    REFERENCES questionnaire (id_eleve)
);


CREATE TABLE IF NOT EXISTS critere_choix(
id_record INTEGER PRIMARY KEY,
id_eleve INTEGER NOT NULL,
nom_critere_choix TEXT NOT NULL,
FOREIGN KEY (id_eleve)
    REFERENCES questionnaire (id_eleve)
);

CREATE TABLE IF NOT EXISTS type_chaussure(
id_record INTEGER PRIMARY KEY,
id_eleve INTEGER NOT NULL,
nom_type_chaussure TEXT NOT NULL,
FOREIGN KEY (id_eleve)
    REFERENCES questionnaire (id_eleve)
);

CREATE TABLE IF NOT EXISTS style(
id_record INTEGER PRIMARY KEY,
id_eleve INTEGER NOT NULL,
nom_style TEXT NOT NULL,
FOREIGN KEY (id_eleve)
    REFERENCES questionnaire (id_eleve)
);