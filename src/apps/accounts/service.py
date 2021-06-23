from apps.accounts.models import Account
from db.service import ModelService


class AccountService(ModelService):

    MODEL = Account
