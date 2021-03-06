from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.forms import Form
from django.db.transaction import atomic
from accounts.models import Profile


class SubmittableForm(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass


class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass


class SignUpForm(SubmittableForm, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        profile = Profile(user=result)
        if commit:
            profile.save()
        return result