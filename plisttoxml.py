import xml.etree.ElementTree as ET

tree = ET.parse('Strings.plist')
root = tree.getroot()

keylist = []
valuelist = []
for string in root.iter('key'):
	keylist.append(string.text)

for string in root.iter('string'):
	valuelist.append(string.text)

writefile = open("Strings1.xml", "w")
writefile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
writefile.write('<resources>\n')


for x in range(len(keylist)):
	writefile.write('<string name="' + keylist[x] + '">' + valuelist[x] + '</string>\n')

writefile.write('</resources>')
writefile.close()