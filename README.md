# uboone-hackdays
uBooNE Hackdays scripts and notebooks



## Before the HackDay

Assuming a lack of cancelled work tomorrow, we’ll be having a interactive session to work with the MicroBooNE deep learning infrastructure.

Since the data files and software are rather large, I thought I would get a jumpstart on instructions for pulling the data and software down.
There’s a few options for deploying the software. If you’d like to build from source, I left some sparse instructions in the slides from the last meeting. 

If you’d like a simpler option, we can go with the Docker build. This requires [setting up Docker](https://docs.docker.com/engine/installation/). Also, you should be warned that this will utilize quite a bit of space (~30GB).

We now have an image of the software up on Docker Hub here: https://hub.docker.com/r/kwierman/hep-dl/ . This includes the pull command to pull down the image.

Once that is done installing, we’re setting up a workspace here: https://github.com/HEP-DL/uboone-hackdays. This can be cloned out now, but since I’m filling in the notebooks as we speak, this will need to be cloned again before the meeting tomorrow.

Finally, the data and training sets are up on constance01.pnl.gov:/scratch/hep_dl . Assuming you have an account on constance, everything here should be readable by everyone.

Let me know if you have any problems pulling the software or the data, and I’ll help you out in advance of the meeting tomorrow. I hope to see everyone there!


## Starting up the Docker container:

The goal of the instructions below is to start the container and issue some additional commands to make it ready for the 

You can automatically start up the docker container and attach to it using the following command. For the sake of this hackday, I'm going to assume that this command is being run from `uboone-hackdays`.

~~~ bash
  docker run -ti -v$(pwd):/workspace -p8888:8888 --name uboone  kwierman/hep-dl
~~~

On first startup, this should put the user in the home directory. The environment variables specific to the software are left initially unset for testing purposes. The command to setup the environment and thus the first command to run is:

~~~ bash
  source setup.sh
~~~

Since the initial `docker run` command attaches the `uboone-hackdays` directory to the container filesystem, this directory can be accessed via:

~~~ bash
  cd /workspace
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