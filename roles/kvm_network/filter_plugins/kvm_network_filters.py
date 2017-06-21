#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: expandtab:tabstop=4:shiftwidth=4
'''
Custom filters for use in kvm_network role
'''
import re

VIRBR_REGEX = re.compile(r'virbr(\d+)')
ONE_NINE_TWO_REGEX = re.compile(r'192.168.(\d+).\d')

def first_available_virbr(ansible_interfaces):
    dev_nums = [int(VIRBR_REGEX.match(dev).group(1)) for dev in ansible_interfaces if VIRBR_REGEX.match(dev) is not None]
    if dev_nums:
        return 'virbr{}'.format(max(dev_nums) + 1)
    else:
        return 'virbr0'


def next_available_cidr(ansible_all_ipv4_addresses):
    one_nine_twos = [int(ONE_NINE_TWO_REGEX.match(net).group(1)) for net in ansible_all_ipv4_addresses if ONE_NINE_TWOS_REGEX.match(net) is not None]
    if one_nine_twos:
        return '192.168.{}.0/24'.format(max(one_nine_twos) + 1)
    else:
        return '192.168.133.0/24'


class FilterModule(object):
    ''' Custom ansible filters for use by the openshift_master role'''

    def filters(self):
        ''' returns a mapping of filters to methods '''
        return {
            "first_available_virbr": first_available_virbr,
            "next_available_cidr": next_available_cidr
        }
