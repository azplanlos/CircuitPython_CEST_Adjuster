Introduction
============




.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/CedarGroveStudios/CircuitPython_DST_Adjuster/workflows/Build%20CI/badge.svg
    :target: https://github.com/CedarGroveStudios/CircuitPython_DST_Adjuster/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A CircitPython helper to detect and adjust North American Daylight Saving Time (DST).

``Adjust DST`` converts Standard Time (xST) to North American DST. Input to this
function is a structured time object in xST. The function returns a structured
time object adjusted to a DST value if appropriate and a flag indicating the DST
adjustment was made. The helper cannot detect DST for a structured time object
that is encoded as DST.

.. image:: https://github.com/CedarGroveStudios/CircuitPython_DST_Adjuster/blob/main/media/WARNING.jpg


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install cedargrove_dst_adjuster

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    import time
    from cedargrove_dst_adjuster import adjust_dst

    # Today's date: 11/01/2020 00:00 Standard Time (xST)
    datetime = time.struct_time((2020, 11, 1, 0, 0, 0, 6, 0, -1))

    # Check datetime and adjust if DST
    adj_datetime, is_dst = adjust_dst(datetime)

    if is_dst:
        flag_text = "DST"
    else:
        flag_text = "xST"

    # Print the submitted time
    print(
        "     {}/{}/{} {:02}:{:02}:{:02}  week_day={}".format(
            datetime.tm_mon,
            datetime.tm_mday,
            datetime.tm_year,
            datetime.tm_hour,
            datetime.tm_min,
            datetime.tm_sec,
            datetime.tm_wday,
        )
    )

# Print the adjusted time
print(
    "{}: {}/{}/{} {:02}:{:02}:{:02}  week_day={}".format(
        flag_text,
        adj_datetime.tm_mon,
        adj_datetime.tm_mday,
        adj_datetime.tm_year,
        adj_datetime.tm_hour,
        adj_datetime.tm_min,
        adj_datetime.tm_sec,
        adj_datetime.tm_wday,
    )
)

Documentation
=============
API documentation for this library can be found on `here <https://github.com/CedarGroveStudios/CircuitPython_DST_Adjuster/blob/main/media/pseudo_rtd_cedargrove_dst_adjuster.pdf>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/CedarGroveStudios/Cedargrove_CircuitPython_DST_Adjuster/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
