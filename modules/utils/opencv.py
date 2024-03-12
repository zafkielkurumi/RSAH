import logging
import cv2


def imgShape(path):
  """
    模拟器分辨率统一为1280*720,这样查图的点位统一
  """
  img = cv2.imread(path)
  if img.shape[0] == 720 and img.shape[1] == 1280:
    return True
  else:
    print("模拟器分辨率应为1280*720")
    raise Exception("模拟器分辨率应为1280*720")

def match_image(source, target, showResult = False):
    """
      匹配图片,并返回中心点位
    """
    screenshot = cv2.imread(source)
    
    pattern = cv2.imread(target, cv2.IMREAD_UNCHANGED)  # 读取包含透明通道的模板图像
    result = cv2.matchTemplate(screenshot, pattern[:,:,:3], cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    h, w, _ = pattern.shape
    top_left = max_loc
    # get the center of the pattern
    center_x = top_left[0] + w // 2
    center_y = top_left[1] + h // 2
    bottom_right = (top_left[0] + w, top_left[1] + h)
    if showResult:
      # draw a rectangle on the screenshot
      cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
      # draw a circle on the center of the pattern
      cv2.circle(screenshot, (center_x, center_y), 10, (0, 0, 255), -1)
      print(center_x, center_y)
      cv2.imshow('Matched Screenshot', screenshot)
      cv2.waitKey(0)
      cv2.destroyAllWindows()        
    # 结果值超过0.8认为符合
    print("max_val: ", max_val)
    if(max_val >= 0.75):
        return (True, (center_x, center_y))
    return (False, (0, 0))
