from django import forms


class VideoForm(forms.Form):
    title = forms.CharField(max_length=100, label="Video Title")
