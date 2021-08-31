#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iproute2
Version  : 5.14.0
Release  : 69
URL      : https://mirrors.kernel.org/pub/linux/utils/net/iproute2/iproute2-5.14.0.tar.xz
Source0  : https://mirrors.kernel.org/pub/linux/utils/net/iproute2/iproute2-5.14.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: iproute2-bin = %{version}-%{release}
Requires: iproute2-data = %{version}-%{release}
Requires: iproute2-lib = %{version}-%{release}
Requires: iproute2-license = %{version}-%{release}
Requires: iproute2-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : libmnl-dev
BuildRequires : pkgconfig(xtables)
Patch1: 0001-Only-use-system-wide-defaults-directory-as-config-is.patch
Patch2: 0002-Permit-unhandled-configure-options.patch

%description
This is a set of utilities for Linux networking.
Information:
https://wiki.linuxfoundation.org/networking/iproute2

%package bin
Summary: bin components for the iproute2 package.
Group: Binaries
Requires: iproute2-data = %{version}-%{release}
Requires: iproute2-license = %{version}-%{release}

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
Requires: iproute2-lib = %{version}-%{release}
Requires: iproute2-bin = %{version}-%{release}
Requires: iproute2-data = %{version}-%{release}
Provides: iproute2-devel = %{version}-%{release}
Requires: iproute2 = %{version}-%{release}

%description dev
dev components for the iproute2 package.


%package lib
Summary: lib components for the iproute2 package.
Group: Libraries
Requires: iproute2-data = %{version}-%{release}
Requires: iproute2-license = %{version}-%{release}

%description lib
lib components for the iproute2 package.


%package license
Summary: license components for the iproute2 package.
Group: Default

%description license
license components for the iproute2 package.


%package man
Summary: man components for the iproute2 package.
Group: Default

%description man
man components for the iproute2 package.


%package staticdev
Summary: staticdev components for the iproute2 package.
Group: Default
Requires: iproute2-dev = %{version}-%{release}

%description staticdev
staticdev components for the iproute2 package.


%prep
%setup -q -n iproute2-5.14.0
cd %{_builddir}/iproute2-5.14.0
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1630448225
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1630448225
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iproute2
cp %{_builddir}/iproute2-5.14.0/COPYING %{buildroot}/usr/share/package-licenses/iproute2/b47456e2c1f38c40346ff00db976a2badf36b5e3
%make_install
## install_append content
install -m 0755 -d %{buildroot}%{_includedir}/
install -m 0755 -d %{buildroot}%{_libdir}/

install -m644 include/libnetlink.h %{buildroot}%{_includedir}/
install -m644 lib/libnetlink.a %{buildroot}%{_libdir}/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/tc/experimental.dist
/usr/lib/tc/normal.dist
/usr/lib/tc/pareto.dist
/usr/lib/tc/paretonormal.dist

%files bin
%defattr(-,root,root,-)
/usr/bin/bridge
/usr/bin/ctstat
/usr/bin/dcb
/usr/bin/devlink
/usr/bin/genl
/usr/bin/ifcfg
/usr/bin/ifstat
/usr/bin/ip
/usr/bin/lnstat
/usr/bin/nstat
/usr/bin/rdma
/usr/bin/routef
/usr/bin/routel
/usr/bin/rtacct
/usr/bin/rtmon
/usr/bin/rtpr
/usr/bin/rtstat
/usr/bin/ss
/usr/bin/tc
/usr/bin/tipc
/usr/bin/vdpa

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/devlink
/usr/share/bash-completion/completions/tc
/usr/share/defaults/iproute2/bpf_pinning
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
/usr/include/iproute2/bpf_elf.h
/usr/include/libnetlink.h
/usr/share/man/man3/libnetlink.3

