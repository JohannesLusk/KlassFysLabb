import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy

# X = np.linspace(-2*np.pi, 2*np.pi, 1024)
# C, S = np.cos(X) , np.sin(X)

# plt.plot(X, C)
# plt.plot(X, S)
# plt.show()


with open("BrewstervinkelData.txt", "r") as data:
  xlist = []
  ylist = []
  for line in data: 
    line = line.split(",")
    xlist.append(int(line[0].strip()))
    ylist.append(float(line[1].strip()))
   


# X = np.linspace(0,90,1024)

plt.plot(xlist, ylist,'bo')
plt.show()


1000
980
972
959
946
932
914
902
890
877
862
850
838
823
807
796
783
771
758
745
732
719
705
690


679
665
650
638
626
613
600
588
574
560
549
536
523
510
496
483
470
456
444
430
417
405
390



378
364
350
339
325
311
298
286
271
258
245
232
220
206
192
179
166
153
140
126
113
100
110
123

137
152
164
176
192
205
219
233
245
258
272
286
299
311
324
340
355
368
378
394
407
420
447
460



464
492
496
509
522
535
547
563
576
590
601
612
629
640
655
666
680
693
710
722
735
750
762
777
787
800
815
825
836
848
862
876
889
904
917
929
945
958
974
980
989
995

