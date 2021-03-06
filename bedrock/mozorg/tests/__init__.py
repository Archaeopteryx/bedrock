# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from contextlib import contextmanager

from django.test import TestCase

import test_utils
from bedrock.base.urlresolvers import (get_url_prefix, Prefixer, set_url_prefix)
from lib.l10n_utils import translation


class TestCase(TestCase):
    """Base class for Bedrock test cases."""
    def shortDescription(self):
        # Stop nose using the test docstring and instead the test method name.
        pass

    @contextmanager
    def activate(self, locale):
        """Context manager that temporarily activates a locale."""
        old_prefix = get_url_prefix()
        old_locale = translation.get_language()
        rf = test_utils.RequestFactory()
        set_url_prefix(Prefixer(rf.get('/%s/' % (locale,))))
        translation.activate(locale)
        yield
        set_url_prefix(old_prefix)
        translation.activate(old_locale)
