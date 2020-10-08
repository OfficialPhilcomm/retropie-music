SourcePath=https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master

# Make sure script is executed as sudo
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi

# Download python3 script
sudo mkdir "/opt/dev_philcomm"
script=/opt/dev_philcomm/music.py
wget -O $script "$SourcePath/music.py"

# Download service script
service=/etc/systemd/system/retropie_background_music.service
wget -O $service "$SourcePath/retropie_background_music.service"