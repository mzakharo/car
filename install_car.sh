sudo cp car.service  /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable car.service 
sudo systemctl restart car.service 
sudo systemctl status car.service 
