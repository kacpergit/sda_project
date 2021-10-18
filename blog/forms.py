from django.forms import ModelForm, CharField, Textarea

from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    body = CharField(widget=Textarea, max_length=400)

    def clean_title(self):
        return self.cleaned_data['title'].capitalize()
