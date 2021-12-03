# RetroPie

Make sure that an internet connection is established and that a keyboard is connected!

## Install

To install the package, simply run this command from the console. This will make the package appear in RetroPie Setup under optional packages. From there, you can install, uninstall and update the package.

```
wget -P /home/pi/RetroPie-Setup/ext/dev_philcomm/scriptmodules/supplementary/ "https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master/retropie-music.sh"
```

## Add music

To add music, just drop `.mp3`, `.ogg` or `.flac` files in the music folder. The music folder is defined in the config (see config section), by default it is located at `/home/pi/RetroPie/roms/music`.

If you want some christmas specific music (I know I do), you can create a folder called `winter` inside the music folder. In December, music will be played exclusively from there.

You might experience slowdowns with mp3 files downloaded from YouTube. This is because the sample rate is not correct. This is something that is being looked into, but there is no straight forward solution to this.

You can convert the sample rate to `44100` with a package called `sox`. Use the command `sox file.mp3 -r 44100 out.mp3`. Make sure the output file is not the input file.

## Config

The config for the script is located at `/opt/retropie/config.yml`. It is created after the first script startup.

Config changes need the script to be restarted. This can be achieved by restarting the console or entering `sudo systemctl restart retropie_music`.

### `music_folder`
This is the location of the music folder. By default, it's set to `/home/pi/RetroPie/roms/music` to be accessible via the roms samba share.

### `max_volume`
This sets the maximum volume for the music script. Allowed are values between `0` and `128`.  
Note: This is a non linear value, 64 is nearly the same as 128. I don't have much influence on this.

### `fade_speed`
This value is used for music fading, for example when an emulator is started. It is set in seconds (`1.5` = 1.5 seconds)

## Credits
This project originated as a python rewrite of https://retropie.org.uk/forum/topic/347/background-music-continued-from-help-support, as the old script wasn't working on newer versions of RetroPie.

I chose to rewrite and restructure the full script in ruby, as here I can directly work with the `sdl2` layer instead of using a game engine (`pygame`). This has some performance benefits, especially when using a Pi Zero.
