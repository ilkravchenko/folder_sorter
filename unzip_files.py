import os
import patoolib

def unzip_files(path):
    path += '/Archive'
    for file in os.listdir(path):
        try:
            name_of_file, ext = os.path.splitext(file)
            if not os.path.exists(path + '\\' + file):
                os.mkdir(path + name_of_file)
            patoolib.extract_archive(path + '\\' + file, outdir=path + '\\' + name_of_file)
        except:
            print("Can't extract files, because all files was extracted")
            break
