from django.shortcuts import render,redirect
from . models import Member

# Create your views here.
def index(request):
    members = Member.objects.all()
    return render(request,'index.html',{'members':members})


def create(request):
    member = Member(Firstname=request.POST['Firstname'], Lastname=request.POST['Lastname'])
    member.save()
    return redirect('/')

def edit(request,pk):
    members = Member.objects.get(pk=pk)
    context = {'members': members}
    return render(request, 'edit.html', context)

def update(request, pk):
    member = Member.objects.get(pk=pk)
    member.Firstname = request.POST['Firstname']
    member.Lastname = request.POST['Lastname']
    member.save()
    return redirect('/crud/')

def delete(request,pk):
    member = Member.objects.get(pk=pk)
    member.delete()
    return redirect('/crud/')




