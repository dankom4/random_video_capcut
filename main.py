import random
import os
import json
import time
import uuid

import keyboard
import pyautogui
import subprocess
from PIL import Image
from mutagen.mp3 import MP3
from dotenv import load_dotenv

load_dotenv()


project_path = os.getenv('PROJECT_PATH')


time_video = int(os.getenv('TIME_VIDEO'))


class Picture:
    @staticmethod
    def get_random_video(def_path):
        random_file = os.listdir(def_path)
        path = f"{def_path}/{random.choice(random_file)}"
        name = path.split("/")[-1]
        return name, path

    @staticmethod
    def get_size(path):
        with Image.open(path) as img:
            width, height = img.size
        return width, height

    @staticmethod
    def get_new_fail(name, path, width, height, times):
        with open(f"{project_path}\draft_meta_info.json",
                  "r", encoding="utf-8") as file:
            f = file.read()
            my_json = json.loads(f)
            my_json["draft_materials"][0]["value"].append({"create_time": time.time(), "duration": times,
                                                           "extra_info": name, "file_Path": path, "height": height,
                                                           "id": f"{str(uuid.uuid4())}", "import_time": time.time(),
                                                           "import_time_ms": time.time_ns(), "item_source": 1,
                                                           "md5": "", "metetype": "photo",
                                                           "roughcut_time_range": {"duration": -1, "start": -1},
                                                           "sub_time_range": {"duration": -1, "start": -1},
                                                           "type": 0, "width": width})
            return my_json

    @staticmethod
    def write_new_fail(data):
        with open(f"{project_path}\draft_meta_info.json",
                  "w", encoding="utf-8") as file_write:
            file_write.write(json.dumps(data))

    @staticmethod
    def get_new_data(name, path, width, height, times, start_time):

        with open(f"{project_path}\draft_content.json",
                  "r", encoding="utf-8") as file_read:
            id_file = f"{uuid.uuid4()}"
            f = file_read.read()
            my_json = json.loads(f)
            ratio = ((width/9)*16)/height
            my_json["materials"]["videos"].append({"aigc_type": "none", "audio_fade": None, "cartoon_path": "",
                                                   "category_id": "", "category_name": "local", "check_flag": 63487,
                                                   "crop": {"lower_left_x": 0.0, "lower_left_y": 1.0, "lower_right_x": 1.0,
                                                            "lower_right_y": 1.0, "upper_left_x": 0.0, "upper_left_y": 0.0,
                                                            "upper_right_x": 1.0, "upper_right_y": 0.0},
                                                   "crop_ratio": "free", "crop_scale": 1.0, "duration": 10_800_000_000,
                                                   "extra_type_option": 0, "formula_id": "", "freeze": None,
                                                   "gameplay": None, "has_audio": False, "height": height,
                                                   "id": id_file,
                                                   "intensifies_audio_path": "", "intensifies_path": "",
                                                   "is_ai_generate_content": False, "is_copyright": False,
                                                   "is_unified_beauty_mode": False, "local_id": "", "local_material_id": "",
                                                   "material_id": "", "material_name": name, "material_url": "",
                                                   "matting": {"flag": 0, "has_use_quick_brush": False,
                                                               "has_use_quick_eraser": False, "interactiveTime": [],
                                                               "path": "", "strokes": []}, "media_path": "",
                                                   "object_locked": None, "origin_material_id": "", "path": path,
                                                   "picture_from": "none", "picture_set_category_id": "",
                                                   "picture_set_category_name": "", "request_id": "",
                                                   "reverse_intensifies_path": "", "reverse_path": "",
                                                   "smart_motion": None, "source": 0, "source_platform": 0,
                                                   "stable": {"matrix_path": "", "stable_level": 0,
                                                              "time_range": {"duration": times, "start": 0}}, "team_id": "",
                                                   "type": "photo", "video_algorithm": {"algorithms": [], "deflicker": None,
                                                                                        "motion_blur_config": None,
                                                                                        "noise_reduction": None, "path": "",
                                                                                        "quality_enhance": None,
                                                                                        "time_range": None}, "width": width}
                                                  )

            if my_json.get('tracks') == []:
                my_json['tracks'] = [{'attribute': 0, 'flag': 0, 'id': f'{uuid.uuid4()}',
                                     'is_default_name': True, 'name': '', 'segments': [], 'type': 'video'}]
            my_json['tracks'][0]['segments'].append({'cartoon': False, 'clip': {'alpha': 1.0, 'flip': {'horizontal': False,
                                                                                                       'vertical': False},
                                                                                'rotation': 0.0,
                                                                                'scale': {'x': round(ratio, 4),
                                                                                          'y': round(ratio, 4)},
                                                                                'transform': {'x': 0.0, 'y': 0.0}},
                                                     'common_keyframes': [], 'enable_adjust': True,
                                                     'enable_color_curves': True, 'enable_color_match_adjust': False,
                                                     'enable_color_wheels': True, 'enable_lut': True,
                                                     'enable_smart_color_adjust': False, 'group_id': '',
                                                     'hdr_settings': {'intensity': 1.0, 'mode': 1, 'nits': 1000},
                                                     "id": str(uuid.uuid4()), 'intensifies_audio': False,
                                                     'is_placeholder': False, 'is_tone_modify': False, 'keyframe_refs': [],
                                                     'last_nonzero_volume': 1.0, 'material_id': id_file, 'render_index': 0,
                                                     'responsive_layout': {'enable': False, 'horizontal_pos_layout': 0,
                                                                           'size_layout': 0, 'target_follow': '',
                                                                           'vertical_pos_layout': 0}, 'reverse': False,
                                                     'source_timerange': {'duration': times, 'start': 0}, 'speed': 1.0,
                                                     'target_timerange': {'duration': times, 'start': start_time},
                                                     'template_id': '', 'template_scene': 'default', 'track_attribute': 0,
                                                     'track_render_index': 0, 'uniform_scale': {'on': True, 'value': 1.0},
                                                     'visible': True, 'volume': 1.0}
                                                    )
        return my_json

    @staticmethod
    def write_new_data(data):
        with open(f"{project_path}\draft_content.json",
                  "w", encoding="utf-8") as file_write:
            file_write.write(json.dumps(data))


