%define major 5
%define libname %mklibname KF5CoreAddons %{major}
%define devname %mklibname KF5CoreAddons -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# This is only required in a BSD context, but rpm's
# cmake dependency generator doesn't understand
# conditionals well enough
%global __requires_exclude ^.*procstat.*

Name: kcoreaddons
Version:	5.101.0
Release:	2
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Core Library addons
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(gamin)
BuildRequires: shared-mime-info
Obsoletes: python-%{name} < %{EVRD}
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
Requires: accountsservice

%description
The KDE Frameworks 5 Core Library addons

%package -n %{libname}
Summary: The KDE Frameworks 5 Core Library addons
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
The KDE Frameworks 5 Core Library addons

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%autosetup -p1
%cmake_kde5 -D_KDE4_DEFAULT_HOME_POSTFIX=4

%build
%ninja -C build

%install
%ninja_install -C build

L="$(pwd)/kcoreaddons%{major}_qt.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f kcoreaddons%{major}_qt.lang
%{_bindir}/desktoptojson
%{_datadir}/mime/packages/kde5.xml
%{_datadir}/kf5
%{_datadir}/qlogging-categories5/*.categories
%{_datadir}/qlogging-categories5/kcoreaddons.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5CoreAddons
%{_libdir}/qt5/mkspecs/modules/*

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
