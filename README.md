# gr-flaress
gr-flaress module for GnuRadio

### HOW TO INSTALL GNURADIO
rember to change MYUSER

    sudo pip install PyBOMBS
    pybombs auto-config
    pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git
    pybombs recipes add gr-etcetera git+https://github.com/gnuradio/gr-etcetera.git
    mkdir /home/MYUSER/gnuradio
    pybombs config --package gnuradio gitrev v3.7.13.5
    pybombs prefix init /home/MYUSER/gnuradio/prefix -a myprefix -R gnuradio-default


## HOW TO INSTALL NEW GROUP OF OOT BLOCKS
(notice that "prefix" must be the same directory where is GNURADIO. The default PyBOMBS path is "prefix"). Run this commands in the main directory of the OOT group.

### PyBOMBS installation:

    source ~/prefix/setup_env.sh  
    mkdir build  
    cd build  
    cmake -DCMAKE_INSTALL_PREFIX=~/prefix ../  
    make  
    make test  
    sudo make install  
    sudo ldconfig  

### apt-get installation:

    mkdir build   
    cd build  
    cmake ../
    make
    make test  
    sudo make install  
    sudo ldconfig  

### MAC OS X installation (from MacPort):

    mkdir build  
    cd build  
    cmake -DCMAKE_INSTALL_PREFIX=/opt/local/ ../  
    make  
    make test  
    sudo make install  

## HOW TO TEST NEW GROUP OF OOT BLOCKS
create a new folder/directory in the main directory of the OOT group (ex gr_flaress) named: "test log" (in that folder will be put the log files)

the command to run the tests is (in the build dir):

    make test   
    
the command to run one specific test with more info is (in the build dir):

    ctest -R qa_AGC -VV

if you want to install the OOT Module in an older version of GnuRadio Companion, for example 3.7.9, it is important to update the cmake file and make sure you have correctly installed the volk library: Build and install Volk

    cd ~
    wget http://libvolk.org/releases/volk-1.3.tar.gz
    tar -xzvf volk-1.3.tar.gz
    cd volk-1.3
    mkdir build && cd build
    cmake ..
    make
    sudo make install
    
    
## DEPENDENCIES

#### wkhtmltopdf 0.12.1:

    sudo wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb
    sudo dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb
#### PDFKit:

    pip install pdfkit
    
## DOXYGEN PDF GENERATION

to generate the PDF version of the doxygen files, from the build folder inside the gr-ecss folder:

    cd /docs/doxygen/
    doxygen
    cd latex
    make
the file containing all the documentation will be named ¨refman.pdf¨.

a recent version of doxygen is needed:

    git clone https://github.com/doxygen/doxygen.git
    cd doxygen
    mkdir build
    cd build
    cmake -G "Unix Makefiles" ..
    make
    sudo make install
    sudo ldconfig

additional packets for latex generation:

    sudo apt-get install texlive-font-utils
    sudo apt install texlive-latex-extra
