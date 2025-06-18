from operator import methodcaller
from django import forms
from .models import Reedsdata
from usersettings.models import Checkbox_for_setting


######################################completed###############################
class ViewUser:

    def __init__(self, user):
        self.current_user = user

    def get_field_list(self):
        try:
            data = Checkbox_for_setting.objects.get(user=self.current_user)
            l = data.checkboxsetting
            l = 'reed_ID,' + l + 'evaluation'
            print(l)
            return l
        except Checkbox_for_setting.DoesNotExist:
            return []


class Caneform(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            li = ViewUser(user).get_field_list()
            for field_name in list(self.fields):
                if field_name not in li:
                    self.fields.pop(field_name)

    class Meta:
        model = Reedsdata
        fields = '__all__'


#######################################################
