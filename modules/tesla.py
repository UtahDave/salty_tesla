# -*- coding: utf-8 -*-
'''
Module for managing a Tesla vehicle
'''
from __future__ import absolute_import, print_function, unicode_literals

# Import python libs
import logging


log = logging.getLogger(__name__)


def __virtual__():
    '''
    Only works on a Tesla vehicle
    '''
    return True
    if is_tesla():
        return True
    #return False, 'This module only runs on a Tesla Vehicle.'
    return False



def is_telsa():
    '''
    Return True if running on a Tesla vehicle,
    Return False if not.
    '''
    # TODO: Figure out how to determine if running on a Telsa
    return True


def ludicrous(status=None):
    '''
    Enable Ludicrous mode
    # todo: figure out how to determine ludicrous mode status

    CLI Example:

    .. code-block:: bash

        salt model3 tesla.ludicrous enable
        salt model3 tesla.ludicrous disable
    '''
    if status is None:
        return 'disabled'
    log.debug('status is: %s', status)
    if 'enable' == status:
        return 'enabled'
    if 'disable' == status:
        return 'disabled'
    # None or some other invalid argument provided
    return 'disabled'
