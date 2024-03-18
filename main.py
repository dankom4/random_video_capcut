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

subprocess.call(['C:/Users/AsRock/AppData/Local/CapCut/Apps/CapCut.exe'])
for _ in range(int(os.getenv('COUNT'))):
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

    class Text:

        @staticmethod
        def add_text_in_content1(time_end, text):
            rgb_color = [round(random.random(), 6) for _ in range(3)]
            hex_color = '#' + ''.join(map(lambda i: f"{int(i):02x}", map(lambda x: x * 100, rgb_color)))

            with open(
                    r'C:\Users\AsRock\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\0305\draft_content.json') as f:
                id_text = f'{uuid.uuid4()}'
                f1 = f.read()
                f2 = json.loads(f1)
                pupu = {'add_type': 0, 'alignment': 1, 'background_alpha': 1.0,
                        'background_color': '', 'background_height': 0.14,
                        'background_horizontal_offset': 0.0, 'background_round_radius': 0.0,
                        'background_style': 0, 'background_vertical_offset': 0.0,
                        'background_width': 0.14, 'bold_width': 0.0, 'border_alpha': 1.0,
                        'border_color': '#000000', 'border_width': 0.08,
                        'caption_template_info': {'category_id': '', 'category_name': '',
                                                  'effect_id': '', 'request_id': '',
                                                  'resource_id': '', 'resource_name': ''},
                        'check_flag': 7, 'combo_info': {'text_templates': []},
                        'content': '{"text":"pipi","styles":[{"fill":{"content":{"solid":{"color":[1,1,1]}}},"font":{"path":"C:/Users/AsRock/AppData/Local/CapCut/Apps/3.5.0.1268/Resources/Font/SystemFont/en.ttf","id":""},"strokes": [{"content":{"solid":{"color":[0,0,0]}},"width":0.08}],"size":30,"range":[0,100]}]}',
                        'fixed_height': -1.0, 'fixed_width': -1.0,
                        'font_category_id': '', 'font_category_name': '',
                        'font_id': '', 'font_name': '',
                        'font_path': 'C:/Users/AsRock/AppData/Local/CapCut/Apps/3.5.0.1268/Resources/Font/SystemFont/en.ttf',
                        'font_resource_id': '', 'font_size': 1.0,
                        'font_source_platform': 0, 'font_team_id': '',
                        'font_title': 'none', 'font_url': '', 'fonts': [],
                        'force_apply_line_max_width': False, 'global_alpha': 1.0,
                        'group_id': '', 'has_shadow': False,
                        'id': id_text, 'initial_scale': 1.0,
                        'is_rich_text': False, 'italic_degree': 0, 'ktv_color': '',
                        'language': '', 'layer_weight': 1, 'letter_spacing': 0.0, 'line_feed': 1,
                        'line_max_width': 0.82, 'line_spacing': 0.02, 'name': '',
                        'original_size': [], 'preset_category': '', 'preset_category_id': '',
                        'preset_has_set_alignment': False, 'preset_id': '', 'preset_index': 0,
                        'preset_name': '', 'recognize_task_id': '', 'recognize_type': 0,
                        'relevance_segment': [], 'shadow_alpha': 0.8, 'shadow_angle': -45.0,
                        'shadow_color': '', 'shadow_distance': 8.0,
                        'shadow_point': {'x': 1.0182337649086284, 'y': -1.0182337649086284},
                        'shadow_smoothing': 1.0, 'shape_clip_x': False,
                        'shape_clip_y': False, 'style_name': '', 'sub_type': 0,
                        'subtitle_keywords': None, 'text_alpha': 1.0,
                        'text_color': '#FFFFFF', 'text_curve': None,
                        'text_preset_resource_id': '', 'text_size': 30,
                        'text_to_audio_ids': [], 'tts_auto_update': False, 'type': 'text',
                        'typesetting': 0, 'underline': False, 'underline_offset': 0.22,
                        'underline_width': 0.05, 'use_effect_default_color': True,
                        'words': {'end_time': [], 'start_time': [], 'text': []}}
                pip = json.loads(pupu['content'])
                pip['text'] = text
                pip['styles'][0]['fill']['content']['solid']['color'] = rgb_color
                pip['styles'][0]['size'] = int(os.getenv('SIZE_TEXT'))
                pip['styles'][0]['strokes']
                pip = json.dumps(pip)
                pupu['content'] = pip
                pupu['text_color'] = hex_color
                pupu['text_size'] = int(os.getenv('SIZE_TEXT'))

                f2['materials']['texts'].append(pupu)
                f2.get('tracks').insert(1,
                                        {'attribute': 0, 'flag': 0, 'id': f'{uuid.uuid4()}', 'is_default_name': True,
                                         'name': '',
                                         'segments': [
                                             {
                                                 'cartoon': False, 'clip': {'alpha': 1.0, 'flip': {'horizontal': False,
                                                                                                   'vertical': False},
                                                                            'rotation': 0.0,
                                                                            'scale': {'x': 1.0, 'y': 1.0},
                                                                            'transform': {'x': 0.0, 'y': 0.0}},
                                                 'common_keyframes': [], 'enable_adjust': False,
                                                 'enable_color_curves': True,
                                                 'enable_color_match_adjust': False, 'enable_color_wheels': True,
                                                 'enable_lut': False, 'enable_smart_color_adjust': False,
                                                 'extra_material_refs': [],
                                                 'group_id': '', 'hdr_settings': None,
                                                 'id': f'{uuid.uuid4()}', 'intensifies_audio': False,
                                                 'is_placeholder': False, 'is_tone_modify': False, 'keyframe_refs': [],
                                                 'last_nonzero_volume': 1.0,
                                                 'material_id': id_text, 'render_index': 14000,
                                                 'responsive_layout': {'enable': False, 'horizontal_pos_layout': 0,
                                                                       'size_layout': 0, 'target_follow': '',
                                                                       'vertical_pos_layout': 0}, 'reverse': False,
                                                 'source_timerange': None, 'speed': 1.0,
                                                 'target_timerange': {'duration': int(os.getenv('TIME_VIDEO')),
                                                                      'start': time_end},
                                                 'template_id': '',
                                                 'template_scene': 'default', 'track_attribute': 0,
                                                 'track_render_index': 0,
                                                 'uniform_scale': {'on': True, 'value': 1.0}, 'visible': True,
                                                 'volume': 1.0}], 'type': 'text'
                                         }
                                        )
                return f2

        @staticmethod
        def add_with_text_in_content(data):
            with open(r'C:\Users\AsRock\AppData\Local\CapCut\User Data\Projects\com.lveditor.draft\0305\draft_content.json', 'w') as f:
                f.write(json.dumps(data))


    def main(num, end_time):
        text = Text()
        text.add_with_text_in_content(text.add_text_in_content1(time_end=end_time, text=os.getenv(f'TEXT{num}')))
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
        pictures.write_new_data(pictures.get_new_data(name1, path1, width1, height1, times=time_video,
                                                      start_time=end_time))

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

    def open_project():
        time.sleep(3)
        pyautogui.moveTo(280, 350)
        pyautogui.click()

    def close_project():
        time.sleep(2)
        keyboard.press("ctrl+e")
        keyboard.release("ctrl+e")
        time.sleep(2)
        keyboard.press('enter')
        keyboard.release('enter')
        time.sleep(3)
        pyautogui.click(1280, 720)
        keyboard.press('esc')
        keyboard.release('esc')
        keyboard.press('ctrl+alt+q')
        keyboard.release('ctrl+alt+q')

    def add_subtitles():
        subtitles_x, subtitles_y = map(int, os.getenv('CORD_SUBTITLES').split())
        create_x, create_y = map(int, os.getenv('CORD_CREATE').split())
        language_x, language_y = map(int, os.getenv('CORD_LANGUAGE').split())
        language2_x, language2_y = map(int, os.getenv('CORD_LANGUAGE2').split())
        size_text_x, size_text_y = map(int, os.getenv('CORD_SIZE').split())
        basic_x, basic_y = map(int, os.getenv('CORD_BASIC').split())
        size_text = os.getenv('SIZE_TEXT')
        color_x, color_y = map(int, os.getenv('CORD_COLOR').split())
        color2_x, color2_y = map(int, os.getenv('CORD_COLOR2').split())
        stroke_x, stroke_y = map(int, os.getenv('CORD_STROKE').split())
        stroke_size_x, stroke_size_y = map(int, os.getenv('CORD_STROKE_SIZE').split())
        stroke_size = os.getenv('STROKE_SIZE')
        animation_x, animation_y = map(int, os.getenv('CORD_ANIMATION').split())
        captions_x, captions_y = map(int, os.getenv('CORD_CAPTIONS').split())
        animation_style_x, animation_style_y = map(int, os.getenv('ANIMATION_STYLE').split())

        time.sleep(2)
        for _ in range(2):
            keyboard.press('tab')
            keyboard.release('tab')
        time.sleep(0.1)
        pyautogui.click(subtitles_x, subtitles_y)
        time.sleep(0.2)
        pyautogui.click(language_x, language_y)
        time.sleep(0.3)
        pyautogui.moveTo(language2_x, language2_y)
        time.sleep(0.3)
        for scroll_count in range(5):
            pyautogui.scroll(-200)
        pyautogui.moveRel(0, 30)
        time.sleep(1.5)
        pyautogui.click()
        pyautogui.click(create_x, create_y)
        time.sleep(10)
        pyautogui.click(basic_x, basic_y)
        pyautogui.click(size_text_x, size_text_y)
        keyboard.press('backspace')
        time.sleep(0.1)
        keyboard.release('backspace')
        time.sleep(0.05)
        keyboard.write(size_text)
        pyautogui.click(color_x, color_y)
        time.sleep(0.1)
        pyautogui.click(color2_x, color2_y)
        time.sleep(0.1)
        pyautogui.click(color_x, color_y)
        pyautogui.scroll(-1000)
        time.sleep(1)
        pyautogui.click(stroke_x, stroke_y)
        time.sleep(0.5)
        pyautogui.click(stroke_size_x, stroke_size_y)
        keyboard.press('backspace')
        time.sleep(0.1)
        keyboard.release('backspace')
        keyboard.write(stroke_size)
        pyautogui.click(animation_x, animation_y)
        time.sleep(0.1)
        pyautogui.click(captions_x, captions_y)
        time.sleep(0.1)
        pyautogui.click(animation_style_x, animation_style_y)
        time.sleep(2)


    open_project()
    close_project()
















































