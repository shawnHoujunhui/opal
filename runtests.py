"""
Standalone test runner for OPAL plugin
"""
import os
import sys

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   OPAL_OPTIONS_MODULE = 'opal.tests.dummy_options_module',
                   ROOT_URLCONF='opal.urls',
                   INTEGRATING=False,
                   DEFAULT_DOMAIN='localhost',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'opal',
                                   'opal.tests'
                               ))

from opal.tests import dummy_options_module
from opal.tests import dummy_opal_application

from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['opal', ])
if failures:
    sys.exit(failures)
