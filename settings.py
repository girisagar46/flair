#settings.py
import os
# __file__ refers to the file settings.py
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
DATA_STATIC = os.path.join(APP_STATIC, 'data')
DOCUMENT_STATIC = os.path.join(APP_STATIC, 'documents')