from django import forms

def validate_of_a(Svalue):
    if Svalue[0].lower()=='a':
        raise forms.validationError("first letter should be a")

def validate_of_length(name):
    if len(name)<=5:
        raise forms.validationError("length is lessthan 5")



class student_from(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_of_a,validate_of_length])
    sage=forms.IntegerField()
    email=forms.EmailField()
    remail=forms.EmailField()
    url=forms.URLField()
    
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']

        if e != re:
            raise forms.ValidationError('email not match ')


    def clean(self):
        u=self.cleaned_data['url']

        if u[-1]=='m':
            raise forms.ValidationError('url error')

    def cleaned_botcatcher(self):
        bot=self.cleaned_data['botcatcher']

        if len(bot)>0:
            raise forms.ValidationError('bot')
