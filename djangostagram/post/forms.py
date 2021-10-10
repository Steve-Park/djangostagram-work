from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=256, label='제목', error_messages={
        'required': '제목을 입력하여 주십시오.'
    })
    content = forms.CharField(widget=forms.Textarea, label='내용', error_messages={
        'required': '내용을 입력하여 주십시오.'
    })
    imageurl = forms.URLField(label='이미지 주소', error_messages={
        'required': '이미지 주소를 입력하여 주십시오.'
    })
    tags = forms.CharField(label='태그', required=False)
