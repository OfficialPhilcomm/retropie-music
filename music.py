import os
import time
import random
import datetime
from pygame import mixer
import configparser

emulator_process_names = emulatornames = [
  'advmame',
  'ags',
  'alephone',
  'atari800',
  'basiliskll',
  'cannonball',
  'capricerpi',
  'cgenesis',
  'daphne',
  'dgen',
  'dosbox',
  'drastic',
  'eduke32',
  'fbzx',
  'frotz',
  'fuse',
  'gemrb',
  'gngeo',
  'gpsp',
  'hatari',
  'ioquake3',
  'jzintv',
  'kodi',
  'linapple',
  'lincity',
  'love',
  'mame',
  'micropolis',
  'moonlight',
  'mupen64plus',
  'nds',
  'openbor',
  'openmsx',
  'openttd',
  'opentyrian',
  'osmose',
  'pifba',
  'pisnes',
  'ppsspp',
  'reicast',
  'residualvm',
  'retroarch',
  'scummvm',
  'sdlpop',
  'simcoupe',
  'snes9x',
  'solarus',
  'steamlink.sh',
  'stella',
  'stratagus',
  'streaming_clien',
  'tyrquake',
  'uae4all2',
  'uae4arm',
  'uqm',
  'vice',
  'wolf4sdl',
  'wolf4sdl.sh',
  'xrick',
  'xroar',
  'zdoom']

config = configparser.ConfigParser()
config_file = '/opt/dev_philcomm/config.cfg'

def setup_config():
  if not os.path.isfile(config_file):
    create_config()
  config.read(config_file)

def create_config():
  config['general'] = { 'music_folder': '/home/pi/music' }
  with open(config_file, 'w') as cfg_file:
    config.write(cfg_file)

setup_config()

music_folder = config.get('general', 'music_folder') or '/home/pi/music'

music_folder_exists = os.path.isdir(music_folder)
if not music_folder_exists:
  os.mkdir(music_folder)
  print(f'Created {music_folder} folder as defined in {config_file}')

winter_folder_exists = os.path.isdir(f'{music_folder}/winter')
if winter_folder_exists and datetime.date.today().month == 12:
  music_folder = f'{music_folder}/winter'

max_volume = 0.6

sound_files = \
  [mp3 for mp3 in os.listdir(music_folder) \
  if mp3.endswith('.mp3') or mp3.endswith('.ogg')]

start_delay = 0
volumefadespeed = 0.02
restart = True

last_song_index = -1
current_song_index = -1

mixer.init()
random.seed()
current_volume = max_volume

def is_emulationstation_running():
  running = False
  pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
  for pid in pids:
    try:
      process_name = open(os.path.join('/proc' ,pid ,'comm'), 'rt').read()[:-1]
      if 'emulationstatio' in str(process_name):
        running = True
    except IOError:
      continue
  return running

while not is_emulationstation_running():
  time.sleep(1)

time.sleep(start_delay)

def wait_for_omx():
  pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
  for pid in pids:
    try:
      process_name = open(os.path.join('/proc', pid, 'comm'), 'rt').read()[:-1]
      if process_name == 'omxplayer' or process_name == 'omxplayer.bin':
        while os.path.exists('/proc/' + pid):
          time.sleep(1)
    except IOError:
      continue

wait_for_omx()

def stop_music():
  if mixer.music.get_busy():
    mixer.music.stop();

def get_random_song():
  song = random.randint(0, len(sound_files) - 1)
  while song == last_song_index and len(sound_files) > 1:
    song = random.randint(0, len(sound_files) - 1)
  return song

def is_emulator_running():
  emulator_process = dict()
  emulator_process['id'] = -1;
  pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

  for pid in pids:
    try:
      process_name = open(os.path.join('/proc', pid, 'comm'), 'rt').read()[:-1]
      is_running = False
      if process_name in emulator_process_names:
        is_running = True
      if is_running:
        emulator_process['id'] = pid
        emulator_process['name'] = process_name
        break
    except IOError:
      continue

  return emulator_process

while True:
  while not is_emulationstation_running():
    stop_music()
    time.sleep(10)

  if not mixer.music.get_busy():
    current_song_index = get_random_song()
    song = os.path.join(music_folder, sound_files[current_song_index])
    mixer.music.load(song)
    last_song_index = current_song_index
    mixer.music.set_volume(max_volume)
    mixer.music.play()
    print(f'Now playing: {song}')

  emulator_process = is_emulator_running()
  if emulator_process['id'] != -1:
    emulator_process_id = emulator_process['id']
    emulator_process_name = emulator_process['name']
    print(f'Emulator process called {str(emulator_process_name)} found. Start fading out the music...')

    while current_volume > 0:
      current_volume = current_volume - volumefadespeed
      if current_volume < 0:
        current_volume = 0
      mixer.music.set_volume(current_volume);
      time.sleep(0.05)
    
    if restart:
      mixer.music.stop()
    else:
      mixer.music.pause()
    print('Background music muted. Waiting for emulator to stop...')
    
    while os.path.exists('/proc/' + emulator_process_id):
      time.sleep(1);
    print('Emulator stopped, start back music')
    
    if not restart:
      mixer.music.unpause()
      while current_volume < max_volume: 
        current_volume = current_volume + volumefadespeed;
        if current_volume > max_volume:
          current_volume = max_volume
        mixer.music.set_volume(current_volume);
        time.sleep(0.05)
    print('Restored.')
    
    current_volume = max_volume

  time.sleep(1);

print('An error has occurred that has stopped music.py from executing.')
