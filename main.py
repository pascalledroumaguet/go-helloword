"""
Main module
"""
from router import router_base

app = router_base.get_router()


# for production conf
# allow_origins = ['client-facing-example-app.com', 'localhost:5000']
