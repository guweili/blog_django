import os
import sys

if os.environ.get('ENV', None) == 'SERVER':
    from .prd_settings import *
else:
    from .dev_settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

SECRET_KEY = 'fmh+pteoto$zu@j%d6snk_olx48wr#=+x@+5bw+95r$s1+@m^f'

ALLOWED_HOSTS = []

MY_APPS = [
    'my_blog',
]

EXPAND_APPS = [
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = MY_APPS + EXPAND_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog_django.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# 部署项目时用到,收集所有的静态文件并放在一个目录里，即STATIC_ROOT指向的目录里
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 额外的静态文件目录，使用STATICFILES_DIRS，来引导django找到并生成文件放置STATIC_ROOT目录下，（django只识别app下的static文件）
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 上传文件访问根路径
MEDIA_URL = '/media/'

# 指定上传目录的根路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 数据库分库路由
# DATABASE_ROUTERS = [
#     "apps.interface.db_router.MasterSlaveDBRouter",
# ]

LOGGING_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

# 日志配置
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': f'{LOGGING_DIR}/{datetime.now().strftime("%Y-%m-%d")}.log',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }
