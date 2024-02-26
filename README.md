# Docker Girder

I am trying to create a plugin dev Docker image. The goal is to restart the Girder server each time a modification is made to a plugin.

## Motivation

We use Docker a lot for simplified deployment, but also in a dev context to ensure isolation between services.

This extensive use of Docker made us want to dockerize our Girder server. There weren't any problem for the production Docker.

However, things were not as easy for the development Docker. This repo is a simple repro with a simple plugin to figure out what happens.

## Identified problems

- It appears that setting mode to development in the configuration file wasn't enough to start the autoreloader. The workaround was to launch the server with the "--dev" option.
- The server cannot restart after a change is made. It gets stuck at this "ENGINE Re-spawning /usr/bin/python3 /usr/local/bin/girder serve --dev". Workaround not found yet !