class Sound:
    @staticmethod
    def get_random_sound(path):
        random_file = os.listdir(path)
        path = f"{path}/{random.choice(random_file)}"
        name = path.split("/")[-1]
        return name, path

    @staticmethod
    def get_times(path):
        mp3 = MP3(path)
        times = mp3.info.length
        return int(times*1000000)

    @staticmethod
    def get_new_fail(name, path, times):
        with open(f"{project_path}\draft_meta_info.json",
             "r", encoding="utf-8") as file_read:
            id_file = f"{str(uuid.uuid4())}"
            f = file_read.read()
            my_json = json.loads(f)
            my_json["draft_materials"][0]["value"].append({"create_time": time.time(), "duration": times,
                                                           "extra_info": name, "file_Path": path, "height": 0,
                                                           "id": id_file, "import_time": time.time(),
                                                           "import_time_ms": time.time_ns(), "item_source": 1,
                                                           "md5": "", "metetype": "music",
                                                           "roughcut_time_range": {"duration": times, "start": -1},
                                                           "sub_time_range": {"duration": -1, "start": -1},
                                                           "type": 0, "width": 0})
            return my_json, id_file

    @staticmethod
    def write_new_fail(datas):
        with open(f"{project_path}\draft_meta_info.json",
                  "w", encoding="utf-8") as file_write:
            file_write.write(json.dumps(datas))

    @staticmethod
    def get_new_data(name, path, times, start_time, id_sounds):
        with open(f"{project_path}\draft_content.json",
                  'r', encoding='utf-8') as file_read:
            id_file = f"{uuid.uuid4()}"
            f = file_read.read()
            my_json = json.loads(f)
            my_json["materials"]['audios'].append(
                {'app_id': 0, 'category_id': '', 'category_name': 'local', 'check_flag': 1,
                 'duration': times, 'effect_id': '', 'formula_id': '', 'id': id_file,
                 'intensifies_path': '', 'is_ai_clone_tone': False, 'is_ugc': False,
                 'local_material_id': id_sounds, 'music_id': f'{uuid.uuid4()}',
                 'name': name, 'path': path, 'query': '', 'request_id': '',
                 'resource_id': '', 'search_id': '', 'source_platform': 0, 'team_id': '',
                 'text_id': '', 'tone_category_id': '', 'tone_category_name': '',
                 'tone_effect_id': '', 'tone_effect_name': '',
                 'tone_second_category_id': '', 'tone_second_category_name': '',
                 'tone_speaker': '', 'tone_type': '', 'type': 'extract_music',
                 'video_id': '', 'wave_points': []
                 })
            if my_json.get('tracks') == []:
                my_json['tracks'] = [{'attribute': 0, 'flag': 0, 'id': f'{uuid.uuid4()}',
                                      'is_default_name': True, 'name': '', 'segments': [], 'type': 'video'},
                                     {'attribute': 0, 'flag': 0, 'id': f'{uuid.uuid4()}',
                                      'is_default_name': True, 'name': '', 'segments': [], "type": "audio"}
                                     ]
            my_json['tracks'][1]['segments'].append({'cartoon': False, 'clip': None, 'common_keyframes': [],
                                                     'enable_adjust': False, 'enable_color_curves': True,
                                                     'enable_color_match_adjust': False, 'enable_color_wheels': True,
                                                     'enable_lut': False, 'enable_smart_color_adjust': False,
                                                     'group_id': '', 'hdr_settings': None, 'id': str(uuid.uuid4()),
                                                     'intensifies_audio': False, 'is_placeholder': False,
                                                     'is_tone_modify': False, 'keyframe_refs': [],
                                                     'last_nonzero_volume': 1.0, 'material_id': id_file,
                                                     'render_index': 0, 'responsive_layout': {'enable': False,
                                                                                              'horizontal_pos_layout': 0,
                                                                                              'size_layout': 0,
                                                                                              'target_follow': '',
                                                                                              'vertical_pos_layout': 0},
                                                     'reverse': False,
                                                     'source_timerange': {'duration': times, 'start': 0},
                                                     'speed': 1.0,
                                                     'target_timerange': {'duration': times, 'start': start_time,
                                                                          'template_id': '',
                                                                          'template_scene': 'default',
                                                                          'track_attribute': 0,
                                                                          'track_render_index': 0,
                                                                          'uniform_scale': None,
                                                                          'visible': True, 'volume': 1.0}})
        return my_json

    @staticmethod
    def write_new_data(datas):
        with open(f"{project_path}\draft_content.json",
                  "w", encoding="utf-8") as file_write:
            file_write.write(json.dumps(datas))


