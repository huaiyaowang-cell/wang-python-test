from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def user_list(request):
    # 返回用户列表的静态测试数据
    users = [
        {"id": 1, "name": "张三", "age": 25, "email": "zhangsan@example.com"},
        {"id": 2, "name": "李四", "age": 30, "email": "lisi@example.com"},
        {"id": 3, "name": "王五", "age": 28, "email": "wangwu@example.com"}
    ]
    return JsonResponse(users, safe=False, json_dumps_params={'ensure_ascii': False})


def product_list(request):
    # 返回产品列表的静态测试数据
    products = [
        {"id": 1, "name": "笔记本电脑", "price": 5999, "category": "电子产品"},
        {"id": 2, "name": "手机", "price": 3999, "category": "电子产品"},
        {"id": 3, "name": "平板电脑", "price": 2999, "category": "电子产品"},
        {"id": 4, "name": "无线耳机", "price": 999, "category": "配件"}
    ]
    return JsonResponse(products, safe=False, json_dumps_params={'ensure_ascii': False})
