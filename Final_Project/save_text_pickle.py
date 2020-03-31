import pickle
import time
import pandas as pd
import pynput
import random
import pyperclip

from pynput.mouse import Button
from pynput.keyboard import Key

restaurant_df = pd.read_pickle("restaurant_df_pickle.pkl")
id_list = pickle.load(open("id_list.p", "rb"))

# id_list = []

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
prev_message = ""

print("Here Here")

for i in range(restaurant_df.size) :
    ID = restaurant_df.iloc[i].ID

    if ID in id_list :
        continue

    print("Venue Number:", i)
    print(ID)

    ### Step 1: Move Mouse to Default Position
    time.sleep(1 * random.random() )
    mouse.position = (800,435)

    ### Step 2: Move Mouse to CMD to copy ID
    # time.sleep(1 * random.random() )
    # mouse.click(Button.left, 2)
    #
    # time.sleep(1 * random.random() )
    # with keyboard.pressed(Key.ctrl):
    #     keyboard.press('c')

    pyperclip.copy(ID)

    ### Step 3: Move Mouse to Foursquare to Paste ID and Search
    time.sleep(1 * random.random() )
    mouse.position = (900,330)

    time.sleep(1 * random.random() )
    mouse.click(Button.left, 2)

    time.sleep(1 * random.random() )
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')

    time.sleep(1 * random.random() )
    mouse.position = (1200,330)

    time.sleep(1 * random.random() )
    mouse.click(Button.left, 1)

    ### Step 4: Press Control+A to obtain all text
    time.sleep(3 )
    mouse.position = (500,380)

    time.sleep(1 * random.random() )
    mouse.click(Button.left, 1)

    time.sleep(1 * random.random() )
    with keyboard.pressed(Key.ctrl):
        keyboard.press('a')

    time.sleep(1 * random.random() )
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')

    ### Step 5: Paste Text on dummy file and press Ctr+S
    # time.sleep(1 * random.random() )
    # mouse.position = (500,500)
    #
    # time.sleep(1 * random.random() )
    # mouse.click(Button.left, 1)

    time.sleep(1 * random.random() )
    mouse.position = (600,550)

    time.sleep(1 * random.random() )
    mouse.click(Button.left, 1)

    time.sleep(1 * random.random() )
    with keyboard.pressed(Key.ctrl):
        keyboard.press('a')

    time.sleep(1 * random.random() )
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')

    time.sleep(1 * random.random() )
    with keyboard.pressed(Key.ctrl):
        keyboard.press('s')

    ### Error Check
    if prev_message == pyperclip.paste() or "No internet" in pyperclip.paste() or "Response\r\n{" not in pyperclip.paste():
        print("Error Network Timeout")
        break
    else :
        prev_message = pyperclip.paste()

    ### Step 6: Convert that Text into a Pickle File
    test = open('dummy_text.txt' , 'r', encoding="utf-8")
    file_name = "Text_Dump_" + str(i)
    pickle.dump( test.read() , open( "Restaurant_Info_Text_Pickle/Text_Dump_%d.p" %(i), "wb" ) )

    id_list.append(ID)
    pickle.dump( id_list, open( "id_list.p", "wb" ) )

    time.sleep(1 * random.random() )
    mouse.position = (800,535)

    time.sleep(1 * random.random() )
    mouse.click(Button.left, 1)
    time.sleep(3)
