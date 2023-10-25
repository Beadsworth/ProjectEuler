FROM haskell:slim-buster

WORKDIR /opt/project_euler

RUN apt-get update
RUN apt-get install nano -y

RUN cabal update

# Add just the .cabal file to capture dependencies
COPY ./req.cabal /opt/project_euler/req.cabal

# Docker will cache this command as a layer, freeing us up to
# modify source code without re-installing dependencies
# (unless the .cabal file changes!)
#RUN cabal build --only-dependencies -j4

# Add and Install Application Code
COPY . /opt/project_euler
#RUN cabal install

CMD ["/bin/bash"]
#CMD ["ghci"]
