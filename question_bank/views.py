from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# 导入数据模型ArticlePost
from .models import essay,Tag
from django.db.models import Q


def essay_question_list(request):
    # 取出所有博客文章
    # questions = essay.objects.all()
    # context = { 'questions': questions }
    # # render函数：载入模板，并返回context对象
    # return render(request, 'essay/list1.html', context)

    questions_list = essay.objects.all()
    paginator = Paginator(questions_list, 20)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    context = {'questions': questions}
    # render函数：载入模板，并返回context对象
    return render(request, 'essay/list1.html', context)


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'essay/list1.html', {'error_msg': error_msg})

    questions = essay.objects.filter(Q(title__icontains=q) | Q(answer__icontains=q))
    return render(request, 'essay/list1.html', {'error_msg': error_msg,
                                                'questions': questions})


def tag(request,tag):
    questions_list = essay.objects.filter(tags__name=tag)#通过文章标签进行查询文章
    paginator = Paginator(questions_list, 20)
    page = request.GET.get('page')
    questions = paginator.get_page(page)

    tname = Tag.objects.get(name=tag)#获取当前搜索的标签名
    # page = request.GET.get('page')
    tags = Tag.objects.all()
    # paginator = Paginator(list, 5)
    # try:
    #     list = paginator.page(page)  # 获取当前页码的记录
    # except PageNotAnInteger:
    #     list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    # except EmptyPage:
    #     list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())
