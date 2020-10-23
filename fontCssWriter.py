import os
def fontsAreReadyForFlask(fontsFolder):
    """
        Your project folder must be like
        >Project-Folder
        > > static
        > >|> > fonts
        > >|> >|> fontCssWriter.py -> run it in current folder
        > >|> > css

        When writing path way:
            Additionally use / 
            Don't use backslash \
    """
    entries = os.listdir(fontsFolder)
    css = ""
    for entry in entries:
        css+="@font-face {{font-family: {};src: url(\"".format(entry[:-4:])+"/static/fonts/{}".format(entry)+'\"'+");}\n"
        #print(css) 

    with open(fontsFolder[:-6:]+'/css/font.css','w') as f:
        f.write(css)
    print("It is Ready!")

fontsAreReadyForFlask("C:/Users/<user>/Desktop/Project-Folder/static/fonts")
