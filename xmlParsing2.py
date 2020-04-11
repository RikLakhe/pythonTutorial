import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user><name age='33'>Ram</name><id>001</id></user>
        <user><name age='22'>Ram2</name><id>002</id></user>
        <user><name age='44'>Ram4</name><id>004</id></user>
    </users>
    <test>
        <user><name age='44'>Ram4</name><id>004</id></user>    
    </test>
</stuff>
'''

stuff =ET.fromstring(input)

lt = stuff.findall('test/user')

print('user count ',len(lt))

for item in lt:
    print('name',item.find('name').text)
    print('age',item.find('name').get('age'))
    print('id',item.find('id').text)


