""" @docStart
### Text **Extraction** <span style="font-size:10px">must watch</span>
##### An **innerText** function
which gives content beteween two substring
@docEnd """

# @codeStart

greet = "Welcome to KodeNoteBook.web.app"

def innerText(x, y, z):
    return "" if y not in x else x[x.find(y)+len(y):x.find(z)]

print(innerText(greet, 'Wel', 'Note'))
# come to Kode

# @codeEnd

""" @docStart
##### An **outerText** function
which gives content beteween two substring including substring
@docEnd """

# @codeStart
def outerText(x, y, z):
    return "" if y not in x else x[x.find(y):x.find(z)+len(z)]

print(outerText(greet, 'Wel', 'Note'))
# Welcome to KodeNote

# @codeEnd

