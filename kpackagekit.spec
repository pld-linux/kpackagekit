
%define		qtver	4.4.3
%define		_snap	928700

Summary:	the KDE interface for PackageKit
Summary(pl.UTF-8):	Interface KDE4 dla PackageKit
Name:		kpackagekit
Version:	0.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/playground/sysadmin/kpackagekit
#Source0:	%{name}-%{version}-%{_snap}.tar.gz
Source0:	http://www.kde-apps.org/CONTENT/content-files/84745-%{name}-%{version}.tar.bz2
# Source0-md5:	e08fc1f795208f474049fa7b7cd32a45
BuildRequires:	PackageKit-qt-devel >= 0.4.3
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver} 
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.2
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	strigi-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	PackageKit
Requires:	PolicyKit-kde
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
the KDE interface for PackageKit.

%description -l pl.UTF-8
Interface KDE4 dla PackageKit

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpackagekit
%attr(755,root,root) %{_bindir}/kpackagekit-smart-icon
## this is not a symlink! vvvvvvvvvvvvv
%attr(755,root,root) %{_libdir}/libkpackagekitlib.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_addrm.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_settings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_update.so
%attr(755,root,root) %{_libdir}/kde4/kded_kpackagekitd.so
%{_desktopdir}/kde4/kpackagekit.desktop
%{_datadir}/apps/kpackagekit
%{_datadir}/apps/kpackagekit-smart-icon
%{_datadir}/kde4/services/kded/kpackagekitd.desktop
%{_datadir}/kde4/services/kpk_addrm.desktop
%{_datadir}/kde4/services/kpk_settings.desktop
%{_datadir}/kde4/services/kpk_update.desktop
%{_datadir}/kde4/services/settings-add-and-remove-software.desktop
