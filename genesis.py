import os
import glob
from PIL import Image
import qrcode


def file_size(filePath):
    with open(filePath, 'r') as file:
        filename = file.read()
        len_chars = sum(len(word) for word in filename)
        print('The file has '+str(len_chars)+' characters.')
        return len_chars


def get_key(fp):
    filename = os.path.splitext(os.path.basename(fp))[0]
    int_part = filename.split()[0]
    return int(int_part)


def makeQR(text):
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

    with open(text, 'r') as f:
        for index, char in enumerate(f.read()):
            print(char, end="")
            qr.add_data(char)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            img.save("./files/images/"+str(index)+".png")
    f.close()

    print("Done.")


def makeGIF(name):
    print('Making a GIF out of images')
    frames = []
    imgs = sorted(glob.glob("./files/images/*.png"), key=get_key)

    for i in imgs:
        new_frame = Image.open(i)
        res_frame = new_frame.resize((512, 512))
        frames.append(res_frame)

    frames[0].save('./files/'+name+'.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=50, loop=0)
    print('Done.')


text_file = './files/text/lorem.txt'

def main():
    file_size(text_file)
    try:
        makeQR(text_file)
    except Exception as e:
        print(e)
    makeGIF('lorem')


main()
