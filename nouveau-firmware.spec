#
%define		nameprog nouveau

Summary:	Firmware for the Nouveau driver
Name:		%{nameprog}-firmware
Version:	20091212
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://people.freedesktop.org/~pq/nouveau-drm/nouveau-firmware-%{version}.tar.gz
# Source0-md5:	518ce9f432498969c88f63579032da74
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the nouveau driver.

%prep
%setup -q -n %{nameprog}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware/nouveau

cp -a *.* $RPM_BUILD_ROOT/lib/firmware/nouveau

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/nouveau
