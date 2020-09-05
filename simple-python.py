##########################################################################
# simple-python.py 
# Author: bill.harper@appdynamics.com
# 
# This a simple python example script to execute 2 BT's in AppDynamics
#  BT#1 is a simulated transaction using sleeps to stall transactions out
#  BT#2 is a ping command
##########################################################################

from appdynamics.agent import api as appd
import time
import os

tc = 0
pg = 0
def setup():
    print("Lets setup the AppD agent ...\n\n")
    appd.init()

def transaction_simulation():
    global tc
    tc=tc+1
    # we do a mod on 30% of the bts to generate slowness+get slower over time   
    if (tc % 5) == 0 or (tc % 6) == 0 or (tc % 7) == 0:
      print('Transaction - Stalling ',tc)
      time.sleep(35+tc)
    else:
      print('Transaction - Normal ',tc)
      time.sleep(1)
    print('Transaction Completed ',tc)


def transaction_ping():
    global pg
    pg=pg+1
    if (pg % 5) == 0 or (pg % 6) == 0 or (pg % 7) == 0:
        print('Ping - Stalling ',pg) 
        hostname = "google.com" #example
        response = os.system("ping -c 15 " + hostname)
    else:
        print('Ping - Normal ',pg)
        hostname = "google.com" #example
        response = os.system("ping -c 1 " + hostname)


def teardown():
    print("This is it")


# Start of main program

# Endless loop around 2 BT that are simulated

while(True):
  setup()
  while (True):
    with appd.bt('Simple BT'):
        transaction_simulation()
        print('Simple BT sent to AppD')
        time.sleep(1)
        break
  teardown()


  setup()
  while (True):
    with appd.bt('Ping BT'):
        transaction_ping()
        print('Simple Ping BT sent to AppD')
        time.sleep(1)
        break
  teardown()



