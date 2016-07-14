# git SHA1 of usable master
%global commit 2210f1fd07c01b206d61404faa0abae01457cd58
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global owner bboozzoo

Name:           mconnect
Version:        0.2.1
Release:        2.20160714git%{shortcommit}%{?dist}
Summary:        Implementation of KDE Connect protocol

License:        GPLv2
URL:            http://github.com/bboozzoo/mconnect
Source0:        https://github.com/%{owner}/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  vala
BuildRequires:  vala-tools
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  libgee-devel
BuildRequires:  openssl-devel
BuildRequires:  libnotify-devel
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf automake libtool pkgconfig
BuildRequires:  gtk3-devel
BuildRequires:  at-spi2-core-devel

%description

MConnect is an implementation of host side of KDE Connect protocol,
but without any KDE or Qt dependencies.

%prep
%setup -q -D -n %{name}-%{commit}


%build
autoreconf -if
%configure
make %{?_smp_mflags} V=1


%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/mconnect.desktop

%files
%doc LICENSE
%{_bindir}/mconnect
%dir %{_datadir}/mconnect
%{_datadir}/mconnect/*
%{_datadir}/applications/*.desktop

%changelog
* Thu Jul 14 2016 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.2.1-2.20160714git2210f1f
- Update to v0.2.1, commit 2210f1fd07c01b206d61404faa0abae01457cd58

* Thu Jul 14 2016 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.2.1-1.20160714git23e1acf
- Update to v0.2.1

* Sun Jan 25 2015 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.2-4.20150125gite4d57ef
- Add vala-tools to BuildRequires

* Sun Jan 25 2015 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.2-3.20150125gite4d57ef
- Add missing gobject-introspection-devel to BuildRequires 

* Sun Jan 25 2015 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.2-2.20150125gite4d57ef
- Updated BuildRequires with autotools, libtool, pkg-config

* Sun Jan 25 2015 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.2-1.20150125gite4d57ef
- Bump to version 0.2

* Mon Jan 19 2015 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.1-3.20150119git3437a33
- Bump version to include minor enhancements

* Mon Jan 19 2015 Maciek Borzęcki <maciek.borzecki@gmail.com> - 0.1-2.20150119gitb8ffa0f
- Bump version to include bug fixes

* Sun Jan 18 2015 Maciek Borzecki <maciek.borzecki@gmail.com> - 0.1-1.20150118git55ae51a
- Initial packaging
