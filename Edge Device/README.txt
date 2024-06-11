python3.8
pytorch 1.12
torchvision 0.13
jetpack 5.1.1

Install all non-jetson deps first then do the following:

Install pytorch and torchvision (only) from the following link:
https://wiki.seeedstudio.com/YOLOv8-DeepStream-TRT-Jetson/

sudo apt-get install -y libopenblas-base libopenmpi-dev
wget https://developer.download.nvidia.com/compute/redist/jp/v50/pytorch/torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl -O torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl
pip3 install torch-1.12.0a0+2c916ef.nv22.3-cp38-cp38-linux_aarch64.whl

sudo apt install -y libjpeg-dev zlib1g-dev
git clone --branch v0.13.0 https://github.com/pytorch/vision torchvision
cd torchvision
python3 setup.py install --user

To start the application run the following command:
./run.sh

