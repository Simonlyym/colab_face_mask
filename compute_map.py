from voc_eval import voc_eval
import numpy as np
# hat
print("==========Hat==========")
Hrec, Hpre, Hap = voc_eval('./results/{}.txt', 
               './VOCdevkit/VOC2007/Annotations/{}.xml', 
               '/content/colab_darknet_yolo/2007_test.txt', 
               'hat', '.')
print("rec:", round(np.mean(Hrec), 4))
print("pre:", round(np.mean(Hpre), 4))
print(" ap:", round(np.mean(Hap), 4))
# person
print("========person=========")
Prec, Ppre, Pap = voc_eval('./results/{}.txt', 
               './VOCdevkit/VOC2007/Annotations/{}.xml', 
               '/content/colab_darknet_yolo/2007_test.txt', 
               'person', '.')
print("rec:", round(np.mean(Prec), 4))
print("pre:", round(np.mean(Ppre), 4))
print(" ap:", round(np.mean(Pap), 4))
print("======================")
print("map:", round((np.mean(Hap) + np.mean(Pap)) / 2, 4))