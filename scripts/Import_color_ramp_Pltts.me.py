##Color Ramp=group
##Import color ramp - Pltts.me=name

##URL_Pltts=string
##Nom_du_style_en_sortie=string 
##Discrete=boolean True

from qgis.core import QgsGradientStop,QgsVectorGradientColorRampV2,QgsStyleV2
from qgis.utils import *
from PyQt4.QtGui import QColor
import urllib2  

tab = []

if Nom_du_style_en_sortie <> "":
    if  URL_Pltts[0:25]== 'http://pltts.me/palettes/': 

        req = urllib2.Request(URL_Pltts, headers={'User-Agent' : "Mozilla/5.0 "}) 

        try:
            handle = urllib2.urlopen(req)
        except IOError, e:
            progress.setText(u'Warning : ERROR URL!')
            iface.messageBar().pushMessage("Warning : ", "ERROR URL - "+URL_Pltts, QgsMessageBar.WARNING, duration=15)
            
        else:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            sock = opener.open(URL_Pltts)
            htmlSource = sock.read()                            
            sock.close()

            from HTMLParser import HTMLParser
            class AllColor(HTMLParser):
                def __init__(self):
                    HTMLParser.__init__(self)
                    self.inLink = False
                    self.dataArray = []
                    self.countColors = 0
                    self.lasttag = None
                    self.lastname = None
                    self.lastvalue = None
                def handle_starttag(self, tag, attrs):
                    self.inLink = False
                    if tag == 'div':
                        for name, value in attrs:
                            if name == 'class' and value == 'color is-dark'or value == 'color is-light':
                                self.countColors += 1
                                self.inLink = True
                                self.lasttag = tag
                def handle_endtag(self, tag):
                    if tag == 'div':
                        self.inlink = False
                def handle_data(self, data):
                    if self.lasttag == 'div' and self.inLink and data.strip():
                        progress.setText(u'Couleur : %s' % data)
                        tab.append(data)

            parser = AllColor()
            parser.feed(htmlSource)

            if Discrete ==True : 
                stop1 = QgsGradientStop(0.2, QColor(tab[1]))
                stop2 = QgsGradientStop(0.4, QColor(tab[2]))
                stop3 = QgsGradientStop(0.6, QColor(tab[3]))
                stop4 = QgsGradientStop(0.8, QColor(tab[4]))
                stops = [stop1, stop2, stop3,stop4]
                discrete = True

                colorRamp = QgsVectorGradientColorRampV2(QColor(tab[0]), QColor(tab[4]), discrete, stops)

                myStyle = QgsStyleV2().defaultStyle()
                myStyle.addColorRamp(Nom_du_style_en_sortie, colorRamp)
                
            else:
                stop1 = QgsGradientStop(0.25, QColor(tab[1]))
                stop2 = QgsGradientStop(0.50, QColor(tab[2]))
                stop3 = QgsGradientStop(0.75, QColor(tab[3]))
                stops = [stop1, stop2, stop3]
                discrete = False

                colorRamp = QgsVectorGradientColorRampV2(QColor(tab[0]), QColor(tab[4]), discrete, stops)

                myStyle = QgsStyleV2().defaultStyle()
                myStyle.addColorRamp(Nom_du_style_en_sortie, colorRamp)

    else :
        progress.setText(u'Warning : URL!')
        iface.messageBar().pushMessage("Warning : ", "URL - "+URL_Pltts, QgsMessageBar.WARNING, duration=15)
else :
    progress.setText(u'Warning : Name')
    iface.messageBar().pushMessage("Warning : ", "Name", QgsMessageBar.WARNING, duration=15)