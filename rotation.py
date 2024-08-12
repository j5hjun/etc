from PIL import Image
import os
from tqdm import tqdm

path = "C:\\Users\\hjcho\\Pictures\\이기적"
save_path = "C:\\Users\\hjcho\\Pictures\\이기적_최종"
if not os.path.exists(save_path):
            os.makedirs(save_path)

for file_num in tqdm(range(1, 781)):
    file = 'capture'+str(file_num)+'.png' # 파일 이름에 맞게 작성
    if file.endswith('.png'):
        img = Image.open(path + '\\' + file)
        rotated_img = img.rotate(-90, expand=True) # 검정색 공백 없이
        rotated_img.save(os.path.join(save_path, str(file_num) + '.png'))