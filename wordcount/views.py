from django.shortcuts import render
import re
import operator


def mainPage(request):
    

    return render(request,'main.html')





def countedPage(request):
    getParam = request.GET['texts']

    count = len(re.findall(r'\w+',getParam))

    wordDict = re.findall(r'\w+',getParam)
    newDict = {}
    for words in wordDict:
        if words in newDict:
            newDict[words] +=1
        else:
            newDict[words] = 1

    #for sort Desc
    sortedWord = sorted(newDict.items(),key=operator.itemgetter(1),reverse=True)
    
    return render(request,'counted.html',{"result":count,'mostWord':sortedWord})    


def aboutPage(request):
    return render(request,'about.html') 