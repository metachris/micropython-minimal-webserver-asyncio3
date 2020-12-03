"""
Minimal MicroPython webserver, using uasyncio v3 (MicroPython 1.13+),
with a fallback for earlier versions of uasyncio/MicroPython.

* License: MIT
* Repository: https://github.com/metachris/micropython-minimal-webserver-asyncio3
* Author: Chris Hager <chris@linuxuser.at> / twitter.com/metachris

References:
- http://docs.micropython.org/en/latest/library/uasyncio.html
- https://github.com/peterhinch/micropython-async/blob/master/v3/README.md
- https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5
"""
import gc
import sys
import socket
import uasyncio as asyncio

# Network setup helper
import net

# Helper to detect uasyncio v3
IS_UASYNCIO_V3 = hasattr(asyncio, "__version__") and asyncio.__version__ >= (3,)


def _handle_exception(loop, context):
    """ uasyncio v3 only: global exception handler """
    print('Global exception handler')
    sys.print_exception(context["exception"])
    sys.exit()


class MyApp:
    async def start(self):
        # Get the event loop
        loop = asyncio.get_event_loop()

        # Add global exception handler
        if IS_UASYNCIO_V3:
            loop.set_exception_handler(_handle_exception)

        # Create the server and add task to event loop
        server = asyncio.start_server(self.handle_connection, "0.0.0.0", 80)
        loop.create_task(server)

        # Start looping forever
        print('Looping forever...')
        loop.run_forever()

    async def handle_connection(self, reader, writer):
        gc.collect()

        # Get HTTP request line
        data = await reader.readline()
        request_line = data.decode()
        addr = writer.get_extra_info('peername')
        print('Received {} from {}'.format(request_line.strip(), addr))

        # Read headers
        headers = {}
        while True:
            gc.collect()
            line = await reader.readline()
            if line == b'\r\n': break
            frags = line.split(b':', 1)
            if len(frags) != 2:
                print('Invalid request header', line)
                return
            headers[frags[0]] = frags[1].strip()
        print("Headers:", headers)

        # Handle the request
        if len(request_line) > 0:
            response = 'HTTP/1.0 200 OK\r\n\r\n'
            with open('index.html') as f:
                response += f.read()
            await writer.awrite(response)

        # Close the socket
        await writer.aclose()
        print("client socket closed")


# Main code entrypoint
try:
    # If you want to connect to a wifi, or start an access point:
    # net.wifi_connect()
    # net.wifi_start_access_point()

    # Instantiate and run
    myapp = MyApp()

    if IS_UASYNCIO_V3:
        asyncio.run(myapp.start())
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(myapp.start())

except KeyboardInterrupt:
    print('Bye')

finally:
    if IS_UASYNCIO_V3:
        asyncio.new_event_loop()  # Clear retained state

