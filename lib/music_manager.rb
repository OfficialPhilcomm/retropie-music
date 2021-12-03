SDL2::init(SDL2::INIT_AUDIO)

SDL2::Mixer.init(SDL2::Mixer::INIT_FLAC|SDL2::Mixer::INIT_MP3|SDL2::Mixer::INIT_OGG)
SDL2::Mixer.open(44100, SDL2::Mixer::DEFAULT_FORMAT, 2, 1024)

class MusicManager
  def initialize
    @music_folder = Config.instance.music_folder
    @current = nil

    @mp3_files = if Dir.exists?("#{@music_folder}/winter") && Time.now.month == 12
      Dir["#{@music_folder}/winter/*.mp3"]
    else
      Dir["#{@music_folder}/**/*.mp3"].select do |file|
        !file.start_with? "#{@music_folder}/winter/"
      end
    end

    SDL2::Mixer::MusicChannel.volume = Config.instance.max_volume
  end

  def start_playing(fade_in = false)
    file = @mp3_files.sample
    while file == @current
      file = @mp3_files.sample
    end
    @current = file

    @song = SDL2::Mixer::Music.load(file)
    if fade_in
      SDL2::Mixer::MusicChannel.fade_in(@song, 1, Config.instance.fade_speed)
    else
      SDL2::Mixer::MusicChannel.play(@song, 1)
    end

    puts "Now playing: #{file.sub "#{@music_folder}/", ""}"
  end

  def fade_out
    SDL2::Mixer::MusicChannel.fade_out(Config.instance.fade_speed)
  end

  def fade_in
    start_playing(fade_in: true)
  end

  def playing?
    SDL2::Mixer::MusicChannel.play?
  end

  def stop
    SDL2::Mixer::MusicChannel.halt
  end
end
