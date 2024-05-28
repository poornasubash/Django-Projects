from django import forms
from.models import booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class booking_from(forms.modelform):
    class meta:
        model=booking
        fields="_all_"
    
    def __init__ (self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper =formhelper(self)
        self.helper.layout=layout(
            submit("advance_payment",css_class='button white btn-block btn-primary')
        )