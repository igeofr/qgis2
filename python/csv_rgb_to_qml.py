from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.gui import QgsMessageBar
import csv

layer = iface.activeLayer()

######## Emplacement du csv
InFlnm='CLC_DOM_nomenclature_03.csv'
InDrPth='/Users/Florian/Downloads/'
InFlPth=InDrPth+InFlnm

######## Ouverture du csv
read_csv = csv.reader(open(InFlPth,"rU"),delimiter=";")

########Permet de passer l'entete du csv
read_csv.next()

########Creation d'un tableau
tab = []
for row in read_csv:
    
######## Permet de definir l'encodage du csv
        unicode_row = [x.decode('latin1') for x in row]
        
######## Permet de definir les colonnes value, label, red, green, blue dans le csv
        col_select =row[0], row[1],row[4], row[5], row[6]
        tab.append(col_select)
        
categories = []
for value, label, red, green, blue in tab :
    
########Concatener r,g,b
    color_rgb = red+','+green+','+blue
    
######## Source : http://gis.stackexchange.com/questions/53121/how-change-border-line-to-no-pen-with-python-console
    symbol = QgsFillSymbolV2.createSimple( {'style':'solid','outline_style':'no','outline_width':'0','color':color_rgb} )
    symbol.setAlpha (0.5)
    category = QgsRendererCategoryV2(value, symbol, label)
    categories.append(category)

######## Permet de creer le rendu et de l'affecter a la couche sur un champ defini
expression = 'CODE_00' # Nom du champ
if layer <> None:
    renderer = QgsCategorizedSymbolRendererV2(expression, categories)
    layer.setRendererV2(renderer)
    iface.messageBar().pushMessage("Notification", "Execute avec succes", QgsMessageBar.INFO, 2)

    ######## Permet d'exporter le qml
    layer.saveNamedStyle('/Users/Florian/Downloads/style.qml')
    
else :
    iface.messageBar().pushMessage("Attention", "Selectionner une couche", level=QgsMessageBar.WARNING, duration=2)

iface.mapCanvas().refresh() 