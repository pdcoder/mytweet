from django import forms
from django.forms.utils import ErrorList

class FormUserNeededList(self,form):

     def form_valid(self,form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededList, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(['User must be logged in to continue'])
            return self.form_invalid(form)