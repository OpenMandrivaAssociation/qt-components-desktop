%define gitversion 20110413


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
BuildArch:	noarch

%description
This contains the research on desktop components for QML.

These files are used by MCC2 infrastructure.

%prep
%setup -q

%build
qmake
%make

%install
rm -rf %buildroot
mkdir -p %{buildroot}/%_datadir/mandriva/mcc2/frontends/users/views
mkdir -p %{buildroot}/%_datadir/mandriva/mcc2/frontends/services/views
cp -R components %{buildroot}/%{_datadir}/mandriva/mcc2/frontends/users/views/
cp -R components %{buildroot}/%{_datadir}/mandriva/mcc2/frontends/services/views/

%files
%defattr(-,root,root)
%_datadir/mandriva/mcc2/frontends/
