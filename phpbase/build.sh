#!/bin/bash
rpmbuild --bb SPECS/angel_php_base.spec --buildroot `pwd`/buildroot --define="_topdir `pwd`"
