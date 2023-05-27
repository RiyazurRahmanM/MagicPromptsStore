from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Prompts

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def sell_view(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        no_of_prompts = request.POST['no_of_prompts']


        return redirect(reverse(sell_cont_view)+f'?title={title}&description={description}&no_of_prompts={no_of_prompts}')
    return render(request,'sell.html')

def sell_cont_view(request):
    title = request.GET.get('title')
    description = request.GET.get('description')
    no_of_prompts = int(request.GET.get('no_of_prompts'))
    prompt = Prompts(title=title,description=description,no_of_prompts=no_of_prompts)
    prompt.save()
    for i in range(1,no_of_prompts+1):
        prompt_field_name = f'prompt{i}'
        prompt_value = request.POST.get(prompt_field_name,'')
        setattr(prompt,prompt_field_name,prompt_value)

        sample_op_input_field_name = f'sample_op_input{i}'
        sample_op_input_value = request.POST.get(sample_op_input_field_name,'')
        setattr(prompt,sample_op_input_field_name,sample_op_input_value)
        prompt.save()
    return render(request,'sell_cont.html')

def find_view(request):
    return render(request,'find.html')

