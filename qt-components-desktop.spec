%define debug_package %{nil}
%define gitversion 20110608

Summary:	A Desktop Qt Quick Component
Name:		qt-components-desktop
Version:	%{gitversion}
Release:	12
License:	LGPLv2
Group:		Development/KDE and Qt
Url:		https://qt.gitorious.org/qt-components/desktop
Source0:	%{name}-%{version}.tar.bz2
Source1:	qt-components-desktop.rpmlintrc
BuildRequires:	qt4-devel

%description
This contains the research on desktop components for QML.

These files are used by MCC2 and MPM infrastructure.

%prep
%setup -q

%build
qmake
%make

%install
mkdir -p %{buildroot}/%{_datadir}/mandriva/qt-components/desktop
cp -R components %{buildroot}/%{_datadir}/mandriva/qt-components/desktop
cp -R examples %{buildroot}/%{_datadir}/mandriva/qt-components/desktop

%files
%{_datadir}/mandriva/qt-components

