#!/bin/sh

###############
## Variables ##
###############

script=/home/lgutierr/Documents/Notebooks/SciProgWorkshops/JupyterLab/Scripts/

path=/home/lgutierr/Documents/Notebooks/SciProgWorkshops/JupyterLab/Data/

prodID="13100111"

##############
### Script ###
##############

echo "PATH TO SCRIPT: " ${script}
echo ""
echo "PATH TO DATA: " ${data}
echo ""
echo "PRODUCT ID: " ${prodID}
echo ""

cd ${script}

echo "Begin Python Script "
echo " "

python script.py ${path} ${prodID}

echo "End Python Script"