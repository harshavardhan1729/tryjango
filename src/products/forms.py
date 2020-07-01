from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title=forms.CharField(required=False)
    description=forms.CharField(label='desc',widget=forms.Textarea(
            attrs={
                "class":"new - calss",
                "rows":20,
                "cols":100,
            }
    ))
    price=forms.DecimalField(initial=12.5)
    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price'
        ]
#     def clean_title(self,*args,**kwrgs):
#         title=self.cleaned_data.get("title")
#         if "Harsha" not  in title:
#            raise forms.ValidationError("This is not a valid tite")

#         return title  
# def clean_title(self,*args,**kwrgs):
#         email=self.cleaned_data.get("email")
#         if  not  email.endsawith("com"):
#            raise forms.ValidationError("This is not a valid tite")
#         return email

class RawProductForm(forms.Form):
    title=forms.CharField(required=False)
    description=forms.CharField(label='desc',widget=forms.Textarea(
            attrs={
                "class":"new - calss",
                "rows":20,
                "cols":100,
            }
    ))
    price=forms.DecimalField(initial=12.5)