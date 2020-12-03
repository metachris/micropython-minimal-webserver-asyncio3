Minimal MicroPython webserver, using uasyncio v3 (MicroPython 1.13+), with a fallback for earlier versions of uasyncio/MicroPython.

---

A simple TCP server that reads request line and headers, and sends a HTTP 1.0 response.

For a more fully featured webserver, I recommend [tinyweb](https://github.com/belyalov/tinyweb) (and [picoweb](https://github.com/pfalcon/picoweb) for pycopy).

* License: MIT
* Author: Chris Hager <chris@linuxuser.at> / twitter.com/metachris
* Repository: https://github.com/metachris/micropython-minimal-webserver-asyncio3

References:

- http://docs.micropython.org/en/latest/library/uasyncio.html
- https://github.com/peterhinch/micropython-async/blob/master/v3/README.md
- https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5

