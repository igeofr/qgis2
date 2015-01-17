Fichiers de style pour QGIS
=====

Pour charger un style dans QGIS :

1. Clic droit sur la couche.
2. Ouvrir les propriétés de la couche.
3. Se placer sur l'onglet : "Style".
4. Pour terminer : "Charger le style..." au format qml.  

**Les styles disponibles :**
- [Corine Land Cover] (http://www.statistiques.developpement-durable.gouv.fr/donnees-ligne/li/1825.html) :
  Fichiers de style créés pour QGIS 2.6 (Attention à la compatibilité)

  Pour la France métropolitaine :
      - [CLC Niveau 1] (styles/clc/clc_niveau1.qml)
      - [CLC Niveau 2] (styles/clc/clc_niveau2.qml)
      - [CLC Niveau 3] (styles/clc/clc_niveau3.qml)

  Pour les départements d'outre-mer (DOM) :
      - [CLC DOM Niveau 1] (styles/clc/clc_dom_niveau1.qml)
      - [CLC DOM Niveau 2] (styles/clc/clc_dom_niveau2.qml)
      - [CLC DOM Niveau 3] (styles/clc/clc_dom_niveau3.qml)

Modèles pour QGIS
=====

Voici plusieurs modèles créés à partir du modeleur graphique de QGIS

**Les modèles disponibles :**
- Indice de forme :
  Modèles créés pour QGIS 2.6 (Attention à la compatibilité)

  - [Indice d'élongation] (models/Indice_elongation.model) : Rapport entre la longueur et largeur de l'entité
  - [Indice de Gravelius] (models/Indice_gravellius.model) : Rapport du périmètre de l'entité, à celui du cercle de même superficie (Non borné, supérieur ou égale à 1)
  - [Indice de Miller] (models/Indice_miller.model) : Indice d'étalement qui tend vers 0 pour une forme plus étirée.
  - [Indice de Morton] (models/Indice_morton.model) : Rapport de la superficie d'une entité, à celle d'un cercle de même périmètre (Vaut 1 si le polygone est un cercle, 0 s'il est de surface nulle)  

En lien, avec une discussion sur [Georezo : "elongation, formes des polygones"] (http://georezo.net/forum/viewtopic.php?pid=143436#p143436)
