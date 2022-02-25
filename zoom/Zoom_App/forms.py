from django import forms
from .models import Lesson

class Contact_Form(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = Lesson
        
        #②表示するモデルクラスのフィールドを定義
        fields = ('Name', 'Week', 'Nyu', 'Password', 'Url')

        #③表示ラベルを定義
        labels = {
            'Name':"授業名",
            'Week':"曜日",
            'Nyu':"ID",
            'Password':"パスワード",
            'Url':"URL",
        }