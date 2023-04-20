from apps.common.handlers.base_handler import BaseHandler
from apps.common.querysets.product_queryset import ProductQuerySet


class ProductHandler(BaseHandler):
    queryset_class = ProductQuerySet