def main(num, end_time):
    sound = Sound()
    name2, path2 = sound.get_random_sound(os.getenv(f'PATH_SOUND{num}'))
    times1 = sound.get_times(path2)
    data, id_sound = sound.get_new_fail(name2, path2, times1)
    sound.write_new_fail(data)
    sound.write_new_data(sound.get_new_data(name2, path2, times1, end_time, id_sound))
    pictures = Picture()
    name1, path1 = pictures.get_random_video(os.getenv(f'PATH_PICTURE{num}'))
    width1, height1 = pictures.get_size(path1)
    pictures.write_new_fail(pictures.get_new_fail(name1, path1, width1, height1, time_video))
    pictures.write_new_data(pictures.get_new_data(name1, path1, width1, height1, times=time_video, start_time=end_time))
    end_time += time_video
    return end_time


def reset():

    with open(f"{project_path}\draft_meta_info.json",
              "r", encoding="utf-8") as file:
        f1 = file.read()
        my_json = json.loads(f1)
        my_json["draft_materials"][0]["value"] = []

    with open(f"{project_path}\draft_meta_info.json",
              "w", encoding="utf-8") as file_write:
        file_write.write(json.dumps(my_json))

    with open(f"{project_path}\draft_content.json",
              "r", encoding="utf-8") as file2:
        f2 = file2.read()
        my_json = json.loads(f2)
        my_json["materials"]["videos"] = []
        my_json["materials"]['audios'] = []
        my_json['tracks'] = [{'attribute': 0, 'flag': 0, 'id': f'{uuid.uuid4()}',
                              'is_default_name': True, 'name': '', 'segments': [], 'type': 'video'},
                             {'attribute': 0, 'flag': 0, 'id': f'{uuid.uuid4()}',
                              'is_default_name': True, 'name': '', 'segments': [], "type": "audio"}]

    with open(f"{project_path}\draft_content.json",
              "w", encoding="utf-8") as file_write2:
        file_write2.write(json.dumps(my_json))


reset()
end_times = 0
for _ in range(1, 6):
    end_times = main(_, end_times)


subprocess.call(['C:/Users/AsRock/AppData/Local/CapCut/Apps/CapCut.exe'])
time.sleep(3)
pyautogui.moveTo(280, 350)
pyautogui.click()
time.sleep(2)
keyboard.press("ctrl+e")
keyboard.release("ctrl+e")
time.sleep(2)
keyboard.press('enter')
keyboard.release('enter')
time.sleep(0.5)
pyautogui.click(1280, 720)
keyboard.press('esc')
keyboard.release('esc')
keyboard.press('ctrl+alt+q')
keyboard.release('ctrl+alt+q')

















































