# Copyright notice for dperf originally developed by David Smith
# MIT License
# 
# Copyright (c) 2016 David Smith dave@smith.earth 
# send donations to bitcoin wallet 19Myzrm8wsoj2XYX8vYK6mq17TTkUy5uD1
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# End of Copyright notice
#
# Version release notes
#
# dperf verion 1.0
# 20160511 Added MIT License for public release
#
# dperf verion 0.1.6
# 20160422 Fixed text on column headers
# 20160422 Allowed for increasing blocksize (not complete)
# 20160425 Added os.fsync(f.fileno()) to writes to properly calculate latency
# 
#
# dperf verion 0.1.5
# 20160408 Updated graph view and scaling
#
# dperf verion 0.1.4
# 20160408 Added read cache statistics
#
# dperf verion 0.1.3
# 20150323 Changed w/r percent to percent of time
#
# dperf verion 0.1.2
#
# 20141231 Removed recursive loop for column display and replaced with 'if' for each
# 20141231 Set IOpercent check to max at 100%, it would go over due to rounding
#
# dperf verion 0.1.1
#
# 20141229 Correct error with binary columns selector to reflect 32 possible bits
#
#dperf version 0.1
#
import sys
from datetime import datetime
from random import randint
from random import shuffle
from random import randrange
import time
import os
import signal
import io

thisplatform = os.name
VERSION = "1.0"
#exit
def printheaders():
    global columnlist
    displayline = ''
    displaylin2 = ''
    colpos = 0
    if (columnlist[0] == '1'):
        #0 test run
        displayline = "%s   Run" % (displayline)
        displaylin2 = "%s -----" % (displaylin2)
    if (columnlist[1] == '1'):
        #1 Date
        displayline = "%s Date    " % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[2] == '1'):
        #2 Time
        displayline = "%s Time       " % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[3] == '1'):
        #3 filename
        displayline = "%s FileName      " % (displayline)
        displaylin2 = "%s --------------" % (displaylin2)
    if (columnlist[4] == '1'):
        #4 filesize
        displayline = "%s FileSize   " % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[5] == '1'):
        #5 blocksize
        displayline = "%s BlockSize" % (displayline)
        displaylin2 = "%s ---------" % (displaylin2)
    if (columnlist[6] == '1'):
        #6 tottime
        displayline = "%s     RunTime" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[7] == '1'):
        #7 WPS
        displayline = "%s Writes/Sec" % (displayline)
        displaylin2 = "%s ----------" % (displaylin2)
    if (columnlist[8] == '1'):
        #8 RPS
        displayline = "%s  Reads/Sec" % (displayline)
        displaylin2 = "%s ----------" % (displaylin2)
    if (columnlist[9] == '1'):
        #9 IOPS
        displayline = "%s      IOPS" % (displayline)
        displaylin2 = "%s ---------" % (displaylin2)
    if (columnlist[10] == '1'):
        #10 minwseektime
        displayline = "%s WMinSeek" % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[11] == '1'):
        #11 maxwseektime
        displayline = "%s WMaxSeek" % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[12] == '1'):
        #12 avgwseektime
        displayline = "%s WAvgSeek" % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[13] == '1'):
        #13 minwtime
        displayline = "%s WMinLatency" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[14] == '1'):
        #14 maxwtime
        displayline = "%s WMaxLatency" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[15] == '1'):
        #15 avgwtime
        displayline = "%s WAvgLatency" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[16] == '1'):
        #16 minrseektime
        displayline = "%s RMinSeek" % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[17] == '1'):
        #17 maxrseektime
        displayline = "%s RMaxSeek" % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[18] == '1'):
        #18 avgrseektime
        displayline = "%s RAvgSeek" % (displayline)
        displaylin2 = "%s --------" % (displaylin2)
    if (columnlist[19] == '1'):
        #19 minrtime
        displayline = "%s RMinLatency" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[20] == '1'):
        #20 maxrtime
        displayline = "%s RMaxLatency" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[21] == '1'):
        #21 avgrtime
        displayline = "%s RAvgLatency" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[22] == '1'):
        #22 wmbitsps
        displayline = "%s       WMbps" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[23] == '1'):
        #23 wkbytesps
        displayline = "%s      WKBps" % (displayline)
        displaylin2 = "%s ----------" % (displaylin2)
    if (columnlist[24] == '1'):
        #24 wmbytesps
        displayline = "%s       WMBps" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[25] == '1'):
        #25 rmbitsps
        displayline = "%s       RMbps" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[26] == '1'):
        #26 rkbytesps
        displayline = "%s      RKBps" % (displayline)
        displaylin2 = "%s ----------" % (displaylin2)
    if (columnlist[27] == '1'):
        #27 rmbitsps
        displayline = "%s       RMbps" % (displayline)
        displaylin2 = "%s -----------" % (displaylin2)
    if (columnlist[28] == '1'):
        #28 rmbitsps
        displayline = "%s         WBytes" % (displayline)
        displaylin2 = "%s --------------" % (displaylin2)
    if (columnlist[29] == '1'):
        #29 rmbitsps
        displayline = "%s         RBytes" % (displayline)
        displaylin2 = "%s --------------" % (displaylin2)
    if (columnlist[30] == '1'):
        #30 IOPercent
        displayline = "%s   IO" % (displayline)
        displaylin2 = "%s ----" % (displaylin2)
    if (columnlist[31] == '1'):
        #31 CPUPercent
        displayline = "%s  CPU" % (displayline)
        displaylin2 = "%s ----" % (displaylin2)
    colpos=colpos+1
    print (displayline)
    print (displaylin2)


