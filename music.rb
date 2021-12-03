require "sdl2"
require "require_all"
require_rel "lib"

music_manager = MusicManager.new()

while true
  music_manager.stop if !ProcessHelper.is_emulation_station_running?
  while !ProcessHelper.is_emulation_station_running?
    sleep 1
  end

  if !music_manager.playing?
    music_manager.start_playing
  end

  running_emulator = ProcessHelper.is_emulator_running

  if running_emulator
    emulator_process_id, emulator_process_name = running_emulator
    puts "Emulator process called #{emulator_process_name} found. Start fading out the music..."
    music_manager.fade_out
    puts "Background music muted. Waiting for emulator to stop..."
    
    while File.exist?("/proc/#{emulator_process_id}")
      sleep 1
    end
    puts "Emulator stopped, starting music"
    music_manager.fade_in
  end
end
