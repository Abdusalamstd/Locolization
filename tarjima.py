#coding=utf-8
'''
Before: pip install googletrans
''''

import xml.etree.ElementTree as ET
import time

from googletrans import Translator
A = Translator(service_urls=['translate.google.cn'])

File_name = "" #بۇ يەرگە تەرجىمە قىلىدىغان "ت س" ھۆججەت نامى
#example: File_name = 'for_translation_deepin-phone-master_deepin-phone-master_ug.ts'

tree = ET.parse(File_name)
root = tree.getroot()

cnt=0
for chi in root:
    for j in chi:
        if j.tag == 'message':
            for elem in j:
                if elem.tag == 'source':
                    preTag = elem.text
                if elem.tag == 'translation':
                    elem.text = A.translate(preTag,dest='ug',src='en').text
                    cnt+=1
                if cnt%20==0:
                    time.sleep(8)
                    # يىگىرمىنى تەرجىمە قىلىپ بولۇپ،سەككىز سېكۇنىت ئۇخلىتىپ قويىمىز. بولمىسا گوگۇل تەرجىمانى ئايپى ئادېرسىڭىزنى پىچەتلىۋىتىپ قېلىشى مۇمكىن
                    
tree.write('finished.ts',encoding='utf-8')
# ئاخېرىدا "ت س" ھۆججىتىنى باسقابىر نامدا ساقلىۋىلىپ چىكىتىمىز،ئەسلى ھۆججەت بۇزۇلمايدۇ
# finished.ts بولسا تاماملانغان ھۆججەت
