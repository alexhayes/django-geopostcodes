#!/bin/bash

# Assume that this script has been imported as a submodule, get top level of parent git repo.
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )/../" && git rev-parse --show-toplevel )"

cd "$DIR" \
  && git pull \
  && git submodule sync && git submodule update --init --recursive \
  && git submodule foreach "git submodule sync && git submodule update --init --recursive" \
