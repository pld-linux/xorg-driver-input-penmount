Summary:	X.org input driver for PenMount devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla urządzeń PenMount
Name:		xorg-driver-input-penmount
Version:	1.4.1
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-penmount-%{version}.tar.bz2
# Source0-md5:	e5984e43ce31d45659eb6ee91c02aba5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for PenMount devices. It supports DMC8910 and
DMC9000.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla urządzeń PenMount. Obsługuje DMC8910 i
DMC9000.

%prep
%setup -q -n xf86-input-penmount-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/penmount_drv.so
%{_mandir}/man4/penmount.4*
