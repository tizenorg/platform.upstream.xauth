Name:           xauth
Version:        1.0.7
Release:        1
License:        MIT
Summary:        Utility to edit and display the X authorization information
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/xauth
%{_mandir}/man1/xauth.1%{?ext_man}

%changelog
