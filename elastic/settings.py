
#pip install django-elasticsearch-dsl

INSTALLED_APPS = [
    'django_elasticsearch_dsl'
]
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://localhost:9200'
    }
}