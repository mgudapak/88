# File contains most of the configuration variables that your app needs.
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True


# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
