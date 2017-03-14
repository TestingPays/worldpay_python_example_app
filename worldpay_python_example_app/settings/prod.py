from worldpay_python_example_app.settings.base import *

WORLDPAY_SERVICE_KEY = os.environ.get("WORLDPAY_SERVICE_KEY", '')
WORLDPAY_ORDERS_URL = os.environ.get("WORLDPAY_ORDERS_URL", "https://api.worldpay.com/v1/orders")
