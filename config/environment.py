from decouple import config, Choices
import os

# App global settings
BASE_URL = config('BASE_URL', None)

SECRET_KEY = os.getenv('SECRET_KEY', "8BYkEfBA6O6donzWlSihBXox7C0sKR6b")

ENVIRONMENT = {
    'APP_ENV': config('APP_ENV', None),
    'DEBUG': config('DEBUG', False),
    'TIMEZONE': config('TIMEZONE', 'America/Bogota'),
}
# Database settings
POSTGRES = {
    'URI': config('POSTGRES_URI', None)
}

# Redis settings
REDIS = config('REDIS_HOST', None)

# Mailer settings
MAILER = {
    'HOST': config('SMTP_HOST', None),
    'PORT': config('SMTP_PORT', None, cast=int),
    'USERNAME': config('SMTP_USERNAME', None),
    'PASSWORD': config('SMTP_PASSWORD', None),
    'TIMEOUT': config('SMTP_TIMEOUT', 10, cast=int)
}
# Email token settings
EMAIL_SALT_KEY = os.getenv(
    'EMAIL_SALT_KEY', "ZqH61Ht1WgFQCRpDVITf4yNy8i7F3tUm")

EMAIL_TOKEN_EXPIRE_SECONDS = config(
    'EMAIL_TOKEN_EXPIRE_SECONDS', 3600, cast=int)

# JWT settings

# JWT secrets
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', "IBQj^J9(HEAf#v0l'dvsdK3JcM4*ET")

JWT_REFRESH_SECRET_KEY = os.getenv(
    'JWT_REFRESH_SECRET_KEY', 'SKvCiYJh2A9zhsEWi6iGeF89H4F19eOM')

# JWT Expiration

# Access token expiration - Default 30 minutes
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = config(
    'JWT_ACCESS_TOKEN_EXPIRE_MINUTES', 30, cast=int)
# Refresh token expiration - Default 7 days
JWT_REFRESH_TOKEN_EXPIRE_MINUTES = config(
    'JWT_REFRESH_TOKEN_EXPIRE_MINUTES', 60 * 24 * 7, cast=int)

# JWT Algorithm
JWT_ALGORITHM = config('JWT_ALGORITHM', "HS256",
                       cast=Choices(['HS256', 'RS256', 'ES256']))

# Development settings
DEVELOPMENT = {
    'POSTGRES_URI_TEST': config('POSTGRES_URI_TEST', None)
}
