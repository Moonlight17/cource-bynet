#! /bin/bash
yum -y update
yum -y install httpd
MYIP=`curl http://169.254.169.254/latest/meta-data/local-ipv4`
echo "<h1>It's My working web-service with Private IP $MYIP</h1><br><br><h2>Created by Terraform with using External File</h2>" > /var/www/html/index.html
service httpd start
chkconfig httpd on 
