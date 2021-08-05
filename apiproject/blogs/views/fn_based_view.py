from django.http import JsonResponse
import json

data = [
        {
        'title': 'DIpesh'
    },
    {
        'title': 'Neupane'
    },
    {
        'title': 'rasuwa'
    }
]


def get_blogs(request):
    res = {
        "success": True,
        "message": 'function based view : api to get blog',
        "next": "http://127.0.0.1:8000/blogs1",
        "result" : data[:2],
        }
    return JsonResponse(res)

def create_blogs(request):
    body = json.loads(request.body),
    data.append(body)
    print(body)
    if request.method == 'POST':
        res = {
        'success': True,
        'message': 'function based view : api to create blog',
        'result': body
        }
    else:
        res = {
        'success': False,
        'message': 'function based view : Invalid Input'
        }
    return JsonResponse(res)

def update_blogs(request):
    if request.method == 'PUT':
        res = {
        'success': True,
        'message': 'function based view : api to Update blog'
        }
    else:
        res = {
        'success': False,
        'message': 'function based view : Invalid Input'
        }
    return JsonResponse(res)

def get_blogs1(request):
    res = {
        'success': True,
        'message': 'next page',
        'previos': "http://127.0.0.1:8000/blogs",
        'result': data[2:]
        }
    return JsonResponse(res)

def delete_blog(request):
    data.pop(),
    res = {
        'success': True,
        'message': 'delete',
        'result': data
        }
    return JsonResponse(res)

