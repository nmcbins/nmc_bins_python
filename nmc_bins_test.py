from nmc_bins_python import nmc_bins as bins
qid='LJdHrbt59Us'
bins.setQid(qid)

text_to_process = 'a male b'
b=bins.normalize(text_to_process)
print b

