from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def uppercase(request):
    return render(request, "uppercase.html")

def lowercase(request):
    return render(request, "lowercase.html")

def remove(request):
    return render(request, "remove.html")

def removepunc(request):
    return render(request, "removepunc.html")

def extraspaces(request):
    return render(request, "extraspace.html")

def wordscount(request):
    return render(request, "wordcount.html")

def replace(request):
    return render(request, "replace.html")

def about(request):
    return render(request, "about.html")



def an_uppercase(request):
    Text=request.POST.get('text', 'default')
    UpperCase= Text.upper()
    parameters={'operation': "Uppercasing", 'Analyzed_text':UpperCase}
    return render(request, "analyze.html", parameters)

def an_lowercase(request):
    Text=request.POST.get('text', 'default')
    LowerCase =Text.lower()
    parameters={'operation': "Lowercasing", 'Analyzed_text':LowerCase}
    return render(request, "analyze.html", parameters)

def an_removepunc(request):
    Text=request.POST.get('text', 'default')
    punctuations="""~!@#$%^&*()_+=-;'":<>/"""
    Analyzed=""
    for char in Text:
        if char not in punctuations:
            Analyzed=Analyzed+char
    parameters={'operation': "Removing Punctuations", 'Analyzed_text':Analyzed}
    return render(request, "analyze.html", parameters)

def an_extraspaces(request):
    Text=request.POST.get('text', 'default')
    spaceremoved=""
    for index, char in enumerate (Text):
        if not(Text[index]== " " and Text[index+1]==" "):
            spaceremoved = spaceremoved + char
    parameters={'operation': "Removing Extra Spaces", 'Analyzed_text':spaceremoved}
    return render(request, "analyze.html", parameters)

def an_wordscount(request):
    Text=request.POST.get('text', 'default')
    spaceremoved=""
    for index, char in enumerate (Text):
        if not(Text[index]== " " and Text[index+1]==" "):
            spaceremoved = spaceremoved + char
    wordscount=len(spaceremoved.split())
    parameters={'operation': "Counting Words", 'Analyzed_text': wordscount}
    return render(request, "wordcountout.html", parameters)

def an_remove(request):
    Text=request.POST.get('text', 'default')
    replace=request.POST.get('replace', 'default')
    replaced=Text.replace( f"{replace}", "")
    replaced1=replaced.replace( f" {replace} ", "")
    replaced2=replaced1.replace( f"{replace} ", "")
    replaced3=replaced2.replace( f" {replace}", "")
    parameters={'operation': "Removing", 'Analyzed_text':replaced3}
    return render(request, "replaceout.html", parameters)
    


def an_replace(request):
    Text=request.POST.get('text', 'default')
    replace=request.POST.get('replace', 'default')
    by= request.POST.get('by', 'default')
    replaced=Text.replace( f"{replace}", f"{by}")
    replaced1=replaced.replace( f" {replace} ", f"{by}")
    replaced2=replaced1.replace( f" {replace}", f"{by}")
    replaced3=replaced2.replace( f"{replace} ", f"{by}")
    parameters={'operation': "Replacement", 'Analyzed_text':replaced3, 'replace':replace, 'by': by }
    return render(request, "replaceout.html", parameters)
    