def signalhandler(signal, frame):
    global graph
    graph=graph*-1
    #print("")
    if (graph < 1):
        printheaders()

graph=-1

if (thisplatform == 'nt'):
    signal.signal(signal.SIGBREAK, signalhandler)
    def gettimestamp():
        #time.clock() is best for windows
        #time.time() is best fo *nix
        return time.clock()

else:
    signal.signal(signal.SIGQUIT, signalhandler)
    def gettimestamp():
        #time.clock() is best for windows
        #time.time() is best fo *nix
        return time.time()
c=0
tfilename=""
trp=""
tpause=""
truns=""
tblock=""
tfilesize=""
tgraph=""
tinterval=1.0
tbrief=""
tcols=""
for x in sys.argv:
    c=c+1
    #print (x)
    try:
        if (x == "-filename"):
            tfilename = sys.argv[c]
            #print("filename ", tfilename)
        if (x == "-rp"):
            trp = sys.argv[c]
            #print("trp ", trp)
        if (x == "-pause"):
            tpause = sys.argv[c]
            #print("tpause ", tpause)
        if (x == "-runs"):
            truns = sys.argv[c]
            #print("truns ", tsecs)
        if (x == "-block"):
            tblock = sys.argv[c]
            #print("tblock ", tblock)
        if (x == "-blockinc"):
            tblockinc = sys.argv[c]
            #print("tblock ", tblock)
        if (x == "-filesize"):
            tfilesize = sys.argv[c]
            #print("tfilesize ", tfilesize)
        if (x == "-graph"):
            tgraph = sys.argv[c]
            #print("tgraph ", tgraph)
        if (x == "-interval"):
            tinterval = sys.argv[c]
            #print("tinterval ", tinterval)
        if (x == "-brief"):
            tbrief = sys.argv[c]
            #print("tinterval ", tinterval)
        if (x == "-cols"):
            tcols = sys.argv[c]
            #print("tinterval ", tinterval)
        if (x == "-?") or (x == "/?") or (x == "-help") or (x == "--help"):
            print("dperf by Dave Smith")
            print("dperf ver " + VERSION)
            print ("Send donations to 19Myzrm8wsoj2XYX8vYK6mq17TTkUy5uD1")
            print("")
            print("Syntax:")
            print(" dperf [-rp readpercent] [-runs testruns] [-interval testrun interval] [-block blocksize] [-blockinc incrementPerRun]")
            print("   [-graph yes | no] [-brief yes | no] [-pause yes | no] [[-filename existingfile] [-filesize filesize]]")
            print("   [-cols 32bitpattern | all | mix | read | write | bits | bytes]")
            print("")
            print("Note: out of range values will be replaced by defaults.  Ensure you are running the test you want.")
            exit()
    except:
        print("dperf by Dave Smith")
        print("dperf ver " + VERSION)
        print ("Send donations to 19Myzrm8wsoj2XYX8vYK6mq17TTkUy5uD1")
        print("")
        print("Syntax:")
        print(" dperf [-rp readpercent] [-runs testruns] [-interval testrun interval] [-block blocksize] [-blockinc incrementPerRun]")
        print("   [-graph yes | no] [-brief yes | no] [-pause yes | no] [[-filename existingfile] [-filesize filesize]]")
        print("   [-cols 32bitpattern | all | mix | read | write | bits | bytes]")
        print("")
        print("Note: out of range values will be replaced by defaults.  Ensure you are running the test you want.")
        exit()
           
