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


GSA1 = '$GPGSA,A,3,19,25,12,02,20,05,06,13,,,,,1.36,1.04,0.88*0E'

GGA1 = '$GPGGA,140921.000,3019.4463,N,09527.9966,W,2,08,1.04,79.2,M,-23.7,M,0000,0000*6F'

RMC1 = '$GPRMC,140921.000,A,3019.4463,N,09527.9966,W,0.07,216.46,281116,,,D*7C'

# Test VTG Sentence
VTG1 = '$GPVTG,216.46,T,,M,0.07,N,0.13,K,D*3A'




class GsvData():
    num_sats = 0
    num_sentance = 0
    PRN_1 = ['0','0','0','0']       # PRN Satelite Number, Elevation, Azimuth, Signal To Noise
    PRN_2 = ['0','0','0','0']
    PRN_3 = ['0','0','0','0']
    PRN_4 = ['0','0','0','0']
      
class VtgData():
	true_track = 0
	magnetic_track = 0
	ground_speed_knots = 0 
	ground_speed_kph = 0 
	
class GsaData():
	fix_mode = 0 
	num_sats_used = 0 
	PDOP = 0			#Dilution Of Precision
	HDOP = 0			#Hozizontal Dilustion of Precision
	VDOP = 0 			#Vertical Dilustion Of Precision

class GgaData():
    fix_time = 0
    lat = 0
    lon = 0 
    fix_quality = 0 
    sat_num_track = 0
    altitude_feet = 0 
    altitude_meters = 0 
	
	

class RmcData():
	rmc_time = 0
	rmc_status = 0
	rmc_lat = 0 
	rmc_lon = 0
	rmc_spd = 0 
	track_angle = 0
	rmc_date = 0
	
def processGGA():
	gga.fix_time = msgP.data[1]
	gga.lat = " ".join(msgP.data[1:3])
	gga.lon = " ".join(msgP.data[3:5])
	gga.fix_quality = msgP.data[5]
	gga.sat_num_track = msgP.data[6]
	gga.altitude_meters = msgP.data[8] + " Meters"
	gga.altitude_feet = str(round(float(msgP.data[8])*3.28084)) + " Feet"
	
def processGSA():
    gsa.fix_mode = msgP.data[0]
    gsa.fix_type = msgP.data[1]
	
	
	
def processRMC():
	rmc.rmc_date = '-'.join([msgP.data[8][:2], msgP.data[8][2:4], msgP.data[8][4:]])
	rmc.rmc_time = ':'.join([msgP.data[0][:2], msgP.data[0][2:4], msgP.data[0][4:6]])+ " UTC"
	rmc.rmc_status = msgP.data[1]
	rmc.rmc_lat = " ".join(msgP.data[2:4])
	rmc.rmc_lon = " ".join(msgP.data[4:6])
	rmc.rmc_spd = msgP.data[6] + " Knots"
	rmc.track_angel= msgP.data[7] + " Degrees"
	

def processVTG():
    vtg.true_track = " ".join(msgP.data[0:2])
    vtg.magnetic_track = " ".join(msgP.data[2:4])
    vtg.ground_speed_knots = str(round(msgP.data[4])) + " Knots"
    vtg.ground_speed_kph = str(round(msgP.data[6])) + " KPH"
    vtg.ground_speed_mph = str(round(float(msgP.data[6])/1.60934)) + " MPH"

	
	
    
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

rmc = RmcData()
vtg = VtgData()
gsa = GsaData()
gga = GgaData()

msgP = pynmea2.parse(GGA1)       

t = threading.Thread(target= timer1)


