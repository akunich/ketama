#!/bin/sh
VERSION=1.0.2
cd ../../
git archive master --format=tar --prefix="php-ketama-${VERSION}/" \
./php_ketama | gzip > /root/rpmbuild/SOURCES/php-ketama-${VERSION}.tar.gz
