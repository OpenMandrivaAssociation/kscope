%define name    kscope
%define version 1.6.2
%define release %mkrel 1
%define Summary KDE frontend to Cscope

# Work around for different libtool use in kde 
%define __libtoolize true

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License: 	BSD
Group: 		Development/Other
Source: 	http://ovh.dl.sourceforge.net/sourceforge/kscope/%name-%version.tar.gz
Url: 		http://sourceforge.net/projects/kscope
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase3-devel
BuildRequires:  libgraphviz-devel
BuildRequires:  flex bison
Requires:	cscope ctags

%description
KScope is a source-editing environment for KDE based on Cscope.

%prep
%setup -q

%build
%configure_kde3
%make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %{buildroot}%{_kde3_datadir}/applications
desktop-file-install --vendor='' --delete-original \
	--dir %{buildroot}%{_kde3_datadir}/applications/ \
	--add-category='TextEditor' \
	%{buildroot}%{_kde3_datadir}/applnk/Development/kscope.desktop

%find_lang %{name} --with-html

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

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde3_bindir}/%{name}
%{_kde3_appsdir}/%{name}
%{_kde3_datadir}/applications/kscope.desktop
%{_kde3_iconsdir}/*/*/apps/*.png
