FROM base/archlinux
RUN pacman -Sy  --noconfirm archlinux-keyring
RUN pacman -Su  --noconfirm
RUN pacman-db-upgrade
RUN pacman -S   --noconfirm ca-certificates-utils
RUN pacman -S   --noconfirm jupyter
RUN pacman -S   --noconfirm opencv
RUN pacman -S   --noconfirm jupyter-notebook
RUN pacman -S   --noconfirm mathjax
ADD https://github.com/krallin/tini/releases/download/v0.10.0/tini-static /tini
RUN chmod a+x /tini
RUN pacman -S   --noconfirm python-numpy
RUN pacman -S   --noconfirm python-matplotlib
RUN python3 -c 'import matplotlib.pyplot'
RUN pacman -S   --noconfirm qt5-svg
EXPOSE 8888
CMD /tini -- jupyter notebook --debug -y --ip 0.0.0.0 --no-browser
