%define base_dir /usr/local/angel.com
Name: angel_ps_php_base
Version: 2
Release: 12
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

%define psrunner_uid    1006
%define psrunner_user   psuser
%define psrunner_gid    1006
%define psrunner_group  psunixusers
%define psrunner_home /home/psuser


%description
Base of php


%files
%defattr(644,%{psrunner_user},%{psrunner_group},755)
%dir  /usr/local/angel.com/psphp
%dir  /usr/local/angel.com/psphpconfig
%dir /var/log/angel
/etc/httpd/conf.d/ps.conf
/etc/php.ini
%pre
if [ "$1" = "1" ] ; then  # If it's the very first version of this package being installed then setup the users, otherwise don't try
	grep -q ^%{psrunner_group}: /etc/group || /usr/sbin/groupadd -g %{psrunner_gid} -r %{psrunner_group} 2>/dev/null
	grep -q ^%{psrunner_user}: /etc/passwd || /usr/sbin/useradd -d %{psrunner_home} -s /bin/bash -g %{psrunner_group} -u %{psrunner_uid} %{psrunner_user} 2>/dev/null
fi


%postun
if [ "$1" = "0" ] ; then  # no versions of this rpm should exist any more, normally this is called also when doing an upgrade
     echo "I'd delete the psuser and group, but it's just too complex to get right.  Sorry"
#     We really should cleanup the
#      	grep -q ^%{psrunner_group}: /etc/group && /usr/sbin/groupdel %{psrunner_group}
#	grep -q ^%{psrunner_user}: /etc/passwd && /usr/sbin/userdel %{psrunner_user}
fi
