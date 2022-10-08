import sys
import os.path
absolutePath = (os.path.realpath(__file__))
rootIndex = absolutePath.rfind('SoftwareEngineeringProject') + len("SoftwareEngineeringProject")
relativePath = absolutePath[:rootIndex] +"/"
sys.path.append(relativePath)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SoftwareEngineeringProject.settings")
import django
from django.conf import settings
import sys
path = settings.BASE_DIR
sys.path.append(path)
import django
django.setup()
from marking.models import *
import codecs
import datetime
from marking.models import *

import random
supervisors = ["ken","glenn"]
titles = ["Multicasting of Bandwidth Efficient Video in Multiradio Multicellular Wireless networks","ADHOC Networks Based Bandwidth Estimation of IEEE 802.11","Data Mining Technique Based Building Intelligent Shopping for Web Services","Automatic Teller Machine Network Implementation based Controlling of CAC Connection Admission","Adaptive Coaching and Co-Operative System for MANETS","Multidimensional and Color Imaging Projections","Inter Domain Packet Filters based Controlling of IP Spoofing","Hidden Markov Models Based Credit Card Fraud Detection","XML Enable SQL Server Based Data Storage and Minimization","Artificial Neural Network Based Verification of Digital Signature","Design and Implementation of E Secure Transaction","Pattern Recognition and Dynamic Character Using Neural Network","Verification of Dynamic Signature Using Pattern Signature","Data Integrity Maintenance and Dynamic University Linking","Filtering and Analyzing of Effective Packet System for ATM Network","Efficient and Distribution and Secure Content Processing by Cooperative Intermediaries","Rule Mining Algorithm for Efficient Association in Distributed Databases","Digest Algorithm for Efficient Message for Data Security"]
studentIDStart = 1632


for title in titles:
    p = Project()
    endOfSID = random.randint(1000,9999)
    studentID = str(studentIDStart)+endOfSID
    kenOrGlenn = random.randint(0,1)
    supervisor = supervisors[kenOrGlenn]
    supervisorid = kenOrGlenn+1
    secondreader = (kenOrGlenn+1) %2

    p.projectid = random.randint(400,700)
    p.title = title
    p.supervisor = supervisor
    p.supervisorid = kenOrGlenn
    p.student = studentID
    p.second_reader = secondreader
    now = datetime.datetime.now()

    p.demodate = now.strftime('%Y-%m-%d')
    p.demotime = "23:19"
    p.save()



# projectid = models.PositiveIntegerField(null=False)
# 	title = models.CharField(max_length=250, null=False)
# 	supervisor = models.CharField(max_length=250, null=False)
# 	supervisorid = models.PositiveIntegerField(null=False)
# 	student = models.PositiveIntegerField(null=False)
# 	second_reader = models.PositiveIntegerField(null=True) 
# 	demodate = models.DateField(("Date"), blank=True)
# 	demotime = models.TimeField(("Time"), blank=True)
# 	demoorganiser = models.PositiveIntegerField(null=True)
# 	demolocation = models.CharField(max_length=50, null=True)
# 	readerOneHasMarked = models.BooleanField(default=False, null=False)
# 	readerTWoHasMarked = models.BooleanField(default=False, null=False)
# 	readerOneMark = models.PositiveIntegerField(default=0, null=False)
# 	readerTWoMark = models.PositiveIntegerField(default=0, null=False)
# 	differenceInMarks = models.PositiveIntegerField(default=0, null=False)
# 	allowedDifferenceInMarks = models.PositiveIntegerField(default=10, null=False)
# 	readerOneHasDraft = models.BooleanField(default=False, null=False)
# 	readerTWoHasDraft = models.BooleanField(default=False, null=False)
# 	readerOne = models.CharField(default='', max_length=250, null=False)
# 	readerTWo = models.CharField(default='', max_length=250, null=False)
# 	readerOneEmail = models.CharField(default='', max_length=250, null=False)
# 	readerTWoEmail = models.CharField(default='', max_length=250, null=False)
# 	course = models.PositiveIntegerField(default=33, null=False) # default course is ICSProj