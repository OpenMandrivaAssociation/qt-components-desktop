%define gitversion 20110413


Summary:	A Desktop Qt Quick Component
Name:		qt-components-desktop
Version:	%gitversion
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Configuration/Boot and Init
Url:		http://qt.gitorious.org/qt-components
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
