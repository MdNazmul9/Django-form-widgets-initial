from django.shortcuts import render
from  .models import Consumer
from .forms import ConsumerForm, RawConsumerForm

def IndexView(request):
    # initial_data = {
    #     "ShopKeperName": str(list(obj.values("first_name").distinct())[0]['first_name'])+" "+str(list(obj.values("last_name").distinct())[0]['last_name']) ,
    #     "ShopKeperCIN": list(obj.values("username").distinct())[0]['username'],
    #     "SenderEmail": list(obj.values("user__email").distinct())[0]['user__email'], 
    # }
    initial_data = {
        'name': 'Nazmul' 
    }
   
    
    form = ConsumerForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        x = Consumer()
        x.name= form.cleaned_data['name']
        x.title = form.cleaned_data['title'] + 'pk'
        x.commission = form.cleaned_data['commission']
        # x.user.add(request.user.id)
        print(request.user.id)
        # form.save()
        x.save()
        
        form = ConsumerForm(initial=initial_data)
        
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'index.html', context)




# def IndexView(request):
#     form = RawConsumerForm()
#     if request.method == "POST":
#         form = RawConsumerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = RawConsumerForm()


#         #SendingInfo.objects.create(**my_form.cleaned_data)
#     else:
#         print(form.errors)

#     context = {
#         'form': form
#     }
#     return render(request, 'index.html', context)


# Create your views here.

# def  IndexView(request):
#     form = ConsumerForm(request.POST or None)
#     if request.method == "POST":
#         form = ConsumerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form = ConsumerForm()

#     context = {
#         'form': form
#     }

#     return (request, 'index.html', context)


# def infoCreate(request):
#     form = SendingInfoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = SendingInfoForm()

#     context = {
#         "form": form
#     }
#     return render(request, "Createinfo.html", context)
