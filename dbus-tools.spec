# TODO:
# - zsh completion: _dbus

%define		svnrev	8
%define		rel		0.1
Summary:	Set of tools for DBus
Name:		dbus-tools
Version:	1
Release:	0.%{svnrev}.%{rel}
License:	MIT
Group:		Applications/System
# revno=
# svn co http://dbus-tools.googlecode.com/svn/trunk${revno:+@$revno} dbus-tools
# tar -cjf dbus-tools-$(svnversion dbus-tools).tar.bz2 --exclude=.svn dbus-tools
# ../dropin dbus-tools-$(svnversion dbus-tools).tar.bz2
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	7ff7a085e5e352c6d3188acce3661a89
URL:		http://code.google.com/p/dbus-tools/
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Requires:	python-lxml
Requires:	python-dbus
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbus-tools is a set of tools to help developers playing with DBus.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p dbus $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/dbus
