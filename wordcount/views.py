from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def aboutme(request):
    return render(request, 'about.html')
    
def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_word = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist),
                                            'sorted':sorted_word})  