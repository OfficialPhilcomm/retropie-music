require "singleton"
require "yaml"

class Config
  include Singleton

  CONFIG_FILE = "config.yml"

  def initialize
    create_config if !File.exist? CONFIG_FILE
    @config = YAML.load_file(CONFIG_FILE)
  end

  def music_folder
    @config["music_folder"]
  end

  def max_volume
    [0, 128, @config["max_volume"].to_i].sort[1]
  end

  def fade_speed
    @config["fade_speed"].to_f * 1000
  end

  private

  def create_config
    File.open(CONFIG_FILE, "w") do |file|
      file.write(default_config.to_yaml)
    end
  end

  def default_config
    config = {}
    config["music_folder"] = "/home/pi/RetroPie/roms/music"
    config["max_volume"] = 128
    config["fade_speed"] = 1.5

    config
  end
end
