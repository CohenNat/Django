# main/documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Article

@registry.register_document
class ArticleDocument(Document):
    class Index:
        # Nom de l'index Elasticsearch
        name = 'articles'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Article  # Le modèle Django associé

        fields = [
            'title',
            'content',
            'publication_date',
        ]
