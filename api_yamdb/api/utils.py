import uuid

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from api_yamdb.settings import EMAIL_ADMIN
from reviews.models import Title, User


class CurrentTitleDefault:
    requires_context = True

    def __call__(self, serializer_field):
        title_id = serializer_field.context['view'].kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title

    def __repr__(self):
        return '%s()' % self.__class__.__name__


def generate_and_send_confirmation_code_to_email(username):
    user = get_object_or_404(User, username=username)
    confirmation_code = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
    user.confirmation_code = confirmation_code
    send_mail(
        'Код подтвержения для завершения регистрации',
        f'Ваш код для получения JWT токена {user.confirmation_code}',
        EMAIL_ADMIN,
        [user.email],
        fail_silently=False,
    )
    user.save()
