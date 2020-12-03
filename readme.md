# RetroPie
Make sure that an internet connection is established and that a keyboard is connected!

## Install
### With RetroPie Setup
You can find this package under the experimental section in the RetroPie Setup Package section
### Manual
Steps:
1. Press F4 on the keyboard
2. On the keyboard, enter `wget -O - "https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master/manual_install.sh" | sudo bash`

## Add music
To add music, just drop `.ogg` or `.mp3` files in the music folder. The music folder is defined in the config (see config section), by default it is located at `/home/pi/music`.

If you are using the `retropie-manager` package, you can create a symlink by entering `ln -s /home/pi/music /home/pi/RetroPie/roms/music`. You will then see a new folder on `retropie-manager` called `music`. If you changed the music folder manually in the config, replace the `/home/pi/music` in the command with your custom folder location.

If you want some christmas specific music (I know I do), you can create a folder called `winter` inside the music folder. In December, music will be played from there.

You might experience slowdowns with mp3 files downloaded from YouTube. This is because the sample rate is not correct. You can convert the sample rate to `44100` with a package called `sox`.  
Use the command `sox file.mp3 -r 44100 out.mp3`. Make sure the output file is not the input file.

## Config
The config for the script is located at `/opt/dev_philcomm/config.cfg`. It is created after the first script startup.

Config changes need the script to be restarted. This can be achieved by restarting the console or entering `sudo systemctl restart retropie_background_music`.

## Logs
The script generates a log file at `/opt/dev_philcomm/retropie_background_music.log`.
Logs include:
- Creation of files and folders that are needed but don't exist
- Songs that are played
- Errors that occur that prevent the script from running

## Uninstall
### With RetroPie Setup
You can use the RetroPie Setup package section to uninstall the script. It is in the experimental section.
### Manual
Steps:
1. Press F4 on the keyboard
2. On the keyboard, enter `wget -O - "https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master/manual_uninstall.sh" | sudo bash`

## Credits
This script is a modified version of the script posted in `https://retropie.org.uk/forum/topic/347/background-music-continued-from-help-support`. I took the freedom of rewriting big parts of it since it wasn't working on newer machines for me.
