CREATE DATABASE dialetti_it;

\c dialetti_it;

CREATE TABLE Regioni (
    codice_nuts2 VARCHAR(5) PRIMARY KEY,
    nome_regione VARCHAR(30) NOT NULL
);

CREATE TABLE Province (
    codice_nuts3 VARCHAR(5) PRIMARY KEY,
    nome_provincia VARCHAR(50) NOT NULL,
    nuts2_regione VARCHAR(5) NOT NULL,
    CONSTRAINT FK_province_regioni FOREIGN KEY (nuts2_regione)
    REFERENCES Regioni(codice_nuts2)
);

CREATE TABLE Comuni (
    id_comune INT PRIMARY KEY,
    nome_comune VARCHAR(100) NOT NULL,
    nuts3_provincia VARCHAR(5) NOT NULL,
    longitudine_comune DOUBLE PRECISION NOT NULL,
    latitudine_comune DOUBLE PRECISION NOT NULL, -- using -1 as unknown value
    CONSTRAINT FK_comuni_province FOREIGN KEY (nuts3_provincia)
    REFERENCES Province(codice_nuts3)
);

CREATE TABLE Frasi (
        id_frase SERIAL PRIMARY KEY,
        testo_frase VARCHAR(1000) NOT NULL
    );


CREATE TABLE Registrazioni (
        id_registrazione SERIAL PRIMARY KEY,
        id_comune INT,
        id_frase INT,
        CONSTRAINT FK_idcomune FOREIGN KEY (id_comune)
        REFERENCES Comuni(id_comune),
        CONSTRAINT FK_idfrase FOREIGN KEY (id_frase)
        REFERENCES Frasi(id_frase)
    );