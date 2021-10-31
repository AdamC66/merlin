from apps.merlin_user.models import MerlinUser

class InvalidPasswordException(Exception):
    pass

def create_user(username, email, password, confirm_password):
    if password != confirm_password:
        raise InvalidPasswordException
    return MerlinUser.objects.create(
        username=username,
        email=email,
        password=password
    )