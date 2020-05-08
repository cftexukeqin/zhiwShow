from django.shortcuts import render
from apps.front.models import Document
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.conf import settings


# Create your views here.

def index(request):
    return render(request, 'front/index.html')


def search(request):
    search_cat_id = request.GET.get('searchtype')
    words = request.GET.get('words')
    p = request.GET.get('page', 1)
    if search_cat_id == 'title':
        if words:
            print("123dfsafsda")
            documents = Document.objects.filter(title__contains=words).all()
        else:
            print("11111111")
            documents = Document.objects.all()
    elif search_cat_id == 'author':
        cat = "作者"
        documents = Document.objects.filter(author__contains=words).all()
    elif search_cat_id == 'source':
        cat = "出处"
        documents = Document.objects.filter(acticle_source__contains=words).all()
    elif search_cat_id == 'keywords':
        cat = "关键词"
        documents = Document.objects.filter(key_words__contains=words).all()
    elif search_cat_id == 'summary':
        cat = "摘要"
        documents = Document.objects.filter(summary__contains=words).all()
    else:
        documents = Document.objects.all()
    paginator = Paginator(documents, settings.PERPAGE_DOCUMENT_COUNT)

    num_pages = paginator.num_pages
    left_has_more = False
    right_has_more = False
    # 分页所需参数
    new_context = {}
    try:
        goodses = paginator.page(p)
        current_page = goodses.number
        if current_page <= settings.AROUND_COUNT + 2:
            left_pages = range(1, current_page)
            new_context['left_pages'] = left_pages
        else:
            left_has_more = True
            left_pages = range(current_page - settings.AROUND_COUNT, current_page)
            new_context['left_pages'] = left_pages
            new_context['current_page'] = current_page

        if current_page >= num_pages - 2 - 1:
            right_pages = range(current_page + 1, num_pages + 1)
            new_context['right_pages'] = right_pages
            new_context['current_page'] = current_page
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + settings.AROUND_COUNT + 1)
            new_context['right_pages'] = right_pages
            new_context['current_page'] = current_page

    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)


    context = {
        'documents': documents,
        'left_has_more':left_has_more,
        'right_has_more':right_has_more,
        'num_pages':num_pages
    }
    context.update(new_context)
    print(context)
    return render(request, 'front/search.html', context=context)



def list(request):
    documents = Document.objects.all()
    p = request.GET.get('page')
    paginator = Paginator(documents, settings.PERPAGE_DOCUMENT_COUNT)
    num_pages = paginator.num_pages
    left_has_more = False
    right_has_more = False
    # 分页所需参数
    new_context = {}
    try:
        goodses = paginator.page(p)
        current_page = goodses.number
        if current_page <= settings.AROUND_COUNT + 2:
            left_pages = range(1, current_page)
            new_context['left_pages'] = left_pages
        else:
            left_has_more = True
            left_pages = range(current_page - settings.AROUND_COUNT, current_page)
            new_context['left_pages'] = left_pages
            new_context['current_page'] = current_page

        if current_page >= num_pages - 2 - 1:
            right_pages = range(current_page + 1, num_pages + 1)
            new_context['right_pages'] = right_pages
            new_context['current_page'] = current_page
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + settings.AROUND_COUNT + 1)
            new_context['right_pages'] = right_pages
            new_context['current_page'] = current_page

    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)

    context = {
        'documents': documents,
        'left_has_more': left_has_more,
        'right_has_more': right_has_more,
        'num_pages': num_pages
    }
    context.update(new_context)
    print(context)
    return render(request,'front/list.html',context=context)