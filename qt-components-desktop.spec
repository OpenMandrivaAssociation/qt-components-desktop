%define gitversion 20110608
%define debug_package %{nil}

Summary:	A Desktop Qt Quick Component
Name:		qt-components-desktop
Version:	%gitversion
Release:	3
License:	LGPL
Group:		Development/KDE and Qt
Url:		http://qt.gitorious.org/qt-components/desktop
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This contains the research on desktop components for QML.

These files are used by MCC2 and MPM infrastructure.

%prep
%setup -q

%build
qmake
%make

%install
rm -rf %buildroot
mkdir -p %{buildroot}/%_datadir/mandriva/qt-components/desktop
cp -R components %{buildroot}/%{_datadir}/mandriva/qt-components/desktop
cp -R examples %{buildroot}/%{_datadir}/mandriva/qt-components/desktop

%files
%defattr(-,root,root)
%_datadir/mandriva/qt-components


%changelog
* Mon Jun 13 2011 Wiliam Alves de Souza <wiliam@mandriva.com> 20110608-1mdv2011.0
+ Revision: 684636
- Updated

* Thu May 26 2011 Paulo Belloni <paulo@mandriva.com> 20110526-1
+ Revision: 679214
- Changes to relocate qt-components-desktop to /usr/share/mandriva

* Wed Apr 27 2011 Eugeni Dodonov <eugeni@mandriva.com> 20110413-1
+ Revision: 659748
- Add missing BR
- Fix buildarch
- Fix url, group and license.
- Imported to cooker
- Created package structure for qt-components-desktop.

