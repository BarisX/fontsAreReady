import os
def fontsAreReadyForFlask(fontsFolder):
    entries = os.listdir(fontsFolder)
    css = ""
    for entry in entries:
        css+="@font-face {{font-family: {};src: url(\"".format(entry[:-4:])+"{{ "+"url_for('static', filename='{}')".format(entry)+' }}\"'+");}\n"
        #print(css)

    with open(fontsFolder+'/font.css','w') as f:
        f.write(css)
    print("It is Ready!")

