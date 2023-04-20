########################
# Tests of Store API
########################

flake8 --disable-noqa --exclude .venv/,migrations/ --ignore=W291,E711,F401,E402 --max-line-length 120

# Set app environment variable to "testing"
export APP_ENV="testing"

# Tests of users endpoint
python -m unittest tests/api/test_users.py -v
# Tests of products endpoint
python -m unittest tests/api/test_products.py -v
# Tests of orders endpoint
python -m unittest tests/api/test_orders.py -v

# Set app environment variable to "testing"
unset APP_ENV