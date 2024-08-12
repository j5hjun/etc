import os
from tqdm import tqdm
from PIL import Image

path = "C:\\Users\\hjcho\\Pictures\\이기적_최종"
files = os.listdir(path)

img_list = []


for file_num in tqdm(range(1, 781)):
    file = str(file_num)+'.png' # 파일 이름에 맞게 작성
    img = Image.open(path + '\\' + file)
    img_1 = img.convert('RGB')
    img_list.append(img_1)

img_list[0].save("C:/Users/hjcho/Pictures/이기적_빅데기.pdf",
                 save_all=True,
                 append_images=img_list[1:])