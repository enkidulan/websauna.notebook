"""An example py.test functional test case."""

import transaction
import time
from sqlalchemy.orm.session import Session
from splinter.driver import DriverAPI

from websauna.tests.utils import create_user
from websauna.tests.utils import EMAIL
from websauna.tests.utils import PASSWORD, create_logged_in_user


def test_context_sensitive_shell(web_server, browser, dbsession, init):
    """See we can open a context sensitive shell in admin."""

    b = browser
    create_logged_in_user(dbsession, init.config.registry, web_server, browser, admin=True)

    b.find_by_css("#nav-admin").click()
    b.find_by_css("#latest-user-shortcut").click()
    b.find_by_css("#btn-crud-shell").click()

    # Ramping up shell takes some extended time
    time.sleep(5)

    # We succesfully exposed obj
    assert b.is_text_present("example@example.com")

    b.find_by_css("#pyramid_notebook_shutdown").click()

    # Back to home screen
    assert b.is_element_visible_by_css("#nav-logout")
