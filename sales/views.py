from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from common.models import Customer


def listorders(request):
    return HttpResponse("订单信息！")

# # 不加参数选择
# def listcustomers(request):
#     # 返回一个 QuerySet 对象 ，包含所有的表记录
#     # 每条表记录都是是一个dict对象，
#     # key 是字段名，value 是 字段值
#     qs = Customer.objects.values()
#
#     # 定义返回字符串
#     retStr = ''
#     for customer in qs:
#         for name, value in customer.items():
#             retStr += f'{name} : {value} | '
#
#         # <br> 表示换行
#         retStr += '<br>'
#
#     return HttpResponse(retStr)3



# 添加参数选择
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()
    ph = request.GET.get('phonenumber', None)
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 定义返回字符串
    retStr = ''
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)