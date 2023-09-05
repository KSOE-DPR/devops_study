FROM ros:humble

ENV ROS_PYTHON_VERSION=3
ENV PYTHONPATH=/opt/ros/$ROS_DISTRO/lib/python3.10/site-packages/

RUN apt-get update \
    && apt-get install -y \
      cmake \
      curl \
      git \
      python3-colcon-common-extensions \
      python3-vcstool \
      wget \
      python3-pip \
      clang lldb lld \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++ 100 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir $HOME/ksoe_ws
WORKDIR $HOME/ksoe_ws
RUN mkdir src
RUN rosdep update --rosdistro $ROS_DISTRO

RUN git clone https://github.com/KSOE-DPR/devops_study.git src/devops_study
RUN cd src/devops_study \
    && git pull \
    && git checkout develop
RUN apt-get update \
    && apt-get upgrade -y \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src --rosdistro $ROS_DISTRO -yr \
    && rm -rf /var/lib/apt/lists/*

RUN . /opt/ros/$ROS_DISTRO/setup.sh \
    && colcon build

RUN sed -i '$isource "/ksoe_ws/install/setup.bash"' /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]
CMD tail -f /dev/null
