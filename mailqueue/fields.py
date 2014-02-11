import re
import six

from south.modelsinspector import add_introspection_rules

from django.core.validators import validate_email
from django.db.models import TextField, SubfieldBase
from django.utils.translation import ugettext as _


add_introspection_rules([], ["^mailqueue\.fields\.EmailsListField"])
class EmailsListField(TextField):
    __metaclass__ = SubfieldBase
    email_separator_re = re.compile(r'\s*,\s*')

    def to_python(self, value):
        if isinstance(value, six.string_types):
            return [x for x in self.email_separator_re.split(value) if x]
        else:
            return list(value)

    def validate(self, value, model_instance):
        super(EmailsListField, self).validate(value, model_instance)

        for email in value:
            validate_email(email)

    def get_prep_value(self, value):
        if isinstance(value, six.string_types):
            return value
        else:
            return ', '.join(value)
