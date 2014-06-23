#!/bin/sh
VERSION=1.0.2
cd ../../
git archive master --format=tar --prefix="libketama-${VERSION}/" \
./libketama | gzip > /root/rpmbuild/SOURCES/libketama-${VERSION}.tar.gz
