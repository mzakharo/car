sudo cp scratch.service  /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable scratch.service 
sudo systemctl restart scratch.service 
sudo systemctl status scratch.service 
