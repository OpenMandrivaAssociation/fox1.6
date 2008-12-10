%define major 1.6
%define oname fox
%define name %{oname}%{major}
%define version 1.6.34
%define release %mkrel 3

%define libname %mklibname %{oname} %{major}

Summary:	The FOX C++ GUI Toolkit
Name:		%{name}
Version:	%version
Release:	%release
License:	LGPLv2+
Group:		Development/C++
URL:		http://www.fox-toolkit.org
Source:		http://www.fox-toolkit.org/ftp/%{oname}-%{version}.tar.gz
BuildRequires:	libmesaglu-devel
BuildRequires:	libcups-devel
BuildRequires:	libbzip2-devel
BuildRequires:	libxft-devel
BuildRequires:	libxcursor-devel
BuildRequires:	libxrandr-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package -n %{libname}
Summary:	The FOX C++ GUI Toolkit - Libraries
Group:		System/Libraries

%description -n %{libname}
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package -n %{libname}-devel
Summary:	FOX header files
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	libfox-devel = %{version}-%{release}
Provides:	fox1.6-devel = %{version}-%{release}
Provides:	libfox1.6-devel = %{version}-%{release}
Conflicts:	fox1.4-devel
Conflicts:	fox1.7-devel

%description -n %{libname}-devel
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

This package contains the necessary files to develop applications
with FOX.

%prep
%setup -q -n %{oname}-%{version}

%build
%define _disable_ld_no_undefined 1
%configure2_5x \
	--with-opengl=yes \
	--enable-cups \
	--with-xft \
	--with-xcursor \
	--with-xrandr \
	--with-shape \
	--with-xshm \
	--enable-threadsafe \
	--enable-release

make

%install
rm -rf %{buildroot} installed-docs
%makeinstall_std

mv %{buildroot}%{_datadir}/doc/fox-1.6/* installed-docs
%multiarch_binaries %{buildroot}%{_bindir}/fox-config

rm -rf %buildroot%_prefix/fox %buildroot%_bindir/Adie.stx \
       %buildroot%_bindir/PathFinder %buildroot%_bindir/adie \
       %buildroot%_bindir/calculator %buildroot%_bindir/shutterbug \
       %buildroot%_mandir/man1/PathFinder* %buildroot%_mandir/man1/adie* \
       %buildroot%_mandir/man1/calculator* %buildroot%_mandir/man1/shutterbug*

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS LICENSE README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc doc ADDITIONS TRACING
%doc installed-docs
%doc %{_mandir}/man1/reswrap*
%{_bindir}/reswrap
%_bindir/fox-config
%multiarch_bindir/fox-config
%dir %{_includedir}/fox-1.6
%{_includedir}/fox-1.6/*
%{_libdir}/pkgconfig/fox.pc
%{_libdir}/*.so
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la
