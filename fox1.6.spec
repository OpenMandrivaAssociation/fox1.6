%define oname fox

%define libname %mklibname %{oname} 1.6 0
%define develname %mklibname %{name} -d
%define debug_package %{nil}

Summary:	The FOX C++ GUI Toolkit
Name:		fox1.6
Version:	1.6.47
Release:	2
License:	LGPLv2+
Group:		Development/C++
URL:		http://www.fox-toolkit.org
Source:		http://www.fox-toolkit.org/ftp/%{oname}-%{version}.tar.gz
Patch0:		fox-1.6.36-fix-str-fmt.patch
Patch1:		fox-1.6.43-fix-linkage.patch
BuildRequires:	bzip2-devel
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xrandr)

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

%package -n %{develname}
Summary:	FOX header files
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	fox1.6-devel = %{version}-%{release}
Provides:	libfox1.6-devel = %{version}-%{release}
Conflicts:	fox1.4-devel
Conflicts:	fox1.7-devel

%description -n %{develname}
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
%patch0 -p0
%patch1 -p0

%build
LDFLAGS="-lfontconfig" %configure2_5x \
    --with-opengl=yes \
    --with-xft \
    --with-xcursor \
    --with-xrandr \
    --with-shape \
    --with-xshm \
    --disable-static \
    --enable-release

%make

%install
%makeinstall_std

mv %{buildroot}%{_datadir}/doc/fox-1.6/* installed-docs
%multiarch_binaries %{buildroot}%{_bindir}/fox-config

rm -rf %{buildroot}%{_prefix}/fox %{buildroot}%{_bindir}/Adie.stx \
       %{buildroot}%{_bindir}/PathFinder %{buildroot}%{_bindir}/adie \
       %{buildroot}%{_bindir}/calculator %{buildroot}%{_bindir}/shutterbug \
       %{buildroot}%{_mandir}/man1/PathFinder* %{buildroot}%{_mandir}/man1/adie* \
       %{buildroot}%{_mandir}/man1/calculator* %{buildroot}%{_mandir}/man1/shutterbug*

%files -n %{libname}
%{_libdir}/*-1.6.so.0*

%files -n %{develname}
%doc doc ADDITIONS TRACING
%doc installed-docs
%doc %{_mandir}/man1/reswrap*
%{_bindir}/reswrap
%{_bindir}/fox-config
%multiarch_bindir/fox-config
%dir %{_includedir}/fox-1.6
%{_includedir}/fox-1.6/*
%{_libdir}/pkgconfig/fox.pc
%{_libdir}/*.so


