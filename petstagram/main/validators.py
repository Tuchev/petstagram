from django.core.exceptions import ValidationError


# def always_valid(chars):
#     def validator(value):
#         pass
#
#     return validator


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            # Invalid case
            raise ValidationError('Value must contain only letters')
    # valid case