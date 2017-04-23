import os
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/Data/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)