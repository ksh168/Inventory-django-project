#####

# from django_elasticsearch_dsl import (
#     Document, Index, fields
# )
# from .models import Product

# # create index called company
# PUBLISHER_INDEX = Index('company')

# PUBLISHER_INDEX.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )


# @PUBLISHER_INDEX.doc_type
# class ProductDocument(Document):
#     # id = fields.TextField(attr="id")

#     fielddata = True

#     # only searching on product_name
#     product_name = fields.TextField(
#         fields={
#             'raw': {
#                 'type': 'keyword'
#             }
#         }
#     )
#     price = fields.IntegerField()
#     quantity = fields.IntegerField()

#     class Django:
#         model = Product
