class ProcessHelper
  EMULATOR_NAMES = [
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
    'zdoom'
  ]

  def self.is_emulation_station_running?
    process_map.map { |_process_id, process_name| process_name }.include? "emulationstatio"
  end

  def self.is_emulator_running
    process_map.select do |_process_id, process_name|
      EMULATOR_NAMES.include? process_name
    end
    .first
  end

  def self.process_map
    Dir.entries("/proc")
      .select do |entry|
        entry.to_i.to_s == entry
      end
      .map do |entry|
        entry.to_i
      end
      .map do |process_id|
        [
          process_id,
          File.exist?("/proc/#{process_id}/comm") ? `cat /proc/#{process_id}/comm`.tr("\n", "") : nil
        ]
      end
  end
end
