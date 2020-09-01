import json
import csv
import numpy as np
import shutil

from PIL import Image

for year in ["1999","2003"]:

    
    byid = {}
    bymeaning = {}

    with open(year + "/dumas-dutil-" + year + ".csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            byid[row["id"]] = row
            slug = "dumas-dutil-" + year + "_" + row["type"] + "_" + row["category"] + "_" + row["meaning"]
            newfn = slug + ".png"
            shutil.copy2(year + "/dumas-dutil-" + year + "-" + row["id"] + ".png", year + "/" + newfn)

            image = Image.open(year + "/dumas-dutil-" + year + "-" + row["id"] + ".png")
            binarified = image.convert("1")
            imagebits = binarified.tobytes()

            bymeaning[slug] = list(imagebits)
            byid[row["id"]]["image"] = list(imagebits)
    

    concatenatedimage = Image.open(year + "/dumas-dutil-" + year + "-concatenated.png")
    binarified = concatenatedimage.convert("1")
    imagebits = binarified.tobytes()

    with open(year + "/dumas-dutil-" + year + "-concatenated.json","w") as jsonfile:
        jsonfile.write(json.dumps(list(imagebits)))

    with open(year + "/dumas-dutil-" + year + "-by-id.json","w") as jsonfile:
        jsonfile.write(json.dumps(byid))

    with open(year + "/dumas-dutil-" + year + "-by-meaning.json","w") as jsonfile:
        jsonfile.write(json.dumps(bymeaning))

    with open(year + "/dumas-dutil-" + year + "-by-id.h","w") as hfile:
        for (key,val) in byid.items():
            hfile.write('uint8_t dumas_dutil_')
            hfile.write(year)
            hfile.write('_' + key)
            hfile.write('[] = {') 

            for element in val["image"]:
                hfile.write('%d, ' % element)
                
            hfile.write('};\n')

    with open(year + "/dumas-dutil-" + year + "-by-meaning.h","w") as hfile:
        for (key,val) in bymeaning.items():
            hfile.write('uint8_t ' + key.replace("-","_"))
            hfile.write('[] = {') 

            for element in val:
                hfile.write('%d, ' % element)
                
            hfile.write('};\n')


    with open(year + "/dumas-dutil-" + year + "-concatenated.h","w") as hfile:

        hfile.write('uint8_t dumas_dutil_concatenated_')
        hfile.write(year)
        hfile.write('[] = {') 

        for element in imagebits:
            hfile.write('%d, ' % element)
            
        hfile.write('};')

