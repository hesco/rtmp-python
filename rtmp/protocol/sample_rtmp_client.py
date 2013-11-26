""" Sample implementation of an RTMP client. """

import rtmp_protocol

class SO(rtmp_protocol.FlashSharedObject):
    """ Represents a sample shared object. """

    def on_change(self, key):
        """ Handle change events for the specific shared object. """
        print '%s.sparam = "%s"' % (self.name, self.data['sparam'])

def main():
    """
    Start the client, connect to 127.0.0.1:80 and use 2 remote flash shared
    objects.
    """
    client = rtmp_protocol.RtmpClient(ip="localhost", port=1935, tc_url='rtmp://localhost/IOTStreaming', page_url='', swf_url='', app='IOTStreaming')
    client.connect([["user-1234"]])

    so_name = SO('queueSharedObject', True)
    client.shared_object_use(so_name)

    client.handle_messages()

if __name__ == '__main__':
    main()
