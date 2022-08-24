# /usr/bin/bash
path=$1
source=$2
dest=$3

for f in *$2; do
    mv -- "$f" "${f%$2}$3"
done