%define gitversion 20110608


Summary:	A Desktop Qt Quick Component
Name:		qt-components-desktop
Version:	%gitversion
Release:	%mkrel 1
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
