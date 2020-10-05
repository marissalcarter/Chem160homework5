import math, time, random
import numpy as np
ntrials=10000000
t=time.process_time()
x1=np.random.random(ntrials)
y1=np.random.random(ntrials)
z1=np.random.random(ntrials)
x2=np.random.random(ntrials)
y2=np.random.random(ntrials)
z2=np.random.random(ntrials)
dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))
et=time.process_time()-t
print("dist =%9.6f  time=%f"% (dist, et))