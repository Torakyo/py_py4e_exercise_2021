#Parse XML
import xml.etree.ElementTree as ET      # ET as a shortcut for this library.

# Use ''' to contain certain data
data = ''' 
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

# Use fromstring method to convert strings into elements.
tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))

print()
#Loop through nodes
import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')           # Method findall() creates a list to contain matching elements.
print('User count: ', len(lst))
lst2 = stuff.findall('users/user/id')
print('Id Count:', len(lst2))

print()
for i in stuff:
    print('Name', i.find('name').text)
    print('Id', i.find('id').text)
    print('Attr: ', i.get('x'))


