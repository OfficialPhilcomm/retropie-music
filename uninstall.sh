rm /opt/dev_philcomm/music.py
rm /opt/dev_philcomm/confighelper.py
rm /opt/dev_philcomm/processhelper.py

sudo systemctl stop retropie_background_music
sudo systemctl disable retropie_background_music
rm /etc/systemd/system/retropie_background_music.service