%files lib
%defattr(-,root,root,-)
/usr/lib/tc/m_ipt.so
/usr/lib/tc/m_xt.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iproute2/b47456e2c1f38c40346ff00db976a2badf36b5e3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man7/tc-hfsc.7
/usr/share/man/man8/arpd.8
/usr/share/man/man8/bridge.8
/usr/share/man/man8/ctstat.8
/usr/share/man/man8/dcb-app.8
/usr/share/man/man8/dcb-buffer.8
/usr/share/man/man8/dcb-dcbx.8
/usr/share/man/man8/dcb-ets.8
/usr/share/man/man8/dcb-maxrate.8
/usr/share/man/man8/dcb-pfc.8
/usr/share/man/man8/dcb.8
/usr/share/man/man8/devlink-dev.8
/usr/share/man/man8/devlink-dpipe.8
/usr/share/man/man8/devlink-health.8
/usr/share/man/man8/devlink-monitor.8
/usr/share/man/man8/devlink-port.8
/usr/share/man/man8/devlink-rate.8
/usr/share/man/man8/devlink-region.8
/usr/share/man/man8/devlink-resource.8
/usr/share/man/man8/devlink-sb.8
/usr/share/man/man8/devlink-trap.8
/usr/share/man/man8/devlink.8
/usr/share/man/man8/genl.8
/usr/share/man/man8/ifcfg.8
/usr/share/man/man8/ifstat.8
/usr/share/man/man8/ip-address.8
/usr/share/man/man8/ip-addrlabel.8
/usr/share/man/man8/ip-fou.8
/usr/share/man/man8/ip-gue.8
/usr/share/man/man8/ip-l2tp.8
/usr/share/man/man8/ip-link.8
/usr/share/man/man8/ip-macsec.8
/usr/share/man/man8/ip-maddress.8
/usr/share/man/man8/ip-monitor.8
/usr/share/man/man8/ip-mptcp.8
/usr/share/man/man8/ip-mroute.8
/usr/share/man/man8/ip-neighbour.8
/usr/share/man/man8/ip-netconf.8
/usr/share/man/man8/ip-netns.8
/usr/share/man/man8/ip-nexthop.8
/usr/share/man/man8/ip-ntable.8
/usr/share/man/man8/ip-route.8
/usr/share/man/man8/ip-rule.8
/usr/share/man/man8/ip-sr.8
/usr/share/man/man8/ip-tcp_metrics.8
/usr/share/man/man8/ip-token.8
/usr/share/man/man8/ip-tunnel.8
/usr/share/man/man8/ip-vrf.8
/usr/share/man/man8/ip-xfrm.8
/usr/share/man/man8/ip.8
/usr/share/man/man8/lnstat.8
/usr/share/man/man8/nstat.8
/usr/share/man/man8/rdma-dev.8
/usr/share/man/man8/rdma-link.8
/usr/share/man/man8/rdma-resource.8
/usr/share/man/man8/rdma-statistic.8
/usr/share/man/man8/rdma-system.8
/usr/share/man/man8/rdma.8
/usr/share/man/man8/routef.8
/usr/share/man/man8/routel.8
/usr/share/man/man8/rtacct.8
/usr/share/man/man8/rtmon.8
/usr/share/man/man8/rtpr.8
/usr/share/man/man8/rtstat.8
/usr/share/man/man8/ss.8
/usr/share/man/man8/tc-actions.8
/usr/share/man/man8/tc-basic.8
/usr/share/man/man8/tc-bfifo.8
/usr/share/man/man8/tc-bpf.8
/usr/share/man/man8/tc-cake.8
/usr/share/man/man8/tc-cbq-details.8
/usr/share/man/man8/tc-cbq.8
/usr/share/man/man8/tc-cbs.8
/usr/share/man/man8/tc-cgroup.8
/usr/share/man/man8/tc-choke.8
/usr/share/man/man8/tc-codel.8
/usr/share/man/man8/tc-connmark.8
/usr/share/man/man8/tc-csum.8
/usr/share/man/man8/tc-ct.8
/usr/share/man/man8/tc-ctinfo.8
/usr/share/man/man8/tc-drr.8
/usr/share/man/man8/tc-ematch.8
/usr/share/man/man8/tc-etf.8
/usr/share/man/man8/tc-ets.8
/usr/share/man/man8/tc-flow.8
/usr/share/man/man8/tc-flower.8
/usr/share/man/man8/tc-fq.8
/usr/share/man/man8/tc-fq_codel.8
/usr/share/man/man8/tc-fq_pie.8
/usr/share/man/man8/tc-fw.8
/usr/share/man/man8/tc-gate.8
/usr/share/man/man8/tc-hfsc.8
/usr/share/man/man8/tc-htb.8
/usr/share/man/man8/tc-ife.8
/usr/share/man/man8/tc-matchall.8
/usr/share/man/man8/tc-mirred.8
/usr/share/man/man8/tc-mpls.8
/usr/share/man/man8/tc-mqprio.8
/usr/share/man/man8/tc-nat.8
/usr/share/man/man8/tc-netem.8
/usr/share/man/man8/tc-pedit.8
/usr/share/man/man8/tc-pfifo.8
/usr/share/man/man8/tc-pfifo_fast.8
/usr/share/man/man8/tc-pie.8
/usr/share/man/man8/tc-police.8
/usr/share/man/man8/tc-prio.8
/usr/share/man/man8/tc-red.8
/usr/share/man/man8/tc-route.8
/usr/share/man/man8/tc-sample.8
/usr/share/man/man8/tc-sfb.8
/usr/share/man/man8/tc-sfq.8
/usr/share/man/man8/tc-simple.8
/usr/share/man/man8/tc-skbedit.8
/usr/share/man/man8/tc-skbmod.8
/usr/share/man/man8/tc-skbprio.8
/usr/share/man/man8/tc-stab.8
/usr/share/man/man8/tc-taprio.8
/usr/share/man/man8/tc-tbf.8
/usr/share/man/man8/tc-tcindex.8
/usr/share/man/man8/tc-tunnel_key.8
/usr/share/man/man8/tc-u32.8
/usr/share/man/man8/tc-vlan.8
/usr/share/man/man8/tc-xt.8
/usr/share/man/man8/tc.8
/usr/share/man/man8/tipc-bearer.8
/usr/share/man/man8/tipc-link.8
/usr/share/man/man8/tipc-media.8
/usr/share/man/man8/tipc-nametable.8
/usr/share/man/man8/tipc-node.8
/usr/share/man/man8/tipc-peer.8
/usr/share/man/man8/tipc-socket.8
/usr/share/man/man8/tipc.8
/usr/share/man/man8/vdpa-dev.8
/usr/share/man/man8/vdpa-mgmtdev.8
/usr/share/man/man8/vdpa.8

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libnetlink.a
