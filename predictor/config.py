BLUR = False
LABELS_PATH = r"D:\predictor_data\data\buildings"  # set_this
OBS_PATH = r"D:\predictor_data\data\observations"  # set_this
PADDING = 16
HEIGHT = 62
WIDTH = 60
DENSE = True
NUM_OF_OBS = 5
KERNEL_SIZE = 3
VAR = 1
OUTPUT_PATH_TOKEN = "6260"
MODELS_PATH = r"C:\Users\zwecher\Documents\mygit\Indoors_Capabilities\models_predictor\models_" + OUTPUT_PATH_TOKEN

BUILDING_NUM = "building_num"
BUILDING = "building"
OBS = "obs"
NEXT_OBS = "next_obs"
ACTION = "action"
REWARD = "reward"

HEIGHT += 2 * PADDING
WIDTH += 2 * PADDING

if HEIGHT % 8 != 0:
    HEIGHT = HEIGHT - HEIGHT % 8 + 8
if WIDTH % 8 != 0:
    WIDTH = WIDTH - WIDTH % 8 + 8