try:
    trpi = int(trp)
except:
    trpi = 50
if (trpi < 0) or (trpi > 100):
    rpercent = 50
else:
    rpercent = trpi


if (tpause == "YES") or (tpause == "yes"):
    blnpause = 1
else:
    blnpause = 0

if (tbrief == "YES") or (tbrief == "yes"):
    blnbrief = 1
else:
    blnbrief = 0


if (tgraph == "YES") or (tgraph == "yes"):
    graph = 1
else:
    graph = -1

try:
    trunsi = int(truns)
except:
    trunsi = 10
if (trunsi < 1):
    testruns = 1
else:
    if (trunsi > 100000):
        testruns = 100000
    else:
        testruns = trunsi
        
try:
    tintervalf = float(tinterval)
except:
    tintervalf = 1.0
if (tintervalf < .1):
    interval = .1
else:
    if (tintervalf > 600):
        interval = 600
        
    else:
        interval = tintervalf

try:
    tblocki = int(tblock)
except:
    tblocki = 131072
if (tblocki < 1):
    blocksize = 1
else:
    if (tblocki > 10000000):
        blocksize = 10000000
    else:
        blocksize = tblocki

if (len(tcols) == 32):
    columnlist=tcols
else:
    columnlist = "11101111110000010000011101100000"
    if (tcols == 'mix'):
        columnlist = "11101111110000010000011101100000"
    if (tcols == 'read'):
        columnlist = "11101110100000000011110001100000"
    if (tcols == 'write'):
        columnlist = "11101111000011110000001100000000"
    if (tcols == 'all'):
        columnlist = "11111111111111111111111111111111"
    if (tcols == 'bits'):
        columnlist = "10000001110000000000001001000000"
    if (tcols == 'bytes'):
        columnlist = "10000001110000000000000100100000"

try:
    tfilesizei = int(tfilesize)
except:
    tfilesizei = 1200000000
if (tfilesizei < 1):
    filesize = 1
else:
    if (tblocki > 12000000000):
        filesize = 12000000000
    else:
        filesize = tfilesizei

try:
    tblockinci = int(tblockinc)
except:
    tblockinci = 0
if (tblockinci < 1):
    blockinc = 0
else:
    if (tblockinci > filesize/2):
        blockinc = (filesize/2)/testruns
    else:
        blockinc = tblockinci

fileready=0
if (tfilename == ""):
    filename = "test" + chr(randint(65,85)) + chr(randint(65,85)) + chr(randint(65,85)) + chr(randint(65,85)) + ".dperf"
else:
    filename = tfilename
    try:
        #print ("have name")
        f = open(filename, 'r+b')
        f.seek(0, os.SEEK_END)
        filesize = f.tell()
        fileready=1
        #f.close()
    except:
        print("There is an error with the file you selected, not using.")
        fileready=0
        filename = "test" + chr(randint(65,85)) + chr(randint(65,85)) + chr(randint(65,85)) + chr(randint(65,85)) + ".dperf"

