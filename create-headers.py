import json
import numpy as np

from PIL import Image

for year in ["1999","2003"]:
    concatenatedimage = Image.open(year + "/dumas-dutil-" + year + "-concatenated.png")
    binarified = concatenatedimage.convert("1")
    imagebits = binarified.tobytes()

    with open(year + "/dumas-dutil-" + year + "-concatenated.json","w") as jsonfile:
        jsonfile.write(json.dumps(list(imagebits)))

    with open(year + "/dumas-dutil-" + year + "-concatenated.h","w") as hfile:

        hfile.write('uint8_t concatenated_')
        hfile.write(year)
        hfile.write('[] = {') 

        for element in imagebits:
            hfile.write('%d, ' % element)
            
        hfile.write('};')

