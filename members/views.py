
from django.shortcuts import render
from .models import form


def createpost(request):
  if request.method=='POST':
    if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('age') and request.POST.get('email'):
      post=form()
      post.fname=request.POST.get('fname')
    
      post.lname = request.POST.get('lname')
      post.age = request.POST.get('age')
      post.email = request.POST.get('email')
      post.save()
      
      return render(request,'members/index.html')
  else:
     return render(request,'members/index.html')
  return render_to_response('members/index.html',{''})