from worldpay_python_example_app.settings.base import *

WORLDPAY_SERVICE_KEY = os.environ.get("WORLDPAY_SERVICE_KEY", 'e0e1db6fa2d205b0a755e2284c0d87fa')
WORLDPAY_ORDERS_URL = os.environ.get("WORLDPAY_ORDERS_URL", "https://api.worldpay.com/v1/orders")
