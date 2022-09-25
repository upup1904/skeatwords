from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    return render(request, "words/skeat_landing.html", {})


def nearest_word(sought):
    all_words = models.SkeatEntry.objects.all()
    after = all_words.filter(word__gt=sought).order_by('word', 'page_number').first()
    before = all_words.filter(word__lt=sought).order_by('-word', '-page_number').first()
    return dict(preceding_word=before.word, preceding_page=before.page_number,
                following_word=after.word, following_page=after.page_number)


def search_for_one_word(request):
    sought = request.GET['sought']
    word_qset = models.SkeatEntry.objects.filter(word__iexact=sought)
    if word_qset:
       if len(word_qset)  == 1:
           return HttpResponse(f"Page: {word_qset.first().page_number}")
       else:
           pages = [str(x.page_number) for x in word_qset]
           return HttpResponse(f"Pages: {', '.join(pages)}")
    
    bounds = nearest_word(sought)
    bounds['sought'] = sought
    if bounds['preceding_page'] == bounds['following_page']:
        return render(request, 'words/not_found_one_candidate_page.html', bounds)
    else:
        return render(request, 'words/not_found_multi_candidate_pages.html', bounds)
  


def cropper_demo(request):
    return render(request, "words/demo.html", {})


