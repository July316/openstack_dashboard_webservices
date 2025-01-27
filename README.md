openstack_dashboard_webservices
===============================

A reusable django webservices app for openstack dashboard.

How to install
==============

1. Clone this app into your django project as an app.
2. Update your django project settings.py to add openstack_dashboard_webservices app.
3. Update your django project urls.py to serve the webservice requests.
4. Restart your django server.

settings.py 
===========
```python
INSTALLED_APPS = (
    'openstack_dashboard',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'horizon',
    'horizon.dashboards.nova',
    'horizon.dashboards.syspanel',
    'horizon.dashboards.settings',
    'openstack_dashboard_webservices', #Added here
)
```

urls.py
=======
```python
urlpatterns = patterns('',
    url(r'^$', 'openstack_dashboard.views.splash', name='splash'),
    url(r'^qunit/$', 'openstack_dashboard.views.qunit_tests', name='qunit_tests'),
    url(r'^soap/','openstack_dashboard_webservices.views.soap_services', name='soap_services'), #Added here
    url(r'', include(horizon.urls)))
```

Test
====
wsdl: 
```python
http://yourhost/soap/?wsdl
```
rpc: 
```python
http://yourhost/soap/get_user?userid=1&username=Tom
```
soap:
```python
from suds.client import Client
client = Client(url='http://yourhost/soap/?wsdl')
print client
print client.service.get_user(userid=1, username='Tom')
```



