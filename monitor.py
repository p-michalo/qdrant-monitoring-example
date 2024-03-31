import psutil
import pygal
#import os
import subprocess
from time import sleep
from datetime import datetime, timedelta
from prettytable import PrettyTable
'''
Script monitors CPU, RAM, and Disk IO usage throughput 
'''
timeout = 360            #max number of seconds of metrics collection
sampleInterval = 1       #set to take sample every Y seconds
metricsPrintInterval = 5 #set to print new metric samples every Z seconds

#It can be snapshot URL or URI (path to the local file)
snapshotURL = "https://snapshots.qdrant.io/arxiv_titles-3083016565637815127-2023-05-29-13-56-22.snapshot"

#Initiate empty tables for metrics data
xLabels =[]
dataCPU = []
dataMemSwapUsed = []
dataMemSwapPerc = []
dataMemVirtUsed = []
dataMemVirtPerc = []
dataDiskWriteC = []
dataDiskReadC = []
dataDiskBusyT = []
dataDiskWriteT = []
dataDiskReadT = []
table = PrettyTable()

# test start date
dtFileString = datetime.now().strftime("%Y%m%d-%H%M%S")

#CPU chart initiation
cpuPercent = pygal.Line(x_label_rotation=30, show_minor_x_labels=False)
cpuPercent.title = 'CPU Stats'

#Memory chart initiation
memSwap = pygal.Line(x_label_rotation=30, show_minor_x_labels=False)
memSwap.title = 'Swap Memory Stats'

memVirt = pygal.Line(x_label_rotation=30, show_minor_x_labels=False)
memVirt.title = 'Virtual Memory Stats'

#Disks chart initiation
diskIO = pygal.Line(x_label_rotation=30, show_minor_x_labels=False)
diskIO.title = 'Disk IO Stats'

#os.system("python3 start_recovery.py "+snapshotURL+" &")
recoveryProc = subprocess.Popen(["python3","start_recovery.py",snapshotURL, "&"])
print("\nSnapshot recovery is running under PID-> "+ str(recoveryProc.pid))
print("__________________________")
#Gathering data
print ("Monitoring in progress ...")
countDown = timeout
try:
    table.field_names = ["CPU%","MemSwU","MemSw%","MemVUsed","MemV%","DiskWC","DiskRC","DiskBT","DiskWT","DiskRT"]
    while True:
        if countDown <= 0:
            print("\n______________________________________________")
            print("TIMED OUT. Saving the results... ")
            break
        xLabels.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sampleCPU = psutil.cpu_percent(interval=1, percpu=False)
        dataCPU.append(sampleCPU)

        sampleMemSwap = psutil.swap_memory()._asdict()
        dataMemSwapUsed.append(sampleMemSwap["used"])
        dataMemSwapPerc.append(sampleMemSwap["percent"])

        sampleMemVirt = psutil.virtual_memory()._asdict()
        dataMemVirtUsed.append(sampleMemVirt["used"])
        #dataMemVirtFree.append(sampleMemVirt["free"])
        dataMemVirtPerc.append(sampleMemVirt["percent"])

        sampleDiskIO = psutil.disk_io_counters(perdisk=False, nowrap=True)._asdict()
        dataDiskWriteC.append(sampleDiskIO["write_count"])
        dataDiskReadC.append(sampleDiskIO["read_count"])
        dataDiskBusyT.append(sampleDiskIO["busy_time"])
        dataDiskWriteT.append(sampleDiskIO["write_time"])
        dataDiskReadT.append(sampleDiskIO["read_time"])

        # prints progess acroding to the interval
        if countDown % metricsPrintInterval == 0:
            table.add_row([sampleCPU, \
                           sampleMemSwap["used"],sampleMemSwap["percent"], \
                           sampleMemVirt["used"],sampleMemVirt["percent"], \
                           sampleDiskIO["write_count"],sampleDiskIO["read_count"], \
                           sampleDiskIO["busy_time"],sampleDiskIO["write_time"],sampleDiskIO["read_time"]])
            print(table)
            table.clear_rows()
        sleep(sampleInterval)
        countDown = countDown - sampleInterval


except KeyboardInterrupt:
    print("\n______________________________________________")
    print("Detected Ctrl-c signal. Saving the results...")
finally:
    renderLabalSpacing = int((timeout - countDown)/10)+1  #calculates chart labels interval

    cpuPercent.add('CPU usage [%]', dataCPU)
    cpuPercent.x_labels = xLabels
    cpuPercent.x_labels_major = xLabels[::renderLabalSpacing]
    cpuPercent.render_to_file(dtFileString+'_cpuPercent.svg')

    memSwap.add('Used [B]', dataMemSwapUsed)
    memSwap.add('Usage[%]', dataMemSwapPerc, secondary=True)
    memSwap.x_labels = xLabels
    memSwap.x_labels_major = xLabels[::renderLabalSpacing]
    memSwap.render_to_file(dtFileString+'_memSwap.svg')

    memVirt.add('Used [B]', dataMemVirtUsed)
    memVirt.add('Usage[%]', dataMemVirtPerc, secondary=True)
    memVirt.x_labels = xLabels
    memVirt.x_labels_major = xLabels[::renderLabalSpacing]
    memVirt.render_to_file(dtFileString+'_memVirt.svg')

    diskIO.add('Writes Time [ms]', dataDiskWriteT)
    diskIO.add('Reads Time [ms]' , dataDiskReadT)
    diskIO.add('Busy Time [ms]'  , dataDiskReadT)
    diskIO.add('Write Counter'   , dataDiskWriteC, secondary=True)
    diskIO.add('Read Counter'    , dataDiskReadC , secondary=True)
    diskIO.x_labels = xLabels
    diskIO.x_labels_major = xLabels[::renderLabalSpacing]
    diskIO.render_to_file(dtFileString+'diskIO.svg')
