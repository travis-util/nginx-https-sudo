#!/usr/bin/env python

'''Openssl req

'''

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pexpect
import sys

# Note that, for Python 3 compatibility reasons, we are using spawnu and
# importing unicode_literals (above). spawnu accepts Unicode input and
# unicode_literals makes all string literals in this script Unicode by default.
# child = pexpect.spawnu('cadaver http://localhost:8000')
child = pexpect.spawn('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout private/selfsigned.key -out selfsigned.crt')
# child.logfile = sys.stdout
child.logfile_read = sys.stdout
# child.expect('^Country Name .*:$')
child.expect('Country Name .*:$')
child.sendline('')
child.expect('State or Province Name .*:$')
child.sendline('')
child.expect('Locality Name .*:$')
child.sendline('City')
child.expect('Organization Name .*:$')
child.sendline('')
child.expect('Organizational Unit Name .*:$')
child.sendline('Section')
child.expect('Common Name .*:$')
child.sendline('*')
child.expect('Email Address .*:$')
child.sendline('admin@example.org')
# child.expect('dav:!> ')
# child.sendline('help')
child.expect(pexpect.EOF)
child.close()
print(child.exitstatus, child.signalstatus)


# From: https://github.com/travis-util/Self-Signed-SSL-Certificate
