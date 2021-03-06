from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )

def validate_email(value):
    email = value
    if '.edu' in email:
        raise forms.ValidationError("Not a valid email .edu")

CATEGORIES = ['Mexican','Asian']

def validate_category(value):
    cat = value.capitalize()
    if value not in CATEGORIES and cat not in CATEGORIES:
        raise ValidationError(f"{value} not a valid category")
