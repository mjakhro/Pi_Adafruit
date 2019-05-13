#Reads temperature and pressure from Adafruit temperature and humidity devices.
#Plots a graph with 50 intervals
# Works only on raspberry pi

from drawnow import *
import Adafruit_DHT
import time

 
tempF= []
pressure=[]

plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0
 
def makeFig(): #Create a function that makes our desired plot
    plt.ylim(0,100)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp C')                            #Set ylabels
    plt.plot(tempF, 'rx--', label='Degrees C')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    plt.ylim(0,100)                                 #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(pressure, 'b^--', label='Humidity (%)') #plot pressure data
    plt2.set_ylabel('Humidity (%)')                  #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    
 
while True: # While loop that loops forever
    hum, temp = Adafruit_DHT.read_retry(11, 17) #Adafruit 11 selected and GPIO17 on raspberry Pi
    tempF.append(temp)                     #Build our tempF array by appending temp readings
    pressure.append(hum)                   #Building our pressure array by appending humidity readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        tempF.pop(0)                       #This allows us to just see the last 50 data points
        pressure.pop(0)
    print(temp,hum)                        #see the values 
    time.sleep(1)                          #wait 1 sec to read data again.

