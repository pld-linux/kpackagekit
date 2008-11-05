
%define		qtver	4.4.1

Summary:	the KDE interface for PackageKit
Summary(pl.UTF-8):	Interface KDE4 dla PackageKit
Name:		kpackagekit
Version:	0.3.1
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kde-apps.org/CONTENT/content-files/84745-%{name}-%{version}.tar.bz2
# Source0-md5:	eb4db65cf2b252dc39eb844ccc174a4d
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	qpackagekit-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	PackageKit
Requires:	PolicyKit-kde
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
the KDE interface for PackageKit.

%description -l pl.UTF-8
Interface KDE4 dla PackageKit

%prep
%setup -q -n KPackageKit

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
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
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_addrm.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_settings.so
%attr(755,root,root) %{_libdir}/kde4/kcm_kpk_update.so
%attr(755,root,root) %{_libdir}/kde4/kded_kpackagekitd.so
%{_desktopdir}/kde4/kpackagekit.desktop
%{_datadir}/apps/KPackageKit
%{_datadir}/apps/kpackagekit
%{_datadir}/kde4/services/kded/kpackagekitd.desktop
%{_datadir}/kde4/services/kpk_addrm.desktop
%{_datadir}/kde4/services/kpk_settings.desktop
%{_datadir}/kde4/services/kpk_update.desktop
%{_datadir}/kde4/services/settings-add-and-remove-software.desktop
