from django import forms
from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView
from django.views.generic import ListView
from . import models
from django.views.generic import DetailView


# Create your views here.
class FormView(TemplateView):

    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                        "form":forms.Contact_Form(),
        }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "App_Folder_HTML/form.html",context=self.params)

    #POST時の処理を記載
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
    # Companyテーブル連携
    model = models.Lesson
    
    # レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "lesson_list"
    
    # テンプレートファイル連携
    template_name = "App_Folder_HTML/Lesson_list.html"


class Form2(DetailView):

    model = models.Lesson

    context_object_name = "lesson_form2"

    template_name = "App_Folder_HTML/form2.html"

    
