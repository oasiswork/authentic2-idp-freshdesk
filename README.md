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


### Diverting some users to somewhere else

You may need to authorize freshdesk access only for a subset of your users,
willing to redirect others to a custom URL (ex: custom error page). There is the
`FRESHDESK_DIVERT` setting for that.

    you should point it to an object instance with two methods :
    should_divert(email) and divert_url(email), for ex:

    class TestDiverter():
        def should_divert(self, user):
            """
            :returns True if the user should be diverted out of FD false else
            if user.email == 'foobar@example.com':
                return True
            else:
                return False

        def divert_url(self, user, request):
            """
            :returns an url, the diversion path, the system will HTTP 302 there.
            """
            return 'http://example.com/{}'.format(user.email)

And in your `local_settings.py`

    FRESHDESK_DIVERT='mymodule.TestDiverter'
