#!/bin/bash

#give permission for everything in the express-app directory
sudo chmod -R 777 /home/ubuntu/StudentRegistration_on_Aws

#navigate into our working directory where we have all our github files
cd /home/ubuntu/StudentRegistration_on_Aws


#start our node app in the background
sudo python3 EmpApp.py > app.out.log 2> app.err.log < /dev/null &
