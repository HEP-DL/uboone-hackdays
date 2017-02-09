# uboone-hackdays
uBooNE Hackdays scripts and notebooks



## Before the HackDay

In order to prepare for hackday, the following 3 things need to be accomplished.

1. Clone the workspace onto a large area of your filesystem
2. Pull the data into the workspace
3. Start up a docker container with
  * A workspace bound to the cloned one from step 1.
  * The image containing the full software stack
  * Port 8888 in the container bound to a port on the host machine (Try port 8888).
  * A couple additional steps that we'll go through below.

Step 0 on this list is to have docker engine up and running.  This requires [setting up Docker](https://docs.docker.com/engine/installation/). Also, you should be warned that the software and data will utilize quite a bit of space (~30GB).

We now have an image of the software up on Docker Hub here: https://hub.docker.com/r/kwierman/hep-dl/ . This includes the pull command to pull down the image.

### Cloning the workspace

As per the above statement, you'll want to find a nice LARGE filespace and clone the repo into a working area.

~~~ bash
  git clone https://github.com/HEP-DL/uboone-hackdays
  cd uboone-hackdays
~~~

Before the hack sesh, you'll want to issue `git pull` from here as I'm working on updating the notebooks.

### Pulling the data


The data and training sets are up on `constance01.pnl.gov:/scratch/hep_dl` . Assuming you have an account on constance, everything here should be readable by everyone. I suggest using rsync to pull these into uboone-hackdays.


## Starting up the Docker container:

If you want to pull the image in advance, the following command can be run from anywhere on your computer.

~~~ bash
docker pull kwierman/hep-dl
~~~

The next step is to start up a container with this image. For today, I'm going to assume that the directory `/workspace` in the docker container is bound to `uboone-hackdays` on your local machine.

Running the following command from the `uboone-hackdays` directory accomplishes this task.

~~~ bash
  docker run -ti -v$(pwd):/workspace -p8888:8888 --name uboone  kwierman/hep-dl
~~~

The run-on sentence explanation is that this is telling docker to spool up a new container, `run`, interactively `-ti`, binding the local workspace, `$(pwd)` to `/workspace` in the container, `-v$(pwd):/workspace`, and binding local port 8888 to container port 8888, `-p8888:8888`, with name `uboone`, `--name uboone` and use image `kwierman/hep-dl`. 

If Docker complains about the ports being occupied, change the first `8888` port number to another port and later when attaching to the notebook server, change the port on the URL.


If this is your first time running, it should begin by pulling the image from dockerhub. This can take time.

On first startup, this should put the user in the home directory. The environment variables specific to the software are left initially unset for testing purposes. The command to setup the environment and thus the first command to run is:

~~~ bash
  source setup.sh
~~~

Since the initial `docker run` command attaches the `uboone-hackdays` directory to the container filesystem, this directory can be accessed via:

~~~ bash
  cd /workspace
~~~

This directory should have the contents of your local machine's `uboone-hackdays` directory, such that `ls` should return something like:

~~~ bash
root@5daa1ffbc1f1:/workspace# ls
LICENSE                     notebooks                 test.root
README.md                   plainresnet10b            train.root
docker-compose.yml          plainresnet10b_untrained
jupyter_notebook_config.py  setup_notebook.sh
~~~


There is one final step before we're ready to work in the container. A shell script has been deposited here for working with `jupyter notebook` which will be the method by which we interact with caffe post-training. This script can be run via the following:

~~~ bash
  . setup_notebook.sh
~~~

Once this script completes, the container will be ready to use for the hackdays.

## Running the Notebook Server

For the second half of this exercise, we'll be working with jupyter notebooks. The command to start the notebook can be found here:

~~~ bash
  cd /workspace
  jupyter-notebook
~~~

For the first instance of running the notebook server, the URL output by the console will need to be entered into your local browser.