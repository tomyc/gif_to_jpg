import os
from PIL import Image
import glob
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def extractFrames(inGif, outFolder):
    if os.path.isdir('output')!=True:
        os.mkdir('output')
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.convert('RGB').save( '%s/%s-%s.jpg' % (outFolder, os.path.basename(inGif), nframes ) , 'JPEG')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True
    

def get_file_paths_with_a_string(dir_path, ext_to_find):
    return glob.glob(
        os.path.join(dir_path, "*{}".format(ext_to_find))
    )

if __name__ == "__main__":
    file_ext = '.gif'
    current_dir = os.getcwd()
    file_paths = get_file_paths_with_a_string(current_dir, file_ext)
    for file_path in file_paths:
        extractFrames(file_path, 'output')
