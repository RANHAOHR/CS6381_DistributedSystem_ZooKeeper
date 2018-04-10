# Sample code for CS6381
# Vanderbilt University
# Instructor: Aniruddha Gokhale
#
# Code taken from ZeroMQ examples with additional
# comments or extra statements added to make the code
# more self-explanatory  or tweak it for our purposes
#
# We are executing these samples on a Mininet-emulated environment
#
#   Weather update client
#   Connects SUB socket to tcp://localhost:5556
#   Collects weather updates and finds avg temp in zipcode
import sys
import zmq
import time

class Subscriber:
    """Implementation of the subscriber"""
    def __init__(self, broker_addr, broker_port, zipcode):
        self.broker = broker_addr
        self.port = broker_port
        self.zipcode = zipcode
        self.socket = zmq.Context().socket(zmq.SUB)
        # Connect to broker
        #context = zmq.Context()
        # Since we are the subscriber, we use the SUB type of the socket
        #socket = context.socket(zmq.SUB)
        connect_str = "tcp://" + self.broker + ":" + self.port
        #print("Collecting updates from weather server proxy at: {}".format(connect_str))
        self.socket.connect(connect_str)

    def subscribe(self):
        # Keep subscribing
        # any subscriber must use the SUBSCRIBE to set a subscription, i.e., tell the
        # system what it is interested in   
        self.socket.setsockopt_string(zmq.SUBSCRIBE, self.zipcode)
        
        # Process 5 updates
        # total_temp = 0
        while True:
            string = self.socket.recv_string()
            zipcode, temperature, relhumidity, ownership, history, pub_time = string.split()
            # total_temp += int(temperature)
            pub_time = float(pub_time.decode('ascii'))
            time_diff = time.time() - pub_time
            print("The time difference is: ", time_diff)
            print string

    def close(self):
        """ This method closes the PyZMQ socket. """
        self.socket.close(0)

if __name__ == '__main__':
    broker = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = sys.argv[2] if len(sys.argv) > 2 else "5556"
    zipcode = sys.argv[3] if len(sys.argv) > 3 else "10001"
    print('input zip:',zipcode)
    # Python 2 - ascii bytes to unicode str
    if isinstance(zipcode, bytes):
        zipcode = zipcode.decode('ascii')
    sub = Subscriber(broker, port, zipcode)
    #sub.connect_broker()
    sub.subscribe()

