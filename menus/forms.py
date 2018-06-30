from django import forms

from restaurant.models import Restaurant

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
        'restaurant',
        'name',
        'contents',
        'excludes',
        'public',
        ]
    def __init__(self, user=None, *args, **kwargs):
        #print(kwargs.pop['user'])
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(user=user) #.exclude (item__isnull=False)
