%define debug_package %{nil}

Summary:        Qt frontend to Cscope
Name:           kscope
Version:        1.9.4
Release:        4
License: 	GPLv2+
Group: 		Development/Other
Source: 	http://ovh.dl.sourceforge.net/sourceforge/kscope/%name-%version.tar.gz
Source1:	kscope.desktop
Patch0:		kscope-1.9.4-compilefix.patch
Patch1:		kscope-1.9.4-linking.patch
Url: 		https://sourceforge.net/projects/kscope
BuildRequires:	qt4-devel
BuildRequires:	qscintilla-qt4-devel
BuildRequires:	desktop-file-utils
Requires:	cscope 
Requires:	ctags 
Requires:	graphviz

%description
KScope is a source-editing environment for KDE based on Cscope.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

sed -i 's|/usr/local|%{buildroot}%{_prefix}|g' config
for i in */*.pro; do
	sed -i 's|/lib|/%{_lib}|g' $i
done

%build
export CXXFLAGS="%{optflags} -I%{qt4include}/Qsci"
%qmake_qt4
make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p app/images/kscope.png %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

rm -f %{buildroot}%{_libdir}/*.so


%files
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/kscope.desktop
%{_datadir}/pixmaps/kscope.png


