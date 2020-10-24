import os

emulator_process_names = [
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
