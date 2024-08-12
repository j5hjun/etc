import pyautogui as pag
from PIL import ImageGrab
import time

# time.sleep(5)
# print(pag.position()) # 마우스 포인터 좌표 출력

time.sleep(2)
left_top = (315, 81) # 캡처할 영역 왼쪽 위
right_bottom = (1605, 1024) # 캡처할 영역 오른쪽 아래
left_top_x = left_top[0]
left_top_y = left_top[1]
capture_width = right_bottom[0]-left_top[0]
capture_height = right_bottom[1]-left_top[1]
i = 1

while True:
    if i < 781: # 페이지 수 + 1
        time.sleep(1.5)
        path = r"C:\Users\hjcho\Pictures\이기적\capture{0}.png".format(i)
        pag.screenshot(path, region=(left_top_x, left_top_y, capture_width, capture_height))
        pag.moveTo(1887, 537)
        pag.click()
        i += 1

    else:
        break