if (blocksize > filesize):
    blocksize = int(filesize / 100)

if (blnbrief == 0):
    print ("dperf ver " + VERSION)
    print ("Send donations to 19Myzrm8wsoj2XYX8vYK6mq17TTkUy5uD1")
    print ("Test file " + filename + " " + str(filesize) + " bytes")
    if (blockinc > 0):
        print ("IO blocks " + str(blocksize) + " bytes start, increasing by " + str(blockinc) + " per run")
    else:
        print ("IO blocks " + str(blocksize) + " bytes")
    print ("IO data   " + str(100 - rpercent) + "% Write and " + str(rpercent) + "% Read")
    print ("Test runs " + str(testruns)) 
    print ("Interval  " + str(interval) + " seconds")
    print ("Columns   " + columnlist)
    
SEQBLOCK=131072
RNDBLOCK=blocksize
#RNDBLOCK=2048
seqfilesize = filesize
rndfilesize = filesize
BLOCKCOUNT = int(seqfilesize / blocksize) - 1
if (fileready == 0):
    if (blnbrief == 0):
        print ("Creating test file...")

    #fr = open(filenamer, 'w+b')
    #fr.seek(seqfilesize-1)
    #fr.write('\x00')
    f = open(filename, 'w+b')
    for x in range(0,seqfilesize,SEQBLOCK):
        f.write(chr(randint(25,255)) * SEQBLOCK)
        #f.flush()
        
f.flush()
os.fsync(f.fileno())
f.close()
#print (io.DEFAULT_BUFFER_SIZE)
#print '----'
f = open(filename, 'r+b',0)

if (blnpause == 1):
    mydata = raw_input('Ready - Press enter when ready...')
else:
    if (blnbrief == 0) and (fileready == 0):
        print ("Done...")

if (blnbrief == 0):
    if (thisplatform == 'nt'):
        print ("Hit CTRL-BREAK to switch from data to graph")
    else:
        print ("Hit CTRL-\ to switch from data to graph")

if (graph < 1) and (blnbrief == 0):
    printheaders()
    
r=int(0)
w=int(0)
runcount=0
DATAPOINTS = 1000000
#DATAPOINTS = 10000
wseektime = [0] * DATAPOINTS
rseektime = [0] * DATAPOINTS
wlatency = [0] * DATAPOINTS
rlatency = [0] * DATAPOINTS
rpercent=float(rpercent)
if (rpercent>0):
    rpercent=rpercent/100

