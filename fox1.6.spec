%define major		1.6

%define oname		fox
%define name %oname%major
%define version 1.6.25
%define release %mkrel 1

%define libname		%mklibname %{oname} %{major}


Summary:	The FOX C++ GUI Toolkit
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		Development/C++
URL:		http://www.fox-toolkit.org
Source: 	http://www.fox-toolkit.org/ftp/%{oname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libmesaglu-devel
BuildRequires:  libcups-devel
BuildRequires:  libbzip2-devel

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
Requires:	%{libname} = %{version}
Provides:	libfox-devel = %version-%release
Provides:	fox1.6-devel = %version-%release
Provides:	libfox1.6-devel = %version-%release
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
rm -rf $RPM_BUILD_ROOT

%setup -q -n %oname-%version

%build

%configure2_5x --with-opengl=mesa --enable-cups

make GL_LIBS="-lGL -lGLU"

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc/fox-1.6/* installed-docs
%multiarch_binaries %buildroot%_bindir/fox-config

rm -rf %buildroot%_prefix/fox %buildroot%_bindir/Adie.stx \
       %buildroot%_bindir/PathFinder %buildroot%_bindir/adie \
       %buildroot%_bindir/calculator %buildroot%_bindir/shutterbug \
       %buildroot%_mandir/man1/PathFinder* %buildroot%_mandir/man1/adie* \
       %buildroot%_mandir/man1/calculator* %buildroot%_mandir/man1/shutterbug*

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS LICENSE README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc doc ADDITIONS INSTALL TRACING
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


