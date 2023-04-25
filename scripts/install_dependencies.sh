#!/bin/bash

DIR="/home/ubuntu/StudentRegistration_on_Aws"
if [-d "$DIR" ]; then
	echo "${DIR} exists"
else
   echo "Creating ${DIR} directory"
   mkdir ${DIR}
fi