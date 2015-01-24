#!/bin/bash

set -e

pwd=$(pwd)
date=$(date +%Y%m%d)
package=gmameui.github
branch=master
name=gmameui

pushd ${package}
git checkout ${branch}
git pull
tag=$(git rev-list HEAD -n 1 | cut -c 1-7)
version=0.2.13
git archive --prefix="${name}-${version}/" --format=tar ${branch} > "$pwd"/${name}-${version}-${date}-${tag}.tar
popd
bzip2 -f ${name}-${version}-${date}-${tag}.tar
echo \#globals for ${name}-${version}-${date}-${tag}
echo %global gitdate ${date}
echo %global gitversion ${tag}
