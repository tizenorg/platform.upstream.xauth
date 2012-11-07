#
# spec file for package xauth
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           xauth
Version:        1.0.7
Release:        1
License:        MIT
Summary:        Utility to edit and display the X authorization information
Url:            http://xorg.freedesktop.org/
Group:          System/X11/Utilities
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM xauth-1.0.2.diff fdo#48642 -- Fix crash on removing non-existant entry
Patch0:         xauth-1.0.2.diff
Patch1:         xauth-tolerant-hostname-changes.diff
Patch2:         u_xauth_Look-for-FamilyLocal-if-inet-or-inet6-addr.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# Name of subpackage when this was part of the xorg-x11 package up to version 7.6
Provides:       xorg-x11-xauth = 7.6
Obsoletes:      xorg-x11-xauth <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xauth program is used to edit and display the authorization
information used in connecting to the X server.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p0

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xauth
%{_mandir}/man1/xauth.1%{?ext_man}

%changelog
