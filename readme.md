# RetroPie
Make sure that an internet connection is established and that a keyboard is connected!

## Install
Steps:
1. Press F4 on the keyboard
2. On the keyboard, enter `wget -O - "https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master/install.sh" | sudo bash`

## Add music
To add music, add a samba share to access `/home/pi/music`. Then, just drop `.ogg` or `.mp3` files on it.

If you are using the `retropie-manager` package, you can create a symlink by entering `ln -s /home/pi/music /home/pi/RetroPie/roms/music`. You will then see a new folder on `retropie-manager` called `music`.

If you want some christmas specific music (I know I do), you can create a folder called `winter` inside `/home/pi/music`. In December, music will be played from there.

## Uninstall
Steps:
1. Press F4 on the keyboard
2. On the keyboard, enter `wget -O - "https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master/uninstall.sh" | sudo bash`