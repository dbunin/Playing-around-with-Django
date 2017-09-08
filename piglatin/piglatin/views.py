from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def translate(request):
    original = request.GET['originalText']
    newString = ''
    for word in original.split():
        if word[0].lower() in ['a', 'e', 'i', 'o', 'y' 'u']:
            # vowel
            newWord = word + 'yay'
            newString += ' ' + newWord
        else:
            # consonant
            newWord = word[1:] + word[0] + 'ay'
            newString += ' ' + newWord
    return render(request, 'translate.html',
                  {'original': original, 'translation': newString})


def about(request):
    return render(request, 'about.html')
