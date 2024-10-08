# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import warnings


class CallableBool:
    """
    An boolean-like object that is also callable for backwards compatibility.

    Copied from django.utils.deprecation
    """
    do_not_call_in_templates = True

    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value

    def __call__(self):
        warnings.warn(
            "Using user.is_authenticated() and user.is_anonymous() as a method "
            "is deprecated. Remove the parentheses to use it as an attribute.",
            DeprecationWarning, stacklevel=2
        )
        return self.value

    # pylint: disable=nonzero-method
    def __nonzero__(self):  # Python 2 compatibility
        return self.value

    def __repr__(self):
        return 'CallableBool(%r)' % self.value

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __or__(self, other):
        return bool(self.value or other)

    def __hash__(self):
        return hash(self.value)

CallableFalse = CallableBool(False)
CallableTrue = CallableBool(True)
