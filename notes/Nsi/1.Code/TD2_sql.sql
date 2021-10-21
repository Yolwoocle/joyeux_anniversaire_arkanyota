--!/usr/bin/env python
-- vim: set sw=4 sts=4 et fdm=marker:
--┎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
--┃ Nom: Carlisi, Prenom: Nolan, Classe: TG 04 ┃
--┃ Creation: 18/10/2021 15:59:51              ┃
--┃ Mise a jour: 18/10/2021 16:09:47           ┃
--┃ Fichier: TD2_sql.py                        ┃
--┃ TD       fiche 2                           ┃
--┖━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


-- Exercice 1 {{{
-- a) A l’aide d’une requête SQL, insérer un nouveau métier dont l’identifiant est 7, le nom est ‘Cordonnier’ le lieu de travail est ‘Atelier’ et avec une rémunération de 950.
INSERT INTO "Metiers" ("id_metier","nom_metier", "lieu_travail", "remuneration")
VALUES (7, 'Cordonnier', 'Atelier', 950)
-- b) A l’aide d’une requête SQL, mettez à jour le métier de cordonnier en modifiant sa rémunération de 950 à 1200.
UPDATE "Metiers"
SET "remuneration" = 1200
WHERE nom_metier=='Cordonnier' 
--c) A l’aide d’une requête SQL, supprimez le joueur qui a pour login ‘Yphe’.
DELETE FROM "Joueurs"
WHERE login=='Yphe' 
--d) A l’aide d’une requête SQL, supprimez tous les joueurs ayant moins de 1000 golds
DELETE FROM "Joueurs"
WHERE gold<=1000 
