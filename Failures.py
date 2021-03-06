# ------------------------------------------------------------------------------
#  Copyright (c) 2019 Parallax Inc.                                            -
#                                                                              -
#  Permission is hereby granted, free of charge, to any person obtaining       -
#  a copy of this software and associated documentation files (the             -
#  “Software”), to deal in the Software without restriction, including         -
#  without limitation the rights to use, copy,  modify, merge, publish,        -
#  distribute, sublicense, and/or sell copies of the Software, and to          -
#  permit persons to whom the Software is furnished to do so, subject          -
#  to the following conditions:                                                -
#                                                                              -
#     The above copyright notice and this permission notice shall be           -
#     included in all copies or substantial portions of the Software.          -
#                                                                              -
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,             -
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF          -
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFINGEMENT.       -
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY        -
#  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,        -
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE           -
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                      -
#                                                                              -
#                                                                              -
# ------------------------------------------------------------------------------

import logging
'''
Failure messages

These functions provide for a standard return message for all known
and expected error conditions.

The return payload is a JSON document and an HTTP error code. The JSON
document includes these elements:

    success - boolean
    message - a short message that uniquely identifies the error
    code    - a distrinct return code that allows the client to act on
              then specic error condition encountered.
    field   - optional data element that identified the name of the
              data element involved in the error.
    data    - optional data element that provides an id or key value
              for the data set being processed when the error occurred.
   
The HTTP error code indicates whether the request succeeded or failed. If
the call is successful, the service will return a code 200 and a message
of "OK".

If the request is unsuccessful and the error is due to faulty client data,
return an HTTP error code of 401 if the user is unknown or authentication fails.
Return an HTTP 500 error if the failure is due to an issue within the server,
such as unable to access the back-end database.
             
'''


def unknown_user_id(id_user):
    logging.debug('Failures: Unknown user id: %s', id_user)
    return {
        'success': False,
        'message': 'Unknown user',
        'code': 400,
        'data': id_user
        }, 404


def unknown_user_email(email):
    logging.debug('Failures: Unknown user email: %s', email)
    return {
        'success': False,
        'message': 'Unknown user',
        'code': 400,
        'data': email
        }, 404


def unknown_user_screen_name(screen_name):
    logging.debug('Failures: Unknown user by screen name: %s', screen_name)
    return {
        'success': False,
        'message': 'Unknown user screen name',
        'code': 400,
        'data': screen_name
        }, 404


def email_already_in_use(email):
    logging.debug('Failures: Email already in use: %s', email)
    return {
        'success': False,
        'message': 'Email already in use',
        'code': 450,
        'data': email
        }, 400


def email_not_confirmed(email):
    logging.debug('Failures: Email %s not confirmed', email)
    return {
        'success': False,
        'message': 'Email not confirmed',
        'code': 430,
        'data': email
        }, 401


def user_blocked(email):
    logging.debug('Failures: User %s blocked', email)
    return {
        'success': False,
        'message': 'User is blocked',
        'code': 420,
        'data': email
        }, 403


def not_a_number(field, value):
    logging.error('Failures: Not a valid number: %s -> %s', field, value)
    return {
        'success': False,
        'message': 'Not a valid number',
        'code': 310,
        'field': field,
        'value': value
        }, 400


def passwords_do_not_match():
    logging.debug('Failures: Passwords do not match')
    return {
        'success': False,
        'message': "Password confirm doesn't match",
        'code': 460
        }, 400


def password_complexity():
    logging.debug('Failures: Password is not complex enough')
    return {
        'success': False,
        'message': "Password is not complex enough",
        'code': 490
        }, 400


def screen_name_already_in_use(screen_name):
    logging.debug('Failures: Screen name already in use: %s', screen_name)
    return {
        'success': False,
        'message': "Screenname already in use",
        'code': 500,
        'data': screen_name
        }, 400


def rate_exceeded(time):
    """
      Service requested to frequently.

      time - string representing the date and time the service will be available again
    """
    logging.debug('Failures: Rate exceeded')
    return {
        'success': False,
        'message': 'Insufficient bucket tokens',
        'code': 470,
        'data': time
        }, 400


def wrong_password(email):
    logging.debug('Failures: Wrong password for %s', email)
    return {
        'success': False,
        'message': 'Wrong password',
        'code': 410,
        'data': email
           }, 401


def password_unknown_format(fault_message):
    logging.debug('Failures: %s', fault_message)
    return {
               'success': False,
               'message': 'Unencoded Unicode password',
               'code': 475,
               'data': fault_message
           }, 500


def unknown_bucket_type(bucket_type):
    logging.debug('Failures: Unknown bucket type: %s', bucket_type)
    return {
        'success': False,
        'message': 'Unknown bucket type',
        'code': 180,
        'data': bucket_type
        }, 400


def wrong_auth_source(auth_source):
    logging.debug('Failures: Wrong auth source: %s', auth_source)
    return {
        'success': False,
        'message': 'Wrong auth source',
        'code': 480,
        'data': auth_source
        }, 500

