from cryptography.fernet import Fernet
from django.conf import settings
from django.db import models


class TokenBaseModel(models.Model):
    class Meta:
        abstract = True

    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    _access_token = models.TextField(null=True, blank=True, default=None)
    _refresh_token = models.TextField(null=True, blank=True, default=None)
    expiry_date = models.DateTimeField(null=True, blank=True, default=None)

    def _decrypt_token(self, token: str) -> str:
        f = Fernet(settings.ECOM_ENCRYPTION_KEY)
        return f.decrypt(token.encode()).decode()

    def _encrypt_token(self, token: str) -> str:
        f = Fernet(settings.ECOM_ENCRYPTION_KEY)
        return f.encrypt(token.encode()).decode()

    @property
    def access_token(self) -> str:
        if not self._access_token:
            raise ValueError("Access token is unset.")
        return self._decrypt_token(self._access_token)

    @access_token.setter
    def access_token(self, value: str) -> None:
        self._access_token = self._encrypt_token(value)

    @property
    def refresh_token(self) -> str:
        if not self._refresh_token:
            raise ValueError("Refresh token is unset.")
        return self._decrypt_token(self._refresh_token)

    @refresh_token.setter
    def refresh_token(self, value: str) -> None:
        self._refresh_token = self._encrypt_token(value)


class SquareToken(TokenBaseModel):
    company_id = models.CharField(max_length=128)
