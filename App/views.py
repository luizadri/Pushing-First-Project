from decimal import Decimal
from django.shortcuts import render

# Create your views here.

def HomePage(request):

    return render(request,'Home.html')

# def Sum(request):
#     if request.method=='POST':
#         num1 = Decimal(request.POST['number1'])
#         num2 = Decimal(request.POST['number2'])

#         result = num1 + num2

#         return render(request,'Result.html',{'r':result})



# def Sum(request):
#     if request.method=='POST':
#         number1 = request.POST.get('number1','')
#         number2 = request.POST.get('number2','')

#         if not number1 or not number2:
#             return render(request,'Error.html')
        
#         num1 = Decimal(number1)
#         num2 = Decimal(number2)

#         result = num1+num2

#         return render(request, 'Result.html',{'r':result})
    
#     else:
#         return render(request,'Error.html')


def Sum(request):

    if request.method == 'POST':

        try:
            num1 = Decimal(request.POST['number1'])
            num2 = Decimal(request.POST['number2'])

            result = num1 + num2
            

            return render(request,'Result.html',{'r':result})
        
        except:
            return render(request,'Error.html')