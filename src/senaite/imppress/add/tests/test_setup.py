# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from senaite.imppress.add.testing import SENAITE_IMPPRESS_ADD_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that senaite.imppress.add is properly installed."""

    layer = SENAITE_IMPPRESS_ADD_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if senaite.imppress.add is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'senaite.imppress.add'))

    def test_browserlayer(self):
        """Test that ISenaiteImppressAddLayer is registered."""
        from senaite.imppress.add.interfaces import (
            ISenaiteImppressAddLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ISenaiteImppressAddLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SENAITE_IMPPRESS_ADD_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['senaite.imppress.add'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if senaite.imppress.add is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'senaite.imppress.add'))

    def test_browserlayer_removed(self):
        """Test that ISenaiteImppressAddLayer is removed."""
        from senaite.imppress.add.interfaces import \
            ISenaiteImppressAddLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ISenaiteImppressAddLayer,
            utils.registered_layers())
