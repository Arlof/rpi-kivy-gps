##################################
##
## GSV GPS Data Example
##
##################################

import threading
import time
import pynmea2
        #      0 1  2  3 4   5   6  7  8  9  10 11 12  13  14 15 16 17 18 19
GSV1 = '$GPGSV,3,1,12,05,83,111,15,12,54,222,21,02,49,038,28,25,44,287,22*74'
GSV2 = '$GPGSV,3,2,12,20,35,219,25,29,26,317,,06,17,063,21,19,13,116,23*73'
GSV3 = '$GPGSV,3,3,12,13,12,152,10,15,04,182,19,09,02,041,,36,,,*44'

class GsvData():
    num_sats = 0
    num_sentance = 0
    PRN_1 = ['0','0','0','0']       # PRN Satelite Number, Elevation, Azimuth, Signal To Noise
    PRN_2 = ['0','0','0','0']
    PRN_3 = ['0','0','0','0']
    PRN_4 = ['0','0','0','0']
    
    
    
    testdata = "Testing"
    
def processGSV():
    if msgP.data[1] == '1':
        # Process And Dump To Sentence 1
        gsv1.num_sats = msgP.data[2]
        gsv1.num_sentance = msgP.data[0]
        gsv1.PRN_1 = msgP.data[3:7]
        gsv1.PRN_2 = msgP.data[7:11]
        gsv1.PRN_3 = msgP.data[11:15]
        gsv1.PRN_4 = msgP.data[15:19]
        
    elif (msgP.data[1] == '2'):
    #Process And Dump To Sentence 2
        gsv2.num_sats = msgP.data[2]
        gsv2.num_sentance = msgP.data[0]
        gsv2.PRN_1 = msgP.data[3:7]
        gsv2.PRN_2 = msgP.data[7:11]
        gsv2.PRN_3 = msgP.data[11:15]
        gsv2.PRN_4 = msgP.data[15:19]
        
    elif (msgP.data[1] == '3'):
    #Process And Dump To Sentence 30
        gsv3.num_sats = msgP.data[2]
        gsv3.num_sentance = msgP.data[0]
        gsv3.PRN_1 = msgP.data[3:7]
        gsv3.PRN_2 = msgP.data[7:11]
        gsv3.PRN_3 = msgP.data[11:15]
        gsv3.PRN_4 = msgP.data[15:19]
        
    else:
        print "error on sat count"
        
    
    
def timer1():
    while (1):
        print("One Second Timer")
        time.sleep(1)
        if d.testrun == 0:
            break

gsv1 = GsvData()        ## Holder For Sentence 1
gsv2 = GsvData()        ## Holder For Sentence 2
gsv3 = GsvData()        ## Holder For Sentence 3

msgP = pynmea2.parse(GSV1)       

t = threading.Thread(target= timer1)


