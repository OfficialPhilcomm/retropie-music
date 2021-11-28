import os
import configparser
import logging

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config_file = os.path.join(dirname, 'config.cfg')

logging.basicConfig(
  filename=os.path.join(dirname, 'retropie_music.log'), 
  level=logging.DEBUG,
  format='[%(asctime)s %(levelname)s] %(message)s',
  datefmt='%Y/%m/%d %I:%M:%S'
)

def setup_config():
  if not os.path.isfile(config_file):
    create_config()
  config.read(config_file)

def create_config():
  config['general'] = { 'music_folder': '/home/pi/music',
  'max_volume': '0.6',
  'volume_fade_speed': '0.02' }
  with open(config_file, 'w') as cfg_file:
    config.write(cfg_file)
  print(f'Created config at {config_file}')
  logging.info(f'Created config at {config_file}')

def get_music_folder():
  return config.get('general', 'music_folder') or '/home/pi/music'

def get_max_volume():
  return float(config.get('general', 'max_volume') or '0.6')

def get_volume_fade_speed():
  return float(config.get('general', 'volume_fade_speed') or 0.02)
