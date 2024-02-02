## Installer une application:

* [github page](https://github.com/jazzband/django-debug-toolbar)
* [installation instruction](https://django-debug-toolbar.readthedocs.io/en/stable/installation.html)

    ```bash
    $ pip install django-debug-toolbar
    ```


- Add to `appname/settings.py` file

    ```python
    INSTALLED_APPS = [
        # ...
        'django.contrib.staticfiles',
        'debug_toolbar',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        # ...,
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = ['127.0.0.1']
    ```


- Add to projectname/urls.py:

    ```python
    from django.conf import settings
    from django.conf.urls import include, url
    from django.contrib import admin

    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    ]

    if settings.DEBUG:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    ```
