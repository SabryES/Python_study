
import subprocess
import pyautogui




def Find_image(image_path):
    while True :
        pyautogui.sleep(5)
        try:
            if pyautogui.locateOnScreen(image_path,confidence=0.8) is not None:
                break
        except pyautogui.ImageNotFoundException:
            pyautogui.sleep(1)


link = "https://eg.indeed.com/jobs?q=embedded+systems&l"
subprocess.run([r"C:\Program Files\Google\Chrome\Application\chrome.exe", link])

Find_image(r"E:\embdede systen\Moatasem\Python\Tuple_set_dictonary_library\link.png")

pyautogui.click(pyautogui.locateCenterOnScreen(r"E:\embdede systen\Moatasem\Python\Tuple_set_dictonary_library\link.png",confidence=0.8))




# while True :
#     try:
#         if pyautogui.locateOnScreen("link.ping",confidence=0.8) is not None:
#             break
#     except pyautogui.ImageNotFoundException:
#         pyautogui.sleep(1)