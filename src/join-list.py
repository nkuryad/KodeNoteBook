""" @docStart
### List Join
a function to join list of strings
@docEnd """

# @codeStart
# join with takes ',' as default param
def join(ar, joinWith=","):
    res = ""
    for i in range(0, len(ar)-1):
        res += ar[i]+joinWith
    return res+ar[-1]


print(join(['kode', 'note', 'book']))
# kode,note,book
print(join(['kode', 'note', 'book'], '-'))
# kode-note-book

# @codeEnd