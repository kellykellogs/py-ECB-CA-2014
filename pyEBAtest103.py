# -*- coding: utf-8 -*-
"""
Created on Sun Nov 02 19:33:28 2014

@author: Kelly
"""


from EBA_ST_2014 import *


import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)    



#OtherTemplates
#Bank_code	Period	Item	Scenario	AMOUNT
fname = 'Other_templates_v2.csv'
import csv


Z = {}
S = {}
f = open(fname, 'rt')
try:
    reader = csv.reader(f)
    k = 0
    for row in reader:
        k = k + 1
        if k > 1:
        #if row[0] == 'JEUVK5RWVJEN8W0C9M24':
            if int(row[2]) in [993434, 993501,993502,993601,993402,993441,993603,993602]:
                entity = row[0]
                period = int(row[1])
                label = int(row[2])
                scenario = int(row[3])
                amount= row[4]
                if entity in Z:
                    pass
                else:
                    Z[entity]={}
                if period> 0:
                    if True:
                        if label in SDDLabel:

                            pass
                            if label in Z[entity]:
                                pass
                            else:
                                Z[entity][label]={}
                        else:
                            label
        
                        if period in Z[entity][label]:
                            pass
                        else:
                            Z[entity][label][period]=[None,None,None,None]
                                
                        Z[entity][label][period][scenario] = amount
                 
finally:
    f.close()


import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)    



print ''
print ' ------------------------------- '
print ' -------     START      -------- '
print ' ------------------------------- '

print ' capital shortfalls with restructuring plans '

from ECB_CA_2014 import *





ECB = {}
for g in generateAll:
    b = g
    ECB[b.shortname] = b

results = {}

for entity in Z:
    S = Z[entity]
    CET1      = float(S[993434][201612][3])
    shortfallB10 = max(CET1*5.5/100.0 - float(S[993402][201612][3]) ,0.0)
    if True:#shortfallB10>0.0:
        
       
        for label in [993441,993603,993402,993501,993601,993434,993502,993602]  :
            
            lines = []
            N = 0
            for period in S[label]:
                line = str( period) +'\t'+ str(S[label][period][2]).rjust(7, ' ')+'\t\t'+str(S[label][period][3]).rjust(7, ' ')
                #"For %s : %d  %d" % (period,  int(S[label][period][2]),int(S[label][period][3]))
                lines.append(line)
                #N = abs(float(S[label][period][2]))+abs(float(S[label][period][3]))
            #print lines
            lines = [SDDLabel[label]+'   '+str(label),'Period\t'+Scenario[2]+'\t '+Scenario[3] ] + natural_sort(lines)
            
            for line in lines:
                pass
                #print line
        REAdv      = max(float(S[993434][201412][3]),max(float(S[993434][201612][3]),float(S[993434][201512][3])))
        REBsl      = max(float(S[993434][201412][2]),max(float(S[993434][201612][2]),float(S[993434][201512][2])))
        REBsl      = float(S[993434][201612][2])
        REAdv      = float(S[993434][201612][3])
        shortfallB10 = max(REAdv*5.5/100.0 - float(S[993402][201612][3]) ,0.0)
        shortfallB9 = max(REBsl*8.0/100.0 - float(S[993402][201612][2]) ,0.0)
      


        REBslR      = float(S[993434][201612][2]) +float(S[993502][999912][2] )
        REAdvR      = float(S[993434][201612][3]) +float(S[993502][999912][3] )
        shortfallB10R = max(REAdvR*5.5/100.0 - float(S[993402][201612][3])- float(S[993501][999912][3]),0.0)
        shortfallB9R = max(REBslR*8.0/100.0 - float(S[993402][201612][2])-float(S[993501][999912][2]) ,0.0)
      
        if abs(REBsl-REBslR)>0.0 :
            results[entity]= [shortfallB9,shortfallB10,shortfallB9R,shortfallB10R]


for e in results:
    print ''
    print Bank_name[e]
    print 'B9\t',results[e][0],', B9R\t',results[e][2]
    print 'B10\t',results[e][1],', B10R\t',results[e][3]

print ' ------------------------------- '
raw_input('END. EXIT ?')