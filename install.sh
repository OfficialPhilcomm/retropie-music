SourcePath=https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master

# Make sure script is executed as sudo
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi

# Download python3 script
sudo apt-get install -y python3-pip libsdl-mixer1.2
sudo pip3 install pygame
sudo mkdir "/opt/dev_philcomm"
sudo chmod 777 "/opt/dev_philcomm"
script=/opt/dev_philcomm/music.py
wget -O $script "$SourcePath/music.py"

# Download service script
service=/etc/systemd/system/retropie_background_music.service
wget -O $service "$SourcePath/retropie_background_music.service"
sudo systemctl enable retropie_background_music
sudo systemctl start retropie_background_music
