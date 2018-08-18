#!/usr/bin/python3
#update README.md file with contents of this repository


__doc__ = '''
Run this script each time update the README.md file
- to list the TOC of scripts in the same folder and subfolder
- hierachy of files as below:
.
├── ex_argparse2.py
├── ex_argparse.py
├── README.md
├── directory
└── update_readme.py

in each python file read the __shortdoc__ variable of each file.
REAMD.md had the line 'Talbe of contents'
'''

import os


def main():
    with open('README.md', 'wt') as f_readme:
        #append the header of README.md 
        #auto update and create the TOC then append to README.md
        for root, _, files in os.walk('.'):
            # lay duong dan tu /blob/master thu muc cha den ten file .py
            for f in files:
                extention = f[f.rfind('.'):]
                if extention == '.py':
                    with open(f, "rt") as fpy:
                        #read the second line, which content the short description of script
                        _temp = fpy.readline()
                        desc = fpy.readline().strip()
                        if not desc.startswith("#"):
                            desc = "Please change description of this script"
                        else:
                            desc = desc[1:]
                    desc_link = "* [{}](../blob/master/{})  \n".format(desc, os.path.join(root, f)[2:])
                    #print(desc_link)
                    f_readme.write(desc_link)
                    
        #append the footer of README.md


if __name__ == "__main__":
    main()