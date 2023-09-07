FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

ENV ROS_PYTHON_VERSION=3
ENV PYTHONPATH=/opt/ros/$ROS_DISTRO/lib/python3.10/site-packages/
ENV TZ="Asia/Seoul"

RUN apt-get update \
    && apt-get install -y \
      cmake \
      curl \
      git \
      wget \
      python3-pip \
      clang lldb lld \
      sudo \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100 \
    && rm -rf /var/lib/apt/lists/*


RUN sudo apt update && sudo apt install locales
RUN sudo locale-gen en_US en_US.UTF-8
RUN sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
RUN export LANG=en_US.UTF-8

RUN apt-get update && \
    apt-get install -yq tzdata



RUN sudo apt install -y software-properties-common
RUN sudo add-apt-repository universe

RUN sudo apt update && sudo apt install curl -y
RUN sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN sudo apt update && sudo apt upgrade
RUN sudo apt install -y ros-humble-desktop
RUN sudo apt install -y ros-dev-tools
RUN sudo apt install -y python3-colcon-common-extensions python3-vcstool


RUN mkdir $HOME/ksoe_ws
WORKDIR $HOME/ksoe_ws
RUN mkdir src
RUN sudo rosdep init && rosdep update

RUN git clone https://github.com/KSOE-DPR/devops_study.git src/devops_study
RUN cd src/devops_study \
    && git pull \
    && git checkout develop

#RUN apt-get update \
#    && apt-get upgrade -y \
#    && rosdep update \
#    && rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO -yr \
#    && rm -rf /var/lib/apt/lists/*

#RUN . /opt/ros/$ROS_DISTRO/setup.sh \
#    && colcon build

#RUN echo ". /ros_entrypoint.sh" >> ~/.bashrc

#RUN sed -i '$isource "/ksoe_ws/install/setup.bash"' /ros_entrypoint.sh

#ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]
CMD tail -f /dev/null