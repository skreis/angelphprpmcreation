%define base_dir /usr/local/angel.com
%define config_dest_dir /usr/local/angel.com/builds/call-server/1
Name: angel_ps_php_base
Version: 105
Release: 105
Summary: Angel Pro Service PHP Base
License: 2010, Angel.com
Distribution: Angel System Config
Group: Angel.Com Engineering
Requires: php
Requires: httpd-devel 
Requires: php-mysql
Requires: php-xml
Requires: libframework1-zend-server
autoprov: yes
autoreq: yes
Prefix: /usr/local
BuildRoot: buildroot
%description
Base of php


%files
%defattr(644,apache,apache,755)
%dir  /usr/local/angel.com/psphp
%dir  /usr/local/angel.com/psphpconfig
%dir /var/log/angel
/etc/httpd/conf.d/ps.conf

