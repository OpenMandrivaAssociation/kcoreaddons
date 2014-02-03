%define major 5
%define libname %mklibname KF5CoreAddons %{major}
%define devname %mklibname KF5CoreAddons -d
%define debug_package %{nil}

Name: kcoreaddons
Version: 4.95.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 Core Library addons
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: extra-cmake-modules5
BuildRequires: shared-mime-info
BuildRequires: qmake5
Requires: %{libname} = %{EVRD}

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

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_datadir}/mime/packages/kde5.xml

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5CoreAddons
