Summary: authd (RSA authentication daemon)
Name: authd
Version: 0.2.1
Release: 1
Copyright: GPL
Group: System Environment/Daemons
Source: authd-0.2.1.tar.gz

%description
authd (RSA authentication daemon)

%prep
%setup

%build
./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make install
install -D -m 755 config/authd /etc/init.d/authd

%clean

%files
%defattr(-, root, root)
/usr/sbin/authd
/usr/lib/libauth.a
/usr/include/auth.h
/etc/init.d/authd

%pre

%post 
if [ "$1" = 1 ]; then
   /etc/init.d/authd restart
   chkconfig --add authd
fi

%preun
if [ "$1" = 0 ]; then
   /etc/init.d/authd stop
   chkconfig --del authd
fi

%postun
if [ "$1" = 1 ]; then
   /etc/init.d/authd restart
fi
