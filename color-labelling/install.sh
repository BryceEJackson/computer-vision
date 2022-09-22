#!/bin/bash
export LANG=C
set -e

(
cd
## install dependences
sudo apt update && sudo apt upgrade -y
sudo apt install -y unzip build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev   libgtk-3-dev libatlas-base-dev gfortran python2.7-dev python3.5-dev
## set env
sudo apt install -y python-pip && pip install --upgrade pip
pip install virtualenv virtualenvwrapper numpy
rm -rf ~/.cache/pip
echo "# virtualenv and virtualenvwrapper" >> .bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> .bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> .bashrc
export WORKON_HOME=$HOME/.virtualenvs
bash -c ". /usr/local/bin/virtualenvwrapper.sh && . ~/.bashrc && mkvirtualenv cv -p python3"
## start build
echo "start build"
. ~/.bashrc
mkdir -p local/src

cd local/src
sudo rm -fr 3.3.1.zip opencv-3.3.1.zip opencv_contrib-3.3.1.zip opencv-3.3.1 opencv_contrib-3.3.1
wget https://github.com/opencv/opencv/archive/3.3.1.zip
mv 3.3.1.zip opencv-3.3.1.zip
wget https://github.com/opencv/opencv_contrib/archive/3.3.1.zip
mv 3.3.1.zip opencv_contrib-3.3.1.zip
unzip opencv-3.3.1.zip
unzip opencv_contrib-3.3.1.zip

## compile latest
cd opencv-3.3.1
mkdir -p build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_INSTALL_PREFIX=/usr/local \
  -D INSTALL_PYTHON_EXAMPLES=ON \
  -D INSTALL_C_EXAMPLES=OFF \
  -D OPENCV_EXTRA_MODULES_PATH=~/local/src/opencv_contrib-3.3.1/modules \
  -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
  -D BUILD_EXAMPLES=ON ..

make -j6
sudo porg -lp opencv-3.3.1 make install
sudo ldconfig
)