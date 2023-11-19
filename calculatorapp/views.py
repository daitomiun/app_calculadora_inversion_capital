from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '../templates/home.html')


def result(request):
    num1 = int(request.GET.get('number1'))
    percentage = int(request.GET.get('percentage'))


    if request.GET.get('multiply') == "":
        ans = num1 * percentage / 100

    return render(request, 'result.html', {'ans': ans})



