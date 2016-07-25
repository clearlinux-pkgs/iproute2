#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iproute2
Version  : 4.3.0
Release  : 25
URL      : https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-4.3.0.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-4.3.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: iproute2-bin
Requires: iproute2-data
Requires: iproute2-doc
Requires: iproute2-lib
BuildRequires : bison
BuildRequires : db-dev
BuildRequires : flex
BuildRequires : pkgconfig(xtables)
Patch1: stateless.patch

%description
This is a set of utilities for Linux networking.
Information:
http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2

%package bin
Summary: bin components for the iproute2 package.
Group: Binaries
Requires: iproute2-data

%description bin
bin components for the iproute2 package.


%package data
Summary: data components for the iproute2 package.
Group: Data

%description data
data components for the iproute2 package.


%package dev
Summary: dev components for the iproute2 package.
Group: Development
Requires: iproute2-lib
Requires: iproute2-bin
Requires: iproute2-data
Provides: iproute2-devel

%description dev
dev components for the iproute2 package.


%package doc
Summary: doc components for the iproute2 package.
Group: Documentation

%description doc
doc components for the iproute2 package.


%package lib
Summary: lib components for the iproute2 package.
Group: Libraries
Requires: iproute2-data

%description lib
lib components for the iproute2 package.


%prep
%setup -q -n iproute2-4.3.0
%patch1 -p1

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
install -m 0755 -d %{buildroot}%{_includedir}/
install -m 0755 -d %{buildroot}%{_libdir}/
install -m644 include/libnetlink.h %{buildroot}%{_includedir}/
install -m644 lib/libnetlink.a %{buildroot}%{_libdir}/
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib/tc/experimental.dist
/usr/lib/tc/normal.dist
/usr/lib/tc/pareto.dist
/usr/lib/tc/paretonormal.dist

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/arpd
/usr/bin/bridge
/usr/bin/ctstat
/usr/bin/genl
/usr/bin/ifcfg
/usr/bin/ifstat
/usr/bin/ip
/usr/bin/lnstat
/usr/bin/nstat
/usr/bin/routef
/usr/bin/routel
/usr/bin/rtacct
/usr/bin/rtmon
/usr/bin/rtpr
/usr/bin/rtstat
/usr/bin/ss
/usr/bin/tc

%files data
%defattr(-,root,root,-)
/usr/share/defaults/iproute2/ematch_map
/usr/share/defaults/iproute2/group
/usr/share/defaults/iproute2/nl_protos
/usr/share/defaults/iproute2/rt_dsfield
/usr/share/defaults/iproute2/rt_protos
/usr/share/defaults/iproute2/rt_realms
/usr/share/defaults/iproute2/rt_scopes
/usr/share/defaults/iproute2/rt_tables

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.a

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/iproute2/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib/tc/m_ipt.so
/usr/lib/tc/m_xt.so
