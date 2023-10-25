#!/bin/bash
docker build -t haskell-p63 .

docker run --rm -it --name haskell-p63-local haskell-p63

