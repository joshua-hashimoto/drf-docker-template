
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',  # dj_rest_auth & simplejwt
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',  # django_filters
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',  # djangorestframework_camel_case
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',  # djangorestframework_camel_case
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'SEARCH_PARAM': 'search',
    'ORDERING_PARAM': 'ordering',
}
