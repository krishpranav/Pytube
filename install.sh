#!/bin/bash
clear
echo "PYTUBE"
INSTALL_DIR="/usr/share/doc/PyTube"

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR"];
then
    echo "[◉] A directory PyTube was found! Do you want to replace it? [Y/n]:" ;
    read reaplce
    if [ $replaec == "y" ];
    then
        sudo rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
sudo apt-get install -y python-pip
sudo pip install --upgrade youtube_dl
sudo apt-get install -y libav-tools
git clone https://github.com/krishpranav/Pytube $INSTALL_DIR;
echo "#!/bin/bash
python $INSTALL_DIR/pytube.py" '${1+"$@"}' > pytube;
chmod +x pytube;
sudo cp pytube /usr/bin/;

if [ -d "$INSTALL_DIR/Pytube"];
then 
    echo "";
    echo "[✔]Tool istalled with success![✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔] ✔✔✔  All is done!! You can execute tool by typing pytube   !   ✔✔✔ [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation faid![✘] ";
    echo "Try again later"
    exit
fi