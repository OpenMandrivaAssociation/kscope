%define name    kscope
%define version 1.6.0
%define release %mkrel 1
%define Summary KDE frontend to Cscope

%define section Applications/Development/Tools
%define title Kscope

# Work around for different libtool use in kde 
%define __libtoolize true

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release

License: 	BSD
Group: 		Development/Other
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
Source: 	http://ovh.dl.sourceforge.net/sourceforge/kscope/%name-%version.tar.bz2
Url: 		http://sourceforge.net/projects/kscope
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase-devel
BuildRequires:  libgraphviz-devel
BuildRequires:  flex bison
Requires:	cscope ctags

%description
KScope is a source-editing environment for KDE based on Cscope.

%prep
%setup -q

%build
%configure
make clean
%make

%install
rm -rf %buildroot
%makeinstall

#mdk icons
install -D -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
install -D -m 644 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png

%find_lang %{name}

%clean
rm -rf %buildroot

%post
%update_menus

%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}

%dir %{_datadir}/apps/kscope/
%{_datadir}/apps/kscope/kscopeui.rc
%{_datadir}/apps/kscope/pics/*.png
%{_datadir}/applnk/Development/kscope.desktop
%{_datadir}/icons/*/*/apps/*.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%doc %_docdir/HTML/*/%{name}/*
%_datadir/apps/kscope/kscope_config
