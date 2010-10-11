#!/bin/bash
mkdir -p RPMS/x86_64
mkdir -p buildroot/usr/local/angel.com/psphp
mkdir -p buildroot/usr/local/angel.com/psphpconfig
mkdir -p buildroot/var/log/angel
rpmbuild --bb SPECS/angel_php_base.spec --buildroot `pwd`/buildroot --define="_topdir `pwd`"
