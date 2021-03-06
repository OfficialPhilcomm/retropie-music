# Make sure script is executed as sudo
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi

# Stop and remove service
service=/etc/systemd/system/retropie_music.service
sudo systemctl disable retropie_music
sudo systemctl stop retropie_music
rm $service

# Delete python3 script
rm /opt/dev_philcomm/music.py
rm /opt/dev_philcomm/confighelper.py
rm /opt/dev_philcomm/processhelper.py
rm /opt/dev_philcomm/config.cfg
rmdir /opt/dev_philcomm
