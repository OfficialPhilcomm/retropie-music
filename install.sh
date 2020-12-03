sudo pip3 install pygame==2.0.0

sudo mkdir "/opt/dev_philcomm"
sudo chmod 777 "/opt/dev_philcomm"
mv music.py /opt/dev_philcomm/music.py
mv confighelper.py /opt/dev_philcomm/confighelper.py
mv processhelper.py /opt/dev_philcomm/processhelper.py

sudo mv retropie_music.service /etc/systemd/system/retropie_music.service
sudo systemctl enable retropie_music
sudo systemctl start retropie_music
