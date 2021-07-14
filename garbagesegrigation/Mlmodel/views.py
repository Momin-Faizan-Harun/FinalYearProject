from django.shortcuts import render

# Create your views here.
def predictimage(request):
    context = {'a':1}
    print(request)
    print(request.POST.dict())
    return render(request,'handler.html',context)