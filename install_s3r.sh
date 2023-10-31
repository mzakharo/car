sudo cp s3r.service  /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable s3r.service 
sudo systemctl restart s3r.service 
sudo systemctl status s3r.service 
