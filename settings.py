AUTHENTICATION_BACKENDS = (
    'account.auth_backends.AccountModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

CUSTOM_USER_MODEL = 'account.Account'
