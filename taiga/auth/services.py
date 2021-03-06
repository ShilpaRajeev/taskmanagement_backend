"""
This module contains a domain logic for authentication
process. It called services because in DDD says it.
"""

from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import transaction as tx
from django.db import IntegrityError
from django.utils.translation import ugettext as _

from taiga.base import exceptions as exc
from taiga.base.mails import mail_builder
from taiga.users.serializers import UserAdminSerializer
from taiga.users.services import get_and_validate_user

from .tokens import get_token_for_user
from .signals import user_registered as user_registered_signal

auth_plugins = {}


def register_auth_plugin(name, login_func):
    auth_plugins[name] = {
        "login_func": login_func,
    }


def get_auth_plugins():
    return auth_plugins


def send_register_email(user) -> bool:
    """
    Given a user, send register welcome email
    message to specified user.
    """
    cancel_token = get_token_for_user(user, "cancel_account")
    context = {"user": user, "cancel_token": cancel_token}
    email = mail_builder.registered_user(user, context)
    return bool(email.send())


def is_user_already_registered(*, username:str, email:str) -> (bool, str):
    """
    Checks if a specified user is already registred.

    Returns a tuple containing a boolean value that indicates if the user exists
    and in case he does whats the duplicated attribute
    """

    user_model = get_user_model()
    if user_model.objects.filter(username=username):
        return (True, _("Username is already in use."))

    if user_model.objects.filter(email=email):
        return (True, _("Email is already in use."))

    return (False, None)


def get_membership_by_token(token:str):
    """
    Given a token, returns a membership instance
    that matches with specified token.

    If not matches with any membership NotFound exception
    is raised.
    """
    membership_model = apps.get_model("projects", "Membership")
    qs = membership_model.objects.filter(token=token)
    if len(qs) == 0:
        raise exc.NotFound(_("Token does not match any valid invitation."))
    return qs[0]


@tx.atomic
def public_register(username:str, password:str, email:str, full_name:str):
    """
    Given a parsed parameters, try register a new user
    knowing that it follows a public register flow.

    This can raise `exc.IntegrityError` exceptions in
    case of conflics found.

    :returns: User
    """

    is_registered, reason = is_user_already_registered(username=username, email=email)
    if is_registered:
        raise exc.WrongArguments(reason)

    user_model = get_user_model()
    user = user_model(username=username,
                      email=email,
                      full_name=full_name,
                      read_new_terms=True)
    user.set_password(password)
    try:
        user.save()
    except IntegrityError:
        raise exc.WrongArguments(_("User is already registered."))

    send_register_email(user)
    user_registered_signal.send(sender=user.__class__, user=user)
    return user


@tx.atomic
def accept_invitation_by_existing_user(token:str, user_id:int):
    user_model = get_user_model()
    user = user_model.objects.get(id=user_id)
    membership = get_membership_by_token(token)

    try:
        membership.user = user
        membership.save(update_fields=["user"])
    except IntegrityError:
        raise exc.IntegrityError(_("This user is already a member of the project."))
    return user


@tx.atomic
def private_register_for_new_user(token:str, username:str, email:str,
                                  full_name:str, password:str):
    """
    Given a inviation token, try register new user matching
    the invitation token.
    """
    is_registered, reason = is_user_already_registered(username=username, email=email)
    if is_registered:
        raise exc.WrongArguments(reason)

    user_model = get_user_model()
    user = user_model(username=username,
                      email=email,
                      full_name=full_name)

    user.set_password(password)
    try:
        user.save()
    except IntegrityError:
        raise exc.WrongArguments(_("Error while creating new user."))

    membership = get_membership_by_token(token)
    membership.user = user
    membership.save(update_fields=["user"])
    send_register_email(user)
    user_registered_signal.send(sender=user.__class__, user=user)

    return user


def make_auth_response_data(user) -> dict:
    """
    Given a domain and user, creates data structure
    using python dict containing a representation
    of the logged user.
    """
    serializer = UserAdminSerializer(user)
    data = dict(serializer.data)
    data["auth_token"] = get_token_for_user(user, "authentication")
    return data


def normal_login_func(request):
    username = request.DATA.get('username', None)
    password = request.DATA.get('password', None)

    user = get_and_validate_user(username=username, password=password)
    data = make_auth_response_data(user)
    return data


register_auth_plugin("normal", normal_login_func)
