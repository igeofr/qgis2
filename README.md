# Fichiers de style pour QGIS

Pour charger un style dans QGIS :

1. Clic droit sur la couche.
2. Ouvrir les propriétés de la couche.
3. Se placer sur l'onglet : "Style".
4. Pour terminer : "Charger le style..." au format qml.  

**Les styles disponibles :**
- Les styles on été déplacés dans un autre dépôt afin de pouvoir être utilisé via le plugin [QGIS Resources Sharing](https://github.com/igeofr/qgis_styles)

# Modèles pour QGIS

Voici plusieurs modèles créés à partir du modeleur graphique de QGIS

**Les modèles disponibles :**
- Indice de forme : Modèles créés pour QGIS 2.6 (Attention à la compatibilité)

  - Indice d'élongation : Rapport entre la longueur et largeur de l'entité.
  - [Indice de Gravelius] (models/Indice_gravellius.model) : Rapport du périmètre de l'entité, à celui du cercle de même superficie (Non borné, supérieur ou égale à 1).
  - [Indice de Miller] (models/Indice_miller.model) : Rapport de la superficie d'une entité, à celle d'un cercle de même périmètre (Vaut 1 si le polygone est un cercle, 0 s'il est de surface nulle).
  - Indice de Morton : Rapport de la superficie d'une entité, à celle d'un cercle de même périmètre (Vaut 1 si le polygone est un cercle, 0 s'il est de surface nulle).
  - [Indice de Solidité] (models/Indice_solidite.model): Rapport de la superficie d'une entité, à celle de son enveloppe convexe. (Vaut 1 pour un objet convexe, nettement < 1 si fortes concavités(forme complexe))
  - [Indice de Concavité] (models/Indice_concavite.model): Rapport du périmètre de l'entité, à celui de son enveloppe convexe. (Vaut 1 pour un objet convexe ou > 1 si fortes concavités (forme complexe))

En lien, avec une discussion sur [Georezo : "elongation, formes des polygones"] (http://georezo.net/forum/viewtopic.php?pid=143436#p143436)

# Scripts pour le processing de QGIS

Pour ajouter un script dans QGIS :

1. Ouvrir la boite à outils de traitement
2. Aller dans Scripts/Outils/Ajouter un script depuis le fichier

Documentation QGIS : [Créer des scripts et les exécuter depuis la boîte à outils] (http://docs.qgis.org/2.6/fr/docs/user_manual/processing/console.html)

**Les scripts disponibles :**

  - Scipts : Testé sur QGIS 2.6 (Attention à la compatibilité)

  - [CSV R-G-B to categorized style](scripts/CSV_R-G-B_to_categorized_style.py) : Permet de créer une symbologie catégorisée à partir de champs séparés Red, Green et Blue contenu dans un fichier CSV
  - [CSV RGB or HEX to categorized style] (scripts/CSV_RGB_or_HEX_to_categorized_style.py) : Permet de créer une symbologie catégorisée à partir d'un champ R,G,B ou hexadécimal contenu dans un fichier CSV
  - [Style to CSV](scripts/Style_to_CSV.py) : Permet de récupérer les informations (Value, Label, Hexa, RGBA, R, G, B, A) d'un style créé sur QGIS (style catégorisé, ensemble de règles,...) au format CSV ce script fait a été créé suite à une discussion sur [Georezo](http://georezo.net/forum/viewtopic.php?pid=290713#p290713)
  - [Import color ramp Colourslovers.com] (scripts/Import_color_ramp_Colourlovers.com/Import_color_ramp_Colourlovers.com.py) : Permet d'importer une palette de couleurs dans QGIS à partir des palettes référencées sur le site [Colourlovers.com](Colourlovers.com)
  - [Cadastre FR WMS] (scripts/Cadastre_FR/) : Afficher le Cadastre (WMS) de plusieurs communes à partir d'une couche vectorielle des communes.

# Flux

**Flux WMS et WFS**

Vous trouverez [ici](flux/QGIS_WMS.xml) une liste de flux WMS et [ici](flux/QGIS_WFS.xml) une liste de flux WFS pour QGIS. N'hésitez pas à compléter ces listes.

Pour ajouter des flux dans QGIS depuis un fichier xml :

  1. Menu "Couche" / Ajouter une couche / Ajouter une couche WMS ou WFS
  2. Cliquer sur charger et sélectionner le xml
  3. Sélectionner les flux à importer
  4. Importer

# Calculatrice

**Expressions disponibles :**

  - [Supprimer les accents d'un champs (Minuscules)](expressions/supprimer_les_accents_minuscules.txt)
  - [Supprimer les accents d'un champs (Majuscules)](expressions/supprimer_les_accents_minuscules.txt)
  - [Mise en forme des toponymes] (expressions/mise_en_forme_des_toponymes.txt)
  - [Mise en forme des toponymes une V2 plus complète en TEST](expressions/mise_en_forme_des_toponymes_V2_beta.txt) et basé sur [ce document de l'IGN](http://www.ign.fr/sites/all/files/charte_toponymie_ign.pdf) / Voir aussi [cet échange sur Géorezo](http://georezo.net/forum/viewtopic.php?pid=281390)
