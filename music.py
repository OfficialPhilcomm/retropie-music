import os
import time
import random
import datetime
from pygame import mixer
import logging
import confighelper
import processhelper

logging.basicConfig(
  filename='/opt/dev_philcomm/retropie_background_music.log', 
  level=logging.DEBUG,
  format='[%(asctime)s %(levelname)s] %(message)s',
  datefmt='%Y/%m/%d %I:%M:%S'
)

confighelper.setup_config()

music_folder = confighelper.get_music_folder()

music_folder_exists = os.path.isdir(music_folder)

while not music_folder_exists:
  time.sleep(1)
  music_folder_exists = os.path.isdir(music_folder)

winter_folder_exists = os.path.isdir(f'{music_folder}/winter')
if winter_folder_exists and datetime.date.today().month == 12:
  music_folder = f'{music_folder}/winter'
  print(f'Loaded winter music from {music_folder}/winter')
  logging.info(f'Loaded winter music from {music_folder}/winter')

max_volume = confighelper.get_max_volume()

sound_files = \
  [mp3 for mp3 in os.listdir(music_folder) \
  if mp3.endswith('.mp3') or mp3.endswith('.ogg')]

start_delay = 0
volume_fade_speed = confighelper.get_volume_fade_speed()
restart = True

last_song_index = -1
current_song_index = -1

mixer.init()
random.seed()
current_volume = max_volume

while not processhelper.is_emulationstation_running():
  time.sleep(1)

time.sleep(start_delay)

processhelper.wait_for_omx()

def stop_music():
  if mixer.music.get_busy():
    mixer.music.stop();

def get_random_song():
  song = random.randint(0, len(sound_files) - 1)
  while song == last_song_index and len(sound_files) > 1:
    song = random.randint(0, len(sound_files) - 1)
  return song

while True:
  while not processhelper.is_emulationstation_running():
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
    logging.info(f'Now playing: {song}')

  emulator_process = processhelper.is_emulator_running()
  if emulator_process['id'] != -1:
    emulator_process_id = emulator_process['id']
    emulator_process_name = emulator_process['name']
    print(f'Emulator process called {str(emulator_process_name)} found. Start fading out the music...')

    while current_volume > 0:
      current_volume = current_volume - volume_fade_speed
      if current_volume < 0:
        current_volume = 0
      mixer.music.set_volume(current_volume);
      time.sleep(0.05)
    
    if restart:
      mixer.music.stop()
    else:
      mixer.music.pause()
    print('Background music muted. Waiting for emulator to stop...')
    logging.info('Background music muted. Waiting for emulator to stop...')
    
    while os.path.exists('/proc/' + emulator_process_id):
      time.sleep(1);
    print('Emulator stopped, start back music')
    logging.info('Emulator stopped, start back music')
    
    if not restart:
      mixer.music.unpause()
      while current_volume < max_volume: 
        current_volume = current_volume + volume_fade_speed;
        if current_volume > max_volume:
          current_volume = max_volume
        mixer.music.set_volume(current_volume);
        time.sleep(0.05)
    print('Restored.')
    
    current_volume = max_volume

  time.sleep(1);

print('An error has occurred that has stopped music.py from executing.')
logging.error('An error has occurred that has stopped music.py from executing.')
