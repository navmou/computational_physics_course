#!/usr/bin/env sh
wget ftp://ftp.gnu.org/gnu/gsl/gsl-2.6.tar.gz
tar -xvf gsl-2.6.tar.gz
cd gsl-2.6/
./configure --prefix=$HOME/.local
make
make install
echo "export C_INCLUDE_PATH=$HOME/.local/include" >> ~/.bashrc
echo "export LIBRARY_PATH=$HOME/.local/lib" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=$HOME/.local/lib" >> ~/.bashrc
export C_INCLUDE_PATH="$HOME/.local/include"
export LIBRARY_PATH="$HOME/.local/lib"
export LD_LIBRARY_PATH="$HOME/.local/lib"
cd ..
rm -rf gsl-2.6.tar.gz
rm -rf gsl-2.6
