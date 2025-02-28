from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CPFBackend(ModelBackend):
    """
    Autentica um usuário usando CPF ao invés de username.
    """
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        try:
            user = User.objects.get(cpf=cpf)
            if user.check_password(password):  # Verifica a senha
                return user
        except User.DoesNotExist:
            return None
