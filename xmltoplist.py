import xml.etree.ElementTree as ET

tree = ET.parse('Strings.xml')
root = tree.getroot()


writefile = open("Strings.plist", "w")
writefile.write('<?xml version="1.0" encoding="UTF-8"?>')
writefile.write('<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">')
writefile.write('<plist version="1.0">')
writefile.write('<dict>')

for string in root.iter('string'):
	key = string.get('name')
	value = string.text
	writefile.write('<key>' + key + '</key>')
	writefile.write('<string>' + value + '</string>')
	print key,value

writefile.write('</dict>')
writefile.write('</plist>')


writefile.close()

