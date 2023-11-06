#!/bin/bash
ghc -O2 --make ./p816.hs -prof -auto-all -fforce-recomp && ./p816 +RTS -p