nowtime = gettimestamp()
snapstart = gettimestamp()
snaptime = snapstart+interval
#read cache count hits
counthits=0
countmisses=0
while (runcount < testruns):
    #if (randrange(0,100)<rpercent):
    if ((nowtime-int(nowtime))<rpercent):
        #do a read operation
        rnum = randrange(0,BLOCKCOUNT)
        rst = gettimestamp()
        f.seek(rnum*RNDBLOCK)
        #print gettimestamp()-rst
        rseektime[r]=gettimestamp()-rst
        rlt = gettimestamp()
        indata = f.read(RNDBLOCK)
        rlatency[r]=gettimestamp()-rlt
        r=r+1
    else:
        #do a write operation
        rnum = randrange(0,BLOCKCOUNT)        
        wst = gettimestamp()
        f.seek(rnum*RNDBLOCK)
        wseektime[w]=gettimestamp()-wst
        wlt = gettimestamp()
        f.write(chr(randint(25,255)) * RNDBLOCK)
        f.flush()
        os.fsync(f.fileno())
        wlatency[w]=gettimestamp()-wlt
        w=w+1
    if (nowtime > snaptime):
        tottime = nowtime - snapstart
        runcount=runcount+1
        if (w<1):
            avgwseektime = 0
            minwseektime = 0
            maxwseektime = 0
            avgwtime = 0
            minwtime = 0
            maxwtime = 0
        else:
            avgwseektime = sum(wseektime)/w
            minwseektime = min(wseektime)
            minwseektime = sorted(wseektime,reverse=True)[w-1]
            maxwseektime = max(wseektime)
            avgwtime = sum(wlatency)/w
            minwtime = sorted(wlatency,reverse=True)[w-1]
            maxwtime = max(wlatency)
        if (r<1):
            avgrseektime = 0
            minrseektime = 0
            maxrseektime = 0
            avgrtime = 0
            minrtime = 0
            maxrtime = 0
        else:
            avgrseektime = sum(rseektime)/r
            minrseektime = sorted(rseektime,reverse=True)[r-1]
            maxrseektime = max(rseektime)
            avgrtime = sum(rlatency)/r
            minrtime = sorted(rlatency,reverse=True)[r-1]
            #print (sorted(rlatency))
            #print ("%8.6f  %d   %d" % (ninetyfifth, ninetyfive, r))
            counthits=0
            countmisses=0
            for tnum in range(0,r):
            #for tnum in (rlatency):
                #if (tnum >0):
                if (rlatency[tnum]<(minrtime*100)):
                    counthits=counthits+1
                else:
                    countmisses=countmisses+1
            maxrtime = max(rlatency)
        
        wbytes = RNDBLOCK * w
        rbytes = RNDBLOCK * r
        wmbytesps = ((wbytes / tottime)/1000000)
        wkbytesps = ((wbytes / tottime)/1000)
        rmbytesps = ((rbytes / tottime)/1000000)
        rkbytesps = ((rbytes / tottime)/1000)
        wmbitsps = wmbytesps * 8
        rmbitsps = rmbytesps * 8
        wps = int(w/tottime)
        rps = int(r/tottime)
        IOPS = int(wps+rps)
        counthitsps=int(counthits/tottime)
        tottime2=sum(rseektime) + sum(rlatency) + sum(wseektime) + sum(wlatency)
        IOpercent = (100/tottime)*tottime2
        if (IOpercent > 100):
            IOpercent = 100
        CPUpercent = 100 - IOpercent
        if (graph<1):
            displayline = ''
            if (columnlist[0] == '1'):
                #0 test run
                displayline = "%s %5d" % (displayline, runcount)
            if (columnlist[1] == '1'):
                #1 Date
                dc = datetime.now().strftime("%Y%m%d")
                displayline = "%s %s" % (displayline, dc)
            if (columnlist[2] == '1'):
                #2 Time
                t2 = datetime.now().strftime("%f")
                tc = datetime.now().strftime("%H:%M:%S.") + t2[:2] 
                displayline = "%s %s" % (displayline, tc)
            if (columnlist[3] == '1'):
                #3 filename
                displayline = "%s %s" % (displayline, filename)
            if (columnlist[4] == '1'):
                #4 filesize
                displayline = "%s %11d" % (displayline, filesize)
            if (columnlist[5] == '1'):
                #5 blocksize
                displayline = "%s %9d" % (displayline, RNDBLOCK)
            if (columnlist[6] == '1'):
                #6 tottime
                displayline = "%s %11.6f" % (displayline, tottime)
            if (columnlist[7] == '1'):
                #7 WPS
                displayline = "%s  %9d" % (displayline, wps)
            if (columnlist[8] == '1'):
                #8 RPS
                displayline = "%s  %9d" % (displayline, rps)
            if (columnlist[9] == '1'):
                #9 IOPS
                displayline = "%s %9d" % (displayline, IOPS)
            if (columnlist[10] == '1'):
                #10 minwseektime
                displayline = "%s %8.6f" % (displayline, minwseektime)
            if (columnlist[11] == '1'):
                #11 maxwseektime
                displayline = "%s %8.6f" % (displayline, maxwseektime)
            if (columnlist[12] == '1'):
                #12 avgwseektime
                displayline = "%s %8.6f" % (displayline, avgwseektime)
            if (columnlist[13] == '1'):
                #13 minwtime
                displayline = "%s    %8.6f" % (displayline, minwtime)
            if (columnlist[14] == '1'):
                #14 maxwtime
                displayline = "%s    %8.6f" % (displayline, maxwtime)
            if (columnlist[15] == '1'):
                #15 avgwtime
                displayline = "%s    %8.6f" % (displayline, avgwtime)
            if (columnlist[16] == '1'):
                #16 minrseektime
                displayline = "%s %8.6f" % (displayline, minrseektime)
            if (columnlist[17] == '1'):
                #17 maxrseektime
                displayline = "%s %8.6f" % (displayline, maxrseektime)
            if (columnlist[18] == '1'):
                #18 avgrseektime
                displayline = "%s %8.6f" % (displayline, avgrseektime)
            if (columnlist[19] == '1'):
                #19 minrtime
                displayline = "%s    %8.6f" % (displayline, minrtime)
            if (columnlist[20] == '1'):
                #20 maxrtime
                displayline = "%s    %8.6f" % (displayline, maxrtime)
            if (columnlist[21] == '1'):
                #21 avgrtime
                displayline = "%s    %8.6f" % (displayline, avgrtime)
            if (columnlist[22] == '1'):
                #22 wmbitsps
                displayline = "%s %11.3f" % (displayline, wmbitsps)
            if (columnlist[23] == '1'):
                #23 wkbytesps
                displayline = "%s %10d" % (displayline, wkbytesps)
            if (columnlist[24] == '1'):
                #24 wmbytesps
                displayline = "%s %11.3f" % (displayline, wmbytesps)
            if (columnlist[25] == '1'):
                #25 rmbitsps
                displayline = "%s %11.3f" % (displayline, rmbitsps)
            if (columnlist[26] == '1'):
                #26 rkbytesps
                displayline = "%s %10d" % (displayline, rkbytesps)
            if (columnlist[27] == '1'):
                #27 rmbitsps
                displayline = "%s %11.3f" % (displayline, rmbytesps)
            if (columnlist[28] == '1'):
                #28 wbytes
                displayline = "%s %14d" % (displayline, wbytes)
            if (columnlist[29] == '1'):
                #29 rbytes
                displayline = "%s %14d" % (displayline, rbytes)
            if (columnlist[30] == '1'):
                #30 rmbitsps
                displayline = "%s %4.1f" % (displayline, IOpercent)
            if (columnlist[31] == '1'):
                #31 rmbitsps
                displayline = "%s %4.1f" % (displayline, CPUpercent)
            print (displayline)
            
        else:
            if (IOPS > 50000):
                i = (IOPS)/10000
                g = str("W" * int(wps/10000)) + "|" + str("R" * int(rps/10000))
            else:
                if (IOPS > 10000):
                    i = (IOPS)/1000
                    g = str("O" * int(wps/1000)) + "|" + str("I" * int(rps/1000))
                else:
                    if (IOPS > 100):
                        i = (IOPS)/100
                        g = str("w" * int(wps/100)) + "|" + str("r" * int(rps/100))
                    else:
                        i = (IOPS)
                        g = str("." * int(wps)) + "|" + str("." * int(rps))
                    
            d2 = datetime.now().strftime("%f")
            d = datetime.now().strftime("%Y%m%d %H:%M:%S.") + d2[:2]
            #print ("%s %8d IOPS  %s" % (d,IOPS,g))
            #print ("%s hits %8d  misses %8s %8d IOPS  %s" % (d,counthits,countmisses,IOPS,g))
            print ("%s %8d cache hits/s, %8d IOPS  %s" % (d,counthitsps,IOPS,g))
        #clear results
        r=0
        w=0
        wseektime = [0] * DATAPOINTS
        rseektime = [0] * DATAPOINTS
        wlatency = [0] * DATAPOINTS
        rlatency = [0] * DATAPOINTS
        snapstart=gettimestamp()
        snaptime=snapstart+interval
        nowtime=snapstart
        RNDBLOCK=RNDBLOCK+blockinc
    else:
        nowtime=gettimestamp()

f.flush()
f.close()

if (fileready == 0):
    complete=0
    while (complete==0):
        try:
            os.remove(filename)
            complete=1
        except:
            time.sleep(.1)
