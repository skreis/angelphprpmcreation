#!/bin/bash
#We don't want to keep the old rpms around in case someone forgot to change the release version
rm -rf RPMS/x86_64/*
mkdir -p RPMS/x86_64
mkdir -p buildroot/usr/local/angel.com/psphp
mkdir -p buildroot/usr/local/angel.com/psphpconfig
mkdir -p buildroot/var/log/angel
rpmbuild --bb SPECS/angel_php_base.spec --buildroot `pwd`/buildroot --define="_topdir `pwd`"
cp RPMS/x86_64/* /usr/local/yum/html/idr-qe/angel/x86_64/
createrepo --update /usr/local/yum/html/idr-qe/angel/x86_64/
