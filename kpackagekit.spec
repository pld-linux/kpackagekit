
%define		qtver	4.6.3
%define		pkver	0.6.8
%define		_snap	 1093726

Summary:	the KDE interface for PackageKit
Summary(pl.UTF-8):	Interface KDE4 dla PackageKit
Name:		kpackagekit
Version:	0.6.1
Release:	2
License:	GPL v2
Group:		X11/Applications
# get it via: svn export svn://anonsvn.kde.org/home/kde/trunk/playground/sysadmin/kpackagekit
#Source0:	http://www.kde-apps.org/CONTENT/content-files/84745-%{name}-%{version}.7z
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	34b1a1433a07d7c1dcc8b438df2ca1e3
BuildRequires:	PackageKit-qt-devel >= %{pkver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	phonon-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	strigi-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXtst-devel
Requires:	PackageKit = %{pkver}
Requires:	PackageKit-qt = %{pkver}
Requires:	kde4-kdebase-workspace
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
the KDE interface for PackageKit.

%description -l pl.UTF-8
Interface KDE4 dla PackageKit

%prep
%setup -q

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
## this is not a symlink! vvvvvvvvvvvvv
%attr(755,root,root) %{_libdir}/libkpackagekitlib.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_addrm.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_settings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_update.so
%attr(755,root,root) %{_libdir}/kde4/kded_kpackagekitd.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kpackagekitsmarticon
%{_desktopdir}/kde4/kpackagekit.desktop
%{_datadir}/apps/kpackagekit
%dir %{_datadir}/apps/KPackageKitSmartIcon
%{_datadir}/apps/KPackageKitSmartIcon/KPackageKitSmartIcon.notifyrc
%{_datadir}/dbus-1/services/org.kde.KPackageKitSmartIcon.service
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service
%{_datadir}/kde4/services/kded/kpackagekitd.desktop
%{_datadir}/kde4/services/kpk_addrm.desktop
%{_datadir}/kde4/services/kpk_settings.desktop
%{_datadir}/kde4/services/kpk_update.desktop
%{_datadir}/kde4/services/settings-add-and-remove-software.desktop
