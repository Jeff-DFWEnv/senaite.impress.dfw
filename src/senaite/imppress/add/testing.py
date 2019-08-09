# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import senaite.imppress.add


class SenaiteImppressAddLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=senaite.imppress.add)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'senaite.imppress.add:default')


SENAITE_IMPPRESS_ADD_FIXTURE = SenaiteImppressAddLayer()


SENAITE_IMPPRESS_ADD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SENAITE_IMPPRESS_ADD_FIXTURE,),
    name='SenaiteImppressAddLayer:IntegrationTesting',
)


SENAITE_IMPPRESS_ADD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SENAITE_IMPPRESS_ADD_FIXTURE,),
    name='SenaiteImppressAddLayer:FunctionalTesting',
)


SENAITE_IMPPRESS_ADD_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SENAITE_IMPPRESS_ADD_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='SenaiteImppressAddLayer:AcceptanceTesting',
)
