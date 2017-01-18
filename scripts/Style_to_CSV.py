#Script cree suite a la discussion suivante : http://georezo.net/forum/viewtopic.php?pid=290713#p290713

##Style=group
##Style to CSV=name

##Vector_layer=vector 
##Output_file=output table

import csv
layer = processing.getObject(Vector_layer)

renderer  = layer.rendererV2()
chemin_fichier = Output_file

file = open(chemin_fichier, 'wb')
file.write(u'\ufeff'.encode('utf8')) # BOM (optionel...Permet a Excel d'ouvrir proprement le fichier en UTF-8)
writer = csv.writer(file, delimiter = ';') # delimiteur ';' pour faciliter l'ouverture avec Excel
writer.writerow(['Value','Label','Hexa', 'RGBA','R','G','B','A']) # Creation des entetes

#==============================================================================
if renderer.type() == 'categorizedSymbol':
    progress.setText(u'Style categorise')
    
    categories = renderer.categories()

    for category in categories: # Recuperation des infos et ecriture dans le csv
        list =[]
        list.append(category.value().encode('utf-8')) # Valeur
        list.append(category.label().encode('utf-8')) # Label
        list.append(category.symbol().color().name().encode('utf-8')) # Couleur hexadecimale
        list.append(str(category.symbol().color().red()).encode('utf-8')+','+str(category.symbol().color().green()).encode('utf-8')+','+str(category.symbol().color().blue()).encode('utf-8') +','+str(category.symbol().color().alpha()).encode('utf-8')) # Couleur rgba
        list.append(str(category.symbol().color().red()).encode('utf-8')) # Couleur red
        list.append(str(category.symbol().color().green()).encode('utf-8')) # Couleur green
        list.append(str(category.symbol().color().blue()).encode('utf-8')) # Couleur blue
        list.append(str(category.symbol().color().alpha()).encode('utf-8')) # Alpha
        progress.setText(u'Information : %s' % list)
        writer.writerow(list) # On ecrit le tout
        
#==============================================================================
elif renderer.type() == 'singleSymbol':
    progress.setText(u'Attention : Style unique')
    
    list =[]
    list.append('singleSymbol') # Valeur
    list.append('singleSymbol') # Label
    list.append(str(renderer.symbol().color().name()).encode('utf-8')) # Couleur hexadecimale
    list.append(str(renderer.symbol().color().red()).encode('utf-8')+','+str(renderer.symbol().color().green()).encode('utf-8')+','+str(renderer.symbol().color().blue()).encode('utf-8') +','+str(renderer.symbol().color().alpha()).encode('utf-8')) # Couleur rgba
    list.append(str(renderer.symbol().color().red()).encode('utf-8')) # Couleur red
    list.append(str(renderer.symbol().color().green()).encode('utf-8')) # Couleur green
    list.append(str(renderer.symbol().color().blue()).encode('utf-8')) # Couleur blue
    list.append(str(renderer.symbol().color().alpha()).encode('utf-8')) # Alpha
    progress.setText(u'Information : %s' % list)
    writer.writerow(list) # On ecrit le tout
        
#==============================================================================
elif renderer.type() == 'graduatedSymbol':
    progress.setText(u'Attention : Style gradue')
        
    ranges = renderer.ranges()
       
    for rng in ranges: # Recuperation des infos et ecriture dans le csv
        list =[]
        list.append(str(rng.lowerValue())+"-"+str(rng.upperValue())) # Valeur
        list.append(rng.label().encode('utf-8')) # Label
        list.append(str(rng.symbol().color().name()).encode('utf-8')) # Couleur hexadecimale
        list.append(str(rng.symbol().color().red()).encode('utf-8')+','+str(rng.symbol().color().green()).encode('utf-8')+','+str(rng.symbol().color().blue()).encode('utf-8') +','+str(rng.symbol().color().alpha()).encode('utf-8')) # Couleur rgba
        list.append(str(rng.symbol().color().red()).encode('utf-8')) # Couleur red
        list.append(str(rng.symbol().color().green()).encode('utf-8')) # Couleur green
        list.append(str(rng.symbol().color().blue()).encode('utf-8')) # Couleur blue
        list.append(str(rng.symbol().color().alpha()).encode('utf-8')) #  Alpha
        progress.setText(u'Information : %s' % list)       
        writer.writerow(list) # On ecrit le tout

#==============================================================================
elif renderer.type() == 'RuleRenderer':
    progress.setText(u'Attention : Style par regle')
        
    root_rule = renderer.rootRule().children()
       
    for rule in root_rule: # Recuperation des infos et ecriture dans le csv
        list =[]
        list.append(rule.filterExpression ().encode('utf-8')) # Valeur
        list.append(rule.label().encode('utf-8')) # Label
        list.append(str(rule.symbol().color().name()).encode('utf-8')) # Couleur hexadecimale
        list.append(str(rule.symbol().color().red()).encode('utf-8')+','+str(rule.symbol().color().green()).encode('utf-8')+','+str(rule.symbol().color().blue()).encode('utf-8') +','+str(rule.symbol().color().alpha()).encode('utf-8')) # Couleur rgba
        list.append(str(rule.symbol().color().red()).encode('utf-8')) # Couleur red
        list.append(str(rule.symbol().color().green()).encode('utf-8')) # Couleur green
        list.append(str(rule.symbol().color().blue()).encode('utf-8')) # Couleur blue
        list.append(str(rule.symbol().color().alpha()).encode('utf-8')) # Alpha
        progress.setText(u'Information : %s' % list)
        writer.writerow(list) # On ecrit le tout
              
#==============================================================================
else :
    progress.setText(u'Attention : Style non gere')
    list =[]
    list.append('Style non gere') # Valeur
    list.append('Style non gere') # Label
    list.append('Style non gere') # Couleur hexadecimale    
    list.append('Style non gere') # Couleur rgba
    list.append('Style non gere')# Couleur red
    list.append('Style non gere') # Couleur green
    list.append('Style non gere') # Couleur blue
    list.append('Style non gere')# Alpha
    progress.setText(u'Information : %s' % list)    
    writer.writerow(list) # On ecrit le tout

file.close()
