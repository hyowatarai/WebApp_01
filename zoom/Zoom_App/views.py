from email.mime import application
from django import forms
from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView
from django.views.generic import ListView
from . import models
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponse
from .application import zoom_main
from .application.zoom_main import task0
from django.db.models import Q

# Create your views here.
class FormView(TemplateView):

    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                        "form":forms.Contact_Form(),
        }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "App_Folder_HTML/form.html",context=self.params)

    # #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)

            #フォーム入力が有効な場合
            if self.params["form"].is_valid():
                #入力項目をデータベースに保存
                self.params["form"].save(commit=True)
                self.params["Message"] = "入力項目が送信されました。"

            return render(request, "App_Folder_HTML/form.html",context=self.params)


            

class LessonList(ListView):
    model = models.Lesson
    
    context_object_name = "lesson_list"
    
    template_name = "App_Folder_HTML/Lesson_list.html"


    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = models.Lesson.objects.filter(
                Q(Name__icontains=q_word) | Q(Week__icontains=q_word))
        else:
            object_list = models.Lesson.objects.all()
        return object_list.order_by("Name")


class Form2(DetailView):

    model = models.Lesson

    context_object_name = "lesson_form2"

    template_name = "App_Folder_HTML/form2.html"

class Update(UpdateView):
    
    model = models.Lesson

    fields = ["Name", "Week", "Nyu", "Password", "Url"]

    template_name = "App_Folder_HTML/Lesson_update.html"

    success_url = "/"

    
    def get_form(self):
        form = super(Update, self).get_form()
        form.fields['Name'].label = '名前'
        form.fields['Week'].label = '曜日'
        form.fields['Nyu'].label = 'ID'
        form.fields['Password'].label = 'パスワード'
        form.fields['Url'].label = 'URL'
        return form

class DeleteView(DeleteView):

    template_name = "App_Folder_HTML/Lesson_delete.html"

    model = models.Lesson

    success_url = "/"

def zoom_main(request):

    template_name = "App_Folder_HTML/form2.html"

    if request.POST:

        name = request.POST[models.Lesson.Nyu]
        password = request.POST[models.Lesson.Password]

        return render(request, "App_Folder_HTML/form2.html")


def zoom(req):
    if req.method == 'GET':
        # ajaxで送信したデータのうち"input_data"を指定して取得する。
        task0(req.GET.get("data1"), req.GET.get("data2"))

        return HttpResponse()


        