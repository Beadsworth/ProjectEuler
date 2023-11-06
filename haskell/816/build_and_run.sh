#!/bin/bash

problem_number=816
image_name="project_euler_p$problem_number"
container_name="$image_name-local"


docker build -t $image_name .

docker run \
    --rm \
    -it \
    --name "$container_name" \
    -v $(pwd):/opt/project_euler \
    $image_name

