from voc_eval import voc_eval
import numpy as np
# hat
print("==========with_mask==========")
Hrec, Hpre, Hap = voc_eval('./results/{}.txt', 
               './VOCdevkit/VOC2007/Annotations/{}.xml', 
               '/content/colab_face_mask/2007_test.txt', 
               'with_mask', '.')
print("rec:", round(np.mean(Hrec), 4))
print("pre:", round(np.mean(Hpre), 4))
print(" ap:", round(np.mean(Hap), 4))
# person
print("========without_mask=========")
Prec, Ppre, Pap = voc_eval('./results/{}.txt', 
               './VOCdevkit/VOC2007/Annotations/{}.xml', 
               '/content/colab_face_mask/2007_test.txt', 
               'without_mask', '.')
print("rec:", round(np.mean(Prec), 4))
print("pre:", round(np.mean(Ppre), 4))
print(" ap:", round(np.mean(Pap), 4))
print("======================")
print("map:", round((np.mean(Hap) + np.mean(Pap)) / 2, 4))