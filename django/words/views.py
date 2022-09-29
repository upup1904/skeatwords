from django.shortcuts import render
from django.http import HttpResponse

from . import models
from .models import SkeatEntry
from . import settings as words_settings

def index(request):
    return render(request, "words/skeat_landing.html", {})


def nearest_word(sought):
    all_words = models.SkeatEntry.objects.all()
    after = all_words.filter(word__gt=sought).order_by('word', 'page_number').first()
    before = all_words.filter(word__lt=sought).order_by('-word', '-page_number').first()
    return dict(preceding_word=before.word, preceding_page=before.page_number,
                following_word=after.word, following_page=after.page_number)


def words_on_page(request, page_number=5):
    qset = SkeatEntry.objects.filter(page_number=page_number)
    if not qset:
        return f"<span class='empty-page'>No words on page {page_number}</span>"
    
    words = [entry.word for entry in qset]
    wordlist = [f"<LI>{w}</LI>" for w in words]
    retval = f"<UL>{''.join(wordlist)}</UL>"
    return HttpResponse(retval)


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
        page_number = int(bounds['preceding_page'])
        img_url = img_url_for_page(page_number)
        context = dict(page_url=img_url,
                       sought=sought,
                       page_number=page_number)
        return render(request, 'words/not_found_one_candidate_page.html', context)
    else:
        return render(request, 'words/not_found_multi_candidate_pages.html', bounds)
  
def img_url_for_page(page_number: int):
    return words_settings.WEBP_TEMPLATE.format(page_number=page_number)

def cropper_demo(request):
    return render(request, "words/demo.html", {})

def look(request):
    return render(request, "words/onepic.html", {'pic': f"{words_settings.WEBP_TEMPLATE}/skeat_642.png"})
    



