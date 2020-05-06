import json
import os


def listDir(path):
    entries = os.listdir(path)
    return sorted(entries)


def readFile(filePath):
    with open(filePath, 'r') as f:
        if f.mode == "r":
            contents = f.read()
            return contents


def writeFile(filePath, data):
    with open(filePath, 'w') as f:
        f.write(data)


def innerText(content, start, end):
    return content[content.index(start)+len(start):content.index(end)]


def outerText(content, start, end):
    return content[content.index(start):content.index(end)+len(end)]


rootPath = './src/'
publicPath = './public/'


def getAllData():
    files = listDir(rootPath)
    res = []
    for file in files:
        content = readFile(rootPath+file)
        content = content.replace('""" @docStart\n', "")
        content = content.replace('\n@docEnd """', "")
        content = content.replace('/* @docStart\n', "")
        content = content.replace('\n@docEnd */', "")
        content = content.replace(
            '# @codeStart', "```"+file[file.rindex('.')+1:])
        content = content.replace('# @codeEnd', "```")
        content = content.replace(
            '// @codeStart', "```"+file[file.rindex('.')+1:])
        content = content.replace('// @codeEnd', "```")
        res.append({"name": file, "content": content})
    return json.dumps(res)


def updateVersion(forceVersion=0):
    indexFile = readFile(publicPath + 'index.html')
    oldContent = outerText(
        indexFile, '<!-- post-dep-start  -->', '<!-- post-dep-end  -->')
    currentVersion = int(innerText(oldContent, '<!-- <lib>', '</lib> -->'))
    print('currentVersion --> ', currentVersion)
    newVersion = currentVersion+1 if forceVersion == 0 else forceVersion
    print('newVersion --> ', newVersion)
    oldName = 'lib-v'+str(currentVersion)
    print('oldName --> ', oldName)
    newName = 'lib-v'+str(newVersion)
    print('newName --> ', newName)
    newContent = oldContent.replace(oldName, newName)
    newContent = newContent.replace('<!-- <lib>'+str(currentVersion) +
                                    '</lib> -->', '<!-- <lib>' + str(newVersion) + '</lib> -->')
    writeFile(publicPath+"index.html",
              indexFile.replace(oldContent, newContent))
    os.rename(publicPath + oldName, publicPath+newName)
    writeFile(publicPath+newName+"/data.json", getAllData())


def main():
    updateVersion()


main()
