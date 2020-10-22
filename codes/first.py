text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(":")
new = text[(ipos+1):]
print(float(new))
