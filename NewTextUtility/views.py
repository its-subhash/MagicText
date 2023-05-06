from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def next(request):
    Text=request.GET.get('text', 'default')
    save=""
    # Checking Conditions
    Uppercase=request.GET.get('Uppercase', 'off')
    Lowercase=request.GET.get('Lowercase', 'off')
    remove=request.GET.get('remove', 'off')
    removepunc=request.GET.get('removepunc', 'off')
    extraspace=request.GET.get('extraspace', 'off')
    Wordscount=request.GET.get('Wordscount', 'off')
    replace=request.GET.get('replace', 'off')
    # for removing punctuations
    if removepunc == "on":
        punctuations="""~!@#$%^&*()_+=-;'":<>/"""
        Analyzed=""
        for char in Text:
            if char not in punctuations:
                Analyzed=Analyzed+char
        save=Analyzed
        parameters={'operation': "Removing Punctuations", 'Analyzed_text':Analyzed}
        return render(request, "analyze.html", parameters)
    
    # for making uppercase
    elif Uppercase=="on":
        UpperCase=""
        for char in Text:
            UpperCase= UpperCase+ char.upper()
        save=UpperCase
        print(save)
        parameters={'operation': "Uppercasing", 'Analyzed_text':UpperCase}
        return render(request, "analyze.html", parameters)
    
    # for making lowercase
    elif Lowercase =="on":
        LowerCase =Text.lower()
        save=LowerCase
        parameters={'operation': "Lowercasing", 'Analyzed_text':LowerCase}
        return render(request, "analyze.html", parameters)
    
    # for removing extra spaces
    elif extraspace =="on":
        spaceremoved=""
        for index, char in enumerate (Text):
            if not(Text[index]== " " and Text[index+1]==" "):
                spaceremoved = spaceremoved + char
        save=spaceremoved
        parameters={'operation': "Removing Extra Spaces", 'Analyzed_text':spaceremoved}
        return render(request, "analyze.html", parameters)
    
    # for words counting
    elif Wordscount=="on":
        spaceremoved=""
        for index, char in enumerate (Text):
            if not(Text[index]== " " and Text[index+1]==" "):
                spaceremoved = spaceremoved + char
        wordscount=len(spaceremoved.split())
        save=wordscount
        parameters={'operation': "Counting Words", 'Analyzed_text': wordscount}
        return render(request, "analyze.html", parameters)
    
        
    else:
        return HttpResponse("Something went wrong!")
    # Title = Text.title()
    # Uppercase = Text.upper()
    # Lowercase = Text.lower()
    # Length = len(Text)
    # Text = "" 
    # para={"Title": Title, "Uppercase": Uppercase, "Lowercase": Lowercase, "Length": Length}
    # return render(request, 'index.html', para)

