from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("C:/Users/Asus/Downloads/go_obo.xml")
obo = DOMTree.documentElement
# get the root element of the document
terms = obo.getElementsByTagName("term")
# a list of 'terms' elements
print('The number of terms is ',len(terms))
# list1 stores id, list2 stores name ,list3 stores definition, list4 stores childnodes.
list1 = []
list2 = []
list3 = []
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    each_id = term.getElementsByTagName('id')[0].childNodes[0].data
    each_name = term.getElementsByTagName('name')[0].childNodes[0].data
    if defstr.find('autophagosome')>0:
            list1.append(each_id)
            list2.append(each_name)
            list3.append(defstr)

# use dic1 to caculate the number of childnodes.
dic1 = {}
for term in terms:
    each_id = term.getElementsByTagName('id')[0].childNodes[0].data
    is_a_list = []
    for i in term.getElementsByTagName('is_a'):
        is_a_list.append(i.childNodes[0].data)
    for is_a in is_a_list:
        if is_a in dic1:
            dic1[is_a].append(each_id)
        else:
            dic1[is_a] = [each_id]
# add the id and is_a in the dictionary
# key = parent node/id, value = child node/is_a

def calculate(list0):
    for i in list0:
        if i in list0:
            if i not in list5:
                list5.append(i)
                if i in dic1:
                    calculate(dic1[i])
    return len(list5)
list4 = []
for term in terms:
    each_id = term.getElementsByTagName('id')[0].childNodes[0].data
    defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    if defstr.find('autophagosome')>0:
        nodes = 0
        list5 = []
        if each_id in dic1:
            nodes = calculate(dic1[each_id])
        list4.append(nodes)
from pandas import DataFrame
data = {'id': list1, 'name': list2, 'definition': list3, 'childnodes': list4}
df = DataFrame(data)
df.to_excel('autophagosome.xlsx')
