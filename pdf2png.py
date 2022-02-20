import sys, fitz 
doc = fitz.open("some.pdf")  # Enter name of pdf
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("page-%i.png" % page.number)  # store image as a PNG
    
    
    # PDF must be in the same directory as this program
    # PNG will be outputted in the same direectory
