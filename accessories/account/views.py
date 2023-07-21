from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView
from.forms import RegForm,LogForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LogView(FormView):
    template_name="log.html"
    form_class=LogForm
    def post(self,request):
        fdata=LogForm(data=request.POST)
        if fdata.is_valid():
            uname=fdata.cleaned_data.get("username")
            pswd=fdata.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect("ch")
            else:
                return render(request,"log.html",{"form":fdata})
            

# class LogView(View):
#     def get(self,request):
#         form=LogForm()
#         return render(request,"log.html",{"f":form})
#     def post(self,request):
#         fdata=LogForm(data=request.POST)
#         if fdata.is_valid():
#             uname=fdata.cleaned_data.get("username")
#             pswd=fdata.cleaned_data.get("password")
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 login(request,user)
#                 return redirect("ch")
#             else:
#                 return render(request,"log.html",{"f":fdata})
            
    
# class RegView(View):
#     template_name="reg.html"
#     form_class=RegForm
#     success_url="log"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         fdata=self.form_class(data=request.POST)
#         if fdata.is_valid():
#             fdata.save()
#             return redirect(self.success_url)
#         else:
#             return render(request,self.template_name,{"form":fdata})
        
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    success_url=reverse_lazy("log")
    
class LogOut(View):
    def get(self,request):
        logout(request)
        return redirect("log")
