# Railway.app Configuration
[build]
builder = "dockerfile"
dockerfile = "Dockerfile"

[deploy]
startCommand = "gunicorn app:app --worker-class=gthread --workers=2 --threads=2"
healthcheckPath = "/health_check"
healthcheckTimeout = 100

[[services]]
name = "postgres"
image = "postgres:15-alpine"
env:
  POSTGRES_DB = "netad_db"
  POSTGRES_USER = "netad_user"
  POSTGRES_PASSWORD = "netad_password"

[env]
FLASK_ENV = "production"
SESSION_COOKIE_SECURE = "True"
IP_RATE_LIMIT = "10 per minute"
