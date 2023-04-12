# 将 main.json 里面的base64音频解码为mp3

import base64
import json
# encode_string = base64.b64encode(open("./wav_raw/2.wav", "rb").read())
# print(encode_string)

with open("./data/main/main.json",'r') as load_f:
    load_dict = json.load(load_f)
    # print(load_dict)
    for mp3_name in load_dict:
        b64string = load_dict[mp3_name]
        b64string = b64string.split(",")[1]
        # print()
        mp3_file = open(mp3_name, "wb")
        decode_string = base64.b64decode(b64string)
        mp3_file.write(decode_string)
