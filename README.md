Authentic2 Freshdesk login
==========================

This plugin allows Authentic2 IDP to log your users to freshdesk through
freshdesk simple SSO mechanism.

Install
-------

You just have to install the package in your virtualenv and relaunch, it will
be automatically loaded by authentic2.

### Freshdesk configuration

- Go to https://yourcompany.freshdesk.com/admin/security
- enable *SSO simple*
- In *Remote login URL* put something like
  `https://myidp.example.com/idp/freshdesk/login/`
- In *Remote logout URL* put something like
  `https://myidp.example.com/idp/logout/`
- Note down the shared secret

### Authentic configuration

Set in your *local_settings.py* the following settings according to your
fresdhesk site.

    FRESHDESK_URL = 'http://yourcompany.freshdesk.com'
    FRESHDESK_SECRET_KEY = 'XXXXXXXXXXXX'