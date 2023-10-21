# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`cedargrove_dst_adjuster`
================================================================================

A CircuitPython helper to adjust Central European Time (CET) to Central European Summer Time (CEST).

* Author(s): JG, AZ

adjusted from: https://github.com/CedarGroveStudios/CircuitPython_DST_Adjuster.git

Implementation Notes
--------------------
**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

"""

import time

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/azplanlose/CircuitPython_CEST_Adjuster.git"

# pylint: disable=too-many-return-statements
def _detect_dst(datetime):
    """Determines if the Central European Time (CET) input is
    within the Daylight Saving Time window. Input to this function is
    expressed as a structured time object in Standard Time. The function
    returns ``True`` if the datetime object is within the DST window, ``False``
    if the datetime object is outside of the DST window. The helper cannot
    detect DST for a structured time object that was encoded as DST.

    :param structured_time datetime: The Standard Time structured time
    input value. Can be any structured time value within the specified date
    calculation range of CircuitPython, currently January 1, 2000 00:00:00 to
    January 19, 2038 03:14:07. No default value.
    """

    # Fix weekday and yearday structured time errors
    datetime = time.localtime(time.mktime(datetime))

    # Convert Python time structure from Monday-origin to Sunday-origin.
    weekday = (datetime.tm_wday + 1) % 7

    # Get the date of the previous Sunday or today's date if Sunday.
    prev_sunday_date = datetime.tm_mday - weekday
    next_sunday_date = prev_sunday_date + 7

    """ Test for March window opening threshold: Last Sunday.
    """
    if datetime.tm_mon == 3:
        if next_sunday_date > 31 or (datetime.tm_mday == 31 and next_sunday_date == 31):  # Last Sunday of month or after
            return True  # CEST
        return False #CET

    """Test for October window closing threshold: Last Sunday.
    """
    if datetime.tm_mon == 10:
        if next_sunday_date > 31 or (datetime.tm_mday == 31 and next_sunday_date == 31):  # Last Sunday of month or after
            return False  # CET
        return True # CEST

    # Check for Standard Time window
    if datetime.tm_mon < 3 or datetime.tm_mon > 10:  # Dec - Feb: xST
        return False  # xST
    return True  # DST; datetime.tm_mon is Apr - Oct


def adjust_dst(datetime):
    """Converts Central European Time (CET) to Central European Summer Time
    (CEST). Input to this function is a structured time object. The
    function returns a structured time object adjusted to a DST value if
    appropriate and a flag indicating the DST adjustment was made. The helper
    cannot correctly detect DST for a structured time object that is encoded as
    DST.

    :param structured_time datetime: The Standard Time structured time
    input value. Can be any structured time value within the specified date
    calculation range of CircuitPython, currently January 1, 2000 00:00:00 to
    January 19, 2038 03:14:07. No default value.
    """

    is_dst = _detect_dst(datetime)  # Determine if datetime is within DST window

    if is_dst:  # If DST, add an hour
        dst_date_time = time.mktime(datetime) + 3600
        return time.localtime(dst_date_time), True
    return datetime, False
