from worldpay_python_example_app.settings.base import *

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]

WORLDPAY_SERVICE_KEY = os.environ.get("WORLDPAY_SERVICE_KEY", 'e0e1db6fa2d205b0a755e2284c0d87fa')
WORLDPAY_ORDERS_URL = os.environ.get("WORLDPAY_ORDERS_URL", "http://localhost:8000/{0}/worldpay/v1/orders".format(WORLDPAY_SERVICE_KEY))
