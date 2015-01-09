#!/usr/bin/python
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pyfits
import numpy as np
from numpy import *
#import fileinput
from glob import glob
from scipy.interpolate import interp1d
import time
import pickle
t0=time.clock()



#fnames = glob('ptc0/ptc_P0_*.fits');
fnames=glob('flats/flat_T_*.fits')
#fnames=glob('tptc/image_*.fits');
l=len(fnames);
s=np.zeros(l);
n=np.zeros(l);
X1=100;
X2=150;
Y1=200;
Y2=500;
hdu_bias=pyfits.open(fnames[0]);
adc_level=np.mean(hdu_bias[0].data);
print adc_level;
for i in np.arange(0,l):
    hdu=pyfits.open(fnames[i]);
    n[i]=np.var(hdu[0].data[X1:X2,Y1:Y2]);
    s[i]=np.mean(hdu[0].data[X1:X2,X1:X2]);

print s # lambda = 280 photons/sec
z=polyfit(s,n,1);
print 'z=',z
p=poly1d(z);   
equation=str(np.round(z[0],2)) + 'x' + '+' + str(np.round(z[1],2)); 
print equation
print fnames

plt.loglog(s, n,'b-');
plt.ylabel('LOG NOISE, ADU');
plt.xlabel('LOG SIGNAL ADU');
plt.title('Theorical Photon Transfer Curve')
#f = interp1d(s, n, kind='quadratic');
 
#s_new=np.arange(10,60000,4800);
#print s_new
#x_new=f(s_new)
#plt.plot(s_new,n_new,'k.');
#plt.loglog(s,p(s),'g')
#slope,intercept = plt.loglog(s,p(s),'b.',basex=10,basey=10);
#plt.ylim([40,10**3]);
#plt.xlim([10**3,10**5]);

plt.grid(True,which="both",ls="--")
plt.savefig('tptc.png')
print time.clock()-t0;
plt.show();



               






