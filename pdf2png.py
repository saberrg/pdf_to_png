import sys, fitz  # import the bindings
#fname = sys.argv[1]  # get filename from command line
doc = fitz.open("some.pdf")  # open document
for page in doc:  # iterate through the pages
    pix = page.get_pixmap()  # render page to an image
    pix.save("page-%i.png" % page.number)  # store image as a PNG
