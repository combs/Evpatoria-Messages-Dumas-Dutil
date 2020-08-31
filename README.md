# Evpatoria-Messages-Dumas-Dutil

Radio transmissions sent to nearby stars from Evpatoria, Ukraine, as part of the "Cosmic Call" in 1999 and 2003. 

![One page of the 1999 message](https://github.com/combs/Evpatoria-Messages-Dumas-Dutil/raw/master/1999/dumas-dutil-1999-119.png)

[More information](https://www.plover.com/misc/Dumas-Dutil/messages.pdf)

## Status

These are currently just PNGs in the same order as the above-linked PDF. I intend to categorize and label them, and transmogrify them to C header files. 

## Format

Processed and resized to black-and-white PNGs. 

Overall pages:

- 127-pixel wide PNGs

Individual glyphs:

- 5x7px PNGs (the 4x7 numbers from the 2003 message are padded with one white pixel to the right)

## Method

Extracted using `pdfimages` and converted to proper pixel dimensions and thresholded via XNView batch conversion:

- resize, Lancszos, sharpened. Outputs smeary-looking grayscale
- reduce brightness -20
- increase contrast +127
- increase contrast +127 again (catches edge case of rgb ~ 107-126)

## License

Public domain
