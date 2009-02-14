%define name    kscope
%define version 1.9.2
%define release %mkrel 1
%define Summary Qt frontend to Cscope

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License: 	GPLv2+
Group: 		Development/Other
Source: 	http://ovh.dl.sourceforge.net/sourceforge/kscope/%name-%version.tar.gz
Source1:	kscope.desktop
Patch0:		kscope-1.9.0-compilefix.patch
Url: 		http://sourceforge.net/projects/kscope
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel qscintilla-qt4-devel
BuildRequires:	desktop-file-utils
Requires:	cscope ctags graphviz

%description
KScope is a source-editing environment for KDE based on Cscope.

%prep
%setup -q
%patch0 -p1
sed -i 's|/usr/local|%{buildroot}%{_prefix}|g' config
for i in */*.pro; do
	sed -i 's|/lib|/%{_lib}|g' $i
done

%build
export CXXFLAGS="%{optflags} -I%{qt4include}/Qsci"
%qmake_qt4
make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p app/images/kscope.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

rm -f %{buildroot}%{_libdir}/*.so

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/kscope.desktop
%{_datadir}/pixmaps/kscope.png
