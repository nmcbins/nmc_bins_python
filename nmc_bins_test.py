#from nmcbins import nmc_bins as bins
import nmcbins as bins
qid='p7INVIHYDQM'
bins.setQid(qid)

text_to_process = 'a male b'
b=bins.normalize(text_to_process)
print b

