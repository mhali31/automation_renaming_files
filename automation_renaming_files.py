import os
import time
'''this script was used to rename the files'''
# an easy way to get folder location is to drag folder into cmd or gitbash
os.chdir(input("insert the directory of files: "))

#print(os.getcwd())
''' to get the name of each file in the directory '''
for f in os.listdir():
    #print(f)
    '''to split the name of the file from the extension'''
    file_name, file_ext = os.path.splitext(f)
    '''to split filename into track number, artist name, title'''
    f_num, f_artist, f_title = file_name.split("-")

    '''removing the underscores from the title and replacing them with spaces
    and changing the words to title case'''
    f_title = f_title.title().replace("_", " ")
    f_artist = f_artist.title()

    '''print out new file name and assign it to variable'''
    print(f"{f_num} - {f_artist} - {f_title}{file_ext}")
    new_name = f"{f_num} - {f_artist} - {f_title}{file_ext}"
    '''rename the current file with new name'''
    os.rename(f, new_name)

    #time.sleep(2)
