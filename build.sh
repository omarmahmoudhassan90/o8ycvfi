#!/usr/bin/env bash
# Helper script: build using Docker (kivy/buildozer)
docker pull kivy/buildozer
docker run --rm -v "$(pwd)":/home/user/hostcwd -w /home/user/hostcwd kivy/buildozer buildozer -v android debug