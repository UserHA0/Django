from django.urls import path
from sales.views import listorders, listcustomers

urlpatterns = [
    path('orders/', listorders),  # 前面是URL，后面是转向的具体执行函数
    path('customers/', listcustomers)
]