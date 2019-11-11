from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
from django.shortcuts import redirect


# Create your views here.
def showbooks(request, sid):
    '''
    详情页
    :param request:
    :param sid:每个id
    :return:
    '''
    cookies=request.COOKIES.get('name')
    print('接受到cookies:',cookies)
    if cookies!='boss1':
        return redirect('showlist')   ## 如果不对跳回列表页
    all_book = models.BOOK.objects.filter(nid=sid).values()


    return HttpResponse(all_book)
def showlist(request):
    '''
    列表
    :param request:
    :return:
    '''
    cookies = models.user1.objects.get(id=1).name
    print('cookies:', cookies)
    list1 =models.BOOK.objects.all()
    response=render( request,'list.html',{
        'list':list1})
    response.set_cookie('name',cookies)   ## 为响应设置cookes值
    print('response',response)

    return response





