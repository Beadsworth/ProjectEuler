#!/bin/bash
ghc -O2 --make ./soln -prof -auto-all -fforce-recomp && ./soln +RTS -p

