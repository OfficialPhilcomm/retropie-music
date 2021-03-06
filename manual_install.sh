SourcePath=https://raw.githubusercontent.com/OfficialPhilcomm/retropie-music/master

# Make sure script is executed as sudo
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi

# Download python3 script
sudo apt-get install -y python3-pip libsdl2-mixer-2.0-0
sudo pip3 install pygame==2.0.0
sudo mkdir "/opt/dev_philcomm"
sudo chmod 777 "/opt/dev_philcomm"
wget -O /opt/dev_philcomm/music.py "$SourcePath/music.py"
wget -O /opt/dev_philcomm/confighelper.py "$SourcePath/confighelper.py"
wget -O /opt/dev_philcomm/processhelper.py "$SourcePath/processhelper.py"

# Download service script
service=/etc/systemd/system/retropie_music.service
wget -O $service "$SourcePath/retropie_music.service"
sudo systemctl enable retropie_music
sudo systemctl start retropie_music
