from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    # title = forms.CharField(widget=forms.Textarea, label='标题', required=False)
