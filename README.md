# dperf
dperf Cross platform opensource disk performance test tool

Runs on most operating systems including Windows, Linux, ESXi, OSX.

Can provide great insight into disk IO performance on traditional hard drives, RAID arrays, USB disks, solid state drives (SSD).  Also works well on NAS storage like NFS file shares and CIFS file shares and SAN technologies like FC, FCoE, and iSCSI.

dperf by Dave Smith
dperf ver 1.0
Send donations to 19Myzrm8wsoj2XYX8vYK6mq17TTkUy5uD1

Syntax:
 dperf [-rp readpercent] [-runs testruns] [-interval testrun interval] [-block blocksize] [-blockinc incrementPerRun]
   [-graph yes | no] [-brief yes | no] [-pause yes | no] [[-filename existingfile] [-filesize filesize]]
   [-cols 32bitpattern | all | mix | read | write | bits | bytes]

Note: out of range values will be replaced by defaults.  Ensure you are running the test you want.

Available output vales can be selected with the -cols switch

Columns:

1  Test run number

2  Date

3  Time

4  Filename

5  File size

6  Block size

7  Run time

8  Writes per second

9  Reads per second

10  IOPS

11 Write minimum seek time

12 Write maximum seek time

13 Write average seek time

14 Write minimum latency

15 Write maximum latency

16 Write average latency

17 Read minimum seek time

18 Read maximum seek time

19 Read average seek time

20 Read minimum latency

21 Read maximum latency

22 Read average latency

23 Write Mbps

24 Write KBps

25 Write MBps

26 Read Mbps

27 Read KBps

28 Read MBps

29 Write bytes

30 Read bytes

31 IO percent

32 CPU percent
