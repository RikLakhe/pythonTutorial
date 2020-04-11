import xml.etree.ElementTree as ET

data = '''
<person><name>Chuck</name><age>22</age><color>dark brown</color><phone type='intl'>+1 734 303 4456</phone><email hide='yes' /></person>'''

tree = ET.fromstring(data)

print("Name",tree.find('name').text)
print("attr",tree.find('email').get('hide'))