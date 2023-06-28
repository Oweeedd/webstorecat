from django.shortcuts import render

def error_404_view(request, exception):
    return render(request, 'main/404.html')
def index(request):
    data = {
        'title': 'Добро пожаловать в наш магазин головных уборов',
        'values': ['some', 'helo', '132']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

