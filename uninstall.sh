rm /opt/dev_philcomm/music.py
rm /opt/dev_philcomm/confighelper.py
rm /opt/dev_philcomm/processhelper.py

sudo systemctl stop retropie_music
sudo systemctl disable retropie_music
rm /etc/systemd/system/retropie_music.service
