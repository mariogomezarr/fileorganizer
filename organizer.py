import os, shutil

def organizeit():

    fp = input('Write the path you want to organize: ')

    for root, dirs, files in os.walk(fp):
        root = root
        dirs = dirs
        files = files
        break

    for file in files:
        format = file.split('.')[-1].upper()
        
        os.makedirs(root + os.sep + format, exist_ok=True)
        shutil.move(os.path.join(root + os.sep + file), os.path.join(root + os.sep + format + os.sep + file))
    
    print("Done.")

if __name__ == '__main__':
    organizeit()