# Make sure script is executed as sudo
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root." 
   exit 1
fi

# Stop and remove service
service=/etc/systemd/system/retropie_background_music.service
sudo systemctl disable retropie_background_music
sudo systemctl stop retropie_background_music
rm $service

# Delete python3 script
script=/opt/dev_philcomm/music.py
config=/opt/dev_philcomm/config.cfg
rm $script
rm $config
rmdir /opt/dev_philcomm
