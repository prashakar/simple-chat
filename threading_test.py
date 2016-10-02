#!/usr/bin/env python

import socket, sys, threading, time

class Threading(object):
        """
        The run() method will be started and run in background until the application exits
        """

        def __init__(self,interval=1):
                self.interval = interval

                thread = threading.Thread(target=self.run)
                thread.daemon = True
                thread.start()

        def run(self):
                while True:
			x = 0
                        print "do something in background"
                        time.sleep(self.interval)
			test.append(x)
			x += 1
			
if __name__ == "__main__":
	test = []
	example = Threading()
	time.sleep(3)
	print "checkpoint"
	print test
	time.sleep(2)
	print test
	print "bye"

