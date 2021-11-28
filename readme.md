# RetroPie

Make sure that an internet connection is established and that a keyboard is connected!

## Install

To install the package, simply run `wget -P /home/pi/RetroPie-Setup/ext/dev_philcomm/scriptmodules/supplementary/ "https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master/retropie-music.sh"` from the console. This will make the package appear in RetroPie Setup in optional packages. From there, you can install, uninstall and update the package.

## Add music

To add music, just drop `.ogg` or `.mp3` files in the music folder. The music folder is defined in the config (see config section), by default it is located at `/home/pi/RetroPie/roms/music`.

If you want some christmas specific music (I know I do), you can create a folder called `winter` inside the music folder. In December, music will be played from there.

You might experience slowdowns with mp3 files downloaded from YouTube. This is because the sample rate is not correct. You can convert the sample rate to `44100` with a package called `sox`.  
Use the command `sox file.mp3 -r 44100 out.mp3`. Make sure the output file is not the input file.

## Config

The config for the script is located at `/opt/retropie/config.cfg`. It is created after the first script startup.

Config changes need the script to be restarted. This can be achieved by restarting the console or entering `sudo systemctl restart retropie_music`.

## Logs

The script generates a log file at `/opt/dev_philcomm/retropie_music.log`.
Logs include:

- Creation of files and folders that are needed but don't exist
- Songs that are played
- Errors that occur that prevent the script from running

## Credits

This script is a heavily modified version of the script posted in `https://retropie.org.uk/forum/topic/347/background-music-continued-from-help-support`. I took the freedom of rewriting big parts of it since it wasn't working on newer machines anymore.
