from PyQt4.QtCore import *
from PyQt4.QtGui import *
import csv
import codecs

layer = iface.activeLayer()

######## Emplacement du csv
InFlnm='RPG_2012_ Codes_groupes_cultures_et_couleurs.csv'
InDrPth='/Users/Florian/Downloads/'
InFlPth=InDrPth+InFlnm

######## Ouverture du csv
read_csv = csv.reader(codecs.open(InFlPth,"ru", "latin1"),delimiter=";")

########Permet de passer l'entete du csv
read_csv.next()

########Creation d'un tableau des valeurs
tab = []
for row in read_csv:
######## Permet de definir les colonnes value, label, red, green, blue
        col_select =row[0], row[1],row[2]
        print col_select
        
        tab.append(col_select)
        
########Creation d'un tableau des categories
categories = []
for value, label, color_hex in tab :
    
######## Source : http://gis.stackexchange.com/questions/53121/how-change-border-line-to-no-pen-with-python-console
    symbol = QgsFillSymbolV2.createSimple( {'style':'solid','outline_style':'no','outline_width':'0','color':color_hex} )
    symbol.setAlpha (0.5)
    
    category = QgsRendererCategoryV2(value, symbol, label)
    categories.append(category)

######## Permet de creer le rendu et de l'affecter a la couche sur un champ defini
expression = 'CULT_MAJ' # Nom du champ
if layer <> None:
    renderer = QgsCategorizedSymbolRendererV2(expression, categories)
    layer.setRendererV2(renderer)
    
    iface.messageBar().pushMessage("Notification", "Execute avec succes", QgsMessageBar.INFO, duration=2)

    ######## Permet d'exporter le qml
    layer.saveNamedStyle('/Users/Florian/Downloads/style.qml')
    
else :
    iface.messageBar().pushMessage("Attention", "Selectionner une couche", level=QgsMessageBar.WARNING, duration=2)

iface.mapCanvas().refresh() 