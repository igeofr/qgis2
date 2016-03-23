##Color Ramp=group
##Import color ramp - ColourLovers.com=name

##URL_palette_ColourLovers=string 
##Style_name=string
##Discrete=boolean True

from qgis.core import QgsGradientStop,QgsVectorGradientColorRampV2,QgsStyleV2
from qgis.utils import *
from qgis.gui import *
from PyQt4.QtGui import QColor
import urllib2
from string import split

tab = []

if Style_name <> "":
    if  URL_palette_ColourLovers[0:36]== 'http://www.colourlovers.com/palette/':

        req = urllib2.Request(URL_palette_ColourLovers, headers={'User-Agent' : "Mozilla/5.0 "})

        try:
            handle = urllib2.urlopen(req)
        except IOError, e:
            progress.setText(u'Warning : ERROR URL!')
            iface.messageBar().pushMessage("Warning : ", "ERROR URL - "+URL_palette_ColourLovers, QgsMessageBar.WARNING, duration=15)

        else:
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            sock = opener.open(URL_palette_ColourLovers)
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
                    if tag == 'h4':
                            self.countColors += 1
                            self.inLink = True
                            self.lasttag = tag
                def handle_endtag(self, tag):
                    if tag == 'h4':
                        self.inlink = False
                def handle_data(self, data):
                    if self.lasttag == 'h4' and self.inLink and data.strip():
                        if "," in data and data.count(',')==2 :
                            progress.setText(u'Couleur : %s' % data)
                            tab.append(data)

            parser = AllColor()
            parser.feed(htmlSource)
                       
            if len(tab) == 2 :

                if Discrete ==True :
                    stop1 = QgsGradientStop(0.5, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stops = [stop1]
                    discrete = True
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2]))
                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete,stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)
                    
                else:
                    discrete = False
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2]))
                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)   

            if len(tab) == 3 :

                if Discrete ==True :
                    stop1 = QgsGradientStop(0.33, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stop2 = QgsGradientStop(0.66, QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2])))
                    stops = [stop1,stop2]
                    discrete = True
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2]))
                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete,stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)
                    
                else:
                    stop1 = QgsGradientStop(0.5, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stops = [stop1]
                    discrete = False
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2]))
                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete,stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)                   

            if len(tab) == 4 :

                if Discrete ==True :
                    stop1 = QgsGradientStop(0.25, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stop2 = QgsGradientStop(0.50, QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2])))
                    stop3 = QgsGradientStop(0.75, QColor(int(split(tab[3],',')[0]), int(split(tab[3],',')[1]), int(split(tab[3],',')[2])))
                    stops = [stop1,stop2,stop3]
                    discrete = True
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[3],',')[0]), int(split(tab[3],',')[1]), int(split(tab[3],',')[2]))
                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete,stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)
                    
                else:
                    stop1 = QgsGradientStop(0.33, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stop2 = QgsGradientStop(0.66, QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2])))
                    stops = [stop1,stop2]
                    discrete = False
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[3],',')[0]), int(split(tab[3],',')[1]), int(split(tab[3],',')[2]))
                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete,stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)   

            if len(tab)==5 :                 
                
                if Discrete ==True :

                    stop1 = QgsGradientStop(0.2, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stop2 = QgsGradientStop(0.4, QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2])))
                    stop3 = QgsGradientStop(0.6, QColor(int(split(tab[3],',')[0]), int(split(tab[3],',')[1]), int(split(tab[3],',')[2])))
                    stop4 = QgsGradientStop(0.8, QColor(int(split(tab[4],',')[0]), int(split(tab[4],',')[1]), int(split(tab[4],',')[2])))
                    stops = [stop1,stop2,stop3,stop4]
                    discrete = True
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[4],',')[0]), int(split(tab[4],',')[1]), int(split(tab[4],',')[2]))

                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete, stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)
                    
                    
                else:
                    stop1 = QgsGradientStop(0.25, QColor(int(split(tab[1],',')[0]), int(split(tab[1],',')[1]), int(split(tab[1],',')[2])))
                    stop2 = QgsGradientStop(0.50, QColor(int(split(tab[2],',')[0]), int(split(tab[2],',')[1]), int(split(tab[2],',')[2])))
                    stop3 = QgsGradientStop(0.75, QColor(int(split(tab[3],',')[0]), int(split(tab[3],',')[1]), int(split(tab[3],',')[2])))
                    stops = [stop1,stop2,stop3]
                    discrete = False
                    
                    color1 = QColor(int(split(tab[0],',')[0]), int(split(tab[0],',')[1]), int(split(tab[0],',')[2]))
                    color2 = QColor(int(split(tab[4],',')[0]), int(split(tab[4],',')[1]), int(split(tab[4],',')[2]))

                    colorRamp = QgsVectorGradientColorRampV2(color1, color2, discrete, stops)
                    
                    myStyle = QgsStyleV2().defaultStyle()
                    myStyle.addColorRamp(Style_name, colorRamp,True)
                    


    else :
        progress.setText(u'Warning : URL!')
        iface.messageBar().pushMessage("Warning : ", "URL - "+URL_palette_ColourLovers, QgsMessageBar.WARNING, duration=15)
else :
    progress.setText(u'Warning : Name')
    iface.messageBar().pushMessage("Warning : ", "Name", QgsMessageBar.WARNING, duration=15)
           