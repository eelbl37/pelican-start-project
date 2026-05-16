Title: git remote aanmaken
Date: 2026-05-16
Author: Einte Elsinga
Modified: 2026-05-16
Category: git
Tags: gitremote, 
Summary: Lokaal project uploaden naar gitub
Status: Published


# remote

De onderstaande remote werkt
    git@github.com:eelbl37/pelican-start-project.git (fetch)
    git@github.com:eelbl37/pelican-start-project.git (push)

# Git project maken

Je lokale project bij github.com opslaan.

Log in en ga naar je reprositories. Rechts boven klik je op de knop NEW.
Voer een naam in en maak een README.md aan en een licesie.

Klik onder aan op CREATE  klaar



# lokale remote aanmaken

Om lange namen te voorkomen maak je eenmalig per project een remote aan.

Ga naar je project en typ.

git remote -v  # geeft de aanwezige remotes  

git remote add origin git@github.com:eelbl37/pelican-start-project.git

git remote remove  'hier de remote naam zonder''  '


# Uploaden naar github

git push origin
