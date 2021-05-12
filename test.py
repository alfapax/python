#---- Fla
import re
import openpyxl
##intest = input("La stampa è per uso interno o esterno? - i / e: ")

f = open("d:\\temp\\Test_Leggi_Gcode\\HVMCV_04.gcode")
content = f.read()
data = content[52:65]
buildtime = content[-191:-156]
filamentLength = content[-154:-112]
plasticVolume = content[-110:-65]
plasticWeight = content[-63:-26]
materialCost = content[-24:]
#print(buildtime, filamentLength, plasticVolume, plasticWeight, materialCost)
bt = re.findall(r'\d+', buildtime )
fl = re.findall(r'[0-9].+?mm', filamentLength)
pv = re.findall(r'\d.+?[mm^3]', plasticVolume)
pw = re.findall(r'\d.+g', plasticWeight)
mc = re.findall(r'[0-9].+', materialCost)
tipos = re.match(r"Speed", content)
tipoq = re.match(r'quality', content)
dataset = re.findall(r'\W', data)
count = 0
for match in re.finditer("layer \d+", content):
    count = count + 1

# bd = buildtime [14:]
# fl = filamentLength [18:]
# pv = plasticVolume [17:]
# pw = plasticWeight [17:]
# mc = materialCost [16:]
""" print ('Tempo di Stampa:', bd)
print ('lunghezza filamento:', fl)
print ('volume materiale:', pv)
print ('peso materiale:', pw)
print ('costo materiale:', mc) """

print(bt)
print(fl)
print(pv)
print(pw)
print(mc)
print(count)
print(tipos)
print(tipoq)
print(data)
##print(intest)
##print(name)