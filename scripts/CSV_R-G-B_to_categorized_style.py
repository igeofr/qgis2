##Couche_vectorielle=vector 
##Nom_du_champ=field Couche_vectorielle
##Fichier_CSV_avec_separateur_point_virgule= file 
##Encodage_du_CSV=string latin1
##Colonne_de_la_value=number 0
##Colonne_du_label=number 1
##Colonne_red=number 4
##Colonne_green=number 5
##Colonne_blue=number 6
##Transparence_du_style=number 0.50
##Outline=boolean false
##Line_Outline_width=number 0.26
##Save_layer_style_as_default=boolean false

from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import csv
import codecs
import os

layer = processing.getObject(Couche_vectorielle)

filePth = layer.dataProvider().dataSourceUri()
myDirectory,nameFile = os.path.split(filePth)
nomCouche = str(os.path.splitext(os.path.split(filePth)[1])[0])

# Verifie l'extension du fichier demande : CSV
fileName, fileExtension = os.path.splitext(Fichier_CSV_avec_separateur_point_virgule)
if  fileExtension =='.csv':
    # Ouverture du csv
    read_csv = csv.reader(codecs.open(Fichier_CSV_avec_separateur_point_virgule,"ru", Encodage_du_CSV),delimiter=";")
    #Permet de passer l'entete du CSV
    read_csv.next()
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Creation d'un tableau qui va stocker les lignes et colonnes choisies du CSV  
    tab = []
    for row in read_csv:
            # Permet de definir les colonnes value, label, red, green, blue
            col_select =row[Colonne_de_la_value], row[Colonne_du_label],row[Colonne_red], row[Colonne_green], row[Colonne_blue]
            # Insere chaque ligne du CSV dans le tableau
            tab.append(col_select)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    categories = []
    for value, label, red, green, blue in tab :
        #Concatener r,g,b
        color_rgb = red+','+green+','+blue
        # Creation de la ligne
        if Outline == False :
           b_outline = 'no'
        else :
            b_outline = 'yes'
        # Largeur de la ligne
        v_width = str(Line_Outline_width)

        # Polygones
        if layer.dataProvider().geometryType() == 3:
            # Source : http://gis.stackexchange.com/questions/53121/how-change-border-line-to-no-pen-with-python-console
            symbol = QgsFillSymbolV2.createSimple( {'style':'solid','outline_style':b_outline,'outline_width':v_width,'color':color_rgb} )
            symbol.setAlpha (Transparence_du_style)
                
            category = QgsRendererCategoryV2(value, symbol, label)
            categories.append(category)

        # Lignes
        if layer.dataProvider().geometryType() == 2:     
            symbol = QgsLineSymbolV2.createSimple( {'style':'solid','line_width':v_width,'color': color_rgb} )
            symbol.setAlpha (Transparence_du_style)
                
            category = QgsRendererCategoryV2(value, symbol, label)
            categories.append(category)

        # Points
        if layer.dataProvider().geometryType() == 1:     
            symbol = QgsMarkerSymbolV2.createSimple( {'style':'solid','outline_style':'no','outline_width':v_width,'color': color_rgb} )
            symbol.setAlpha (Transparence_du_style)
                
            category = QgsRendererCategoryV2(value, symbol, label)
            categories.append(category)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Permet de creer le rendu et de l'affecter a la couche sur un champ defini
    
    # Nom du champ sur lequel doit s'appliquer la symbologie
    expression = Nom_du_champ

    renderer = QgsCategorizedSymbolRendererV2(expression, categories)
    layer.setRendererV2(renderer)
    
    # Creation des fichiers de style
    if Save_layer_style_as_default :
        # QML
        layer.saveDefaultStyle() 
        # SLD
        layer.saveSldStyle(myDirectory+'/'+nomCouche+'.sld')
            
    iface.messageBar().pushMessage("Notification :", "Execute avec succes", QgsMessageBar.INFO, duration=2)

    iface.mapCanvas().refresh() 

else :
    iface.messageBar().pushMessage("Ohoh :", "J'ai demande un csv!", QgsMessageBar.WARNING, duration=2)