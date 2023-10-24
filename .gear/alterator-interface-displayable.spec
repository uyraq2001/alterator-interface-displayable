Name: alterator-interface-displayable
Version: 0.1.0
Release: alt1

Summary: XML and polkit rules files for ru.basealt.alterator.displayable interface.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-interface-displayable

BuildArch: noarch

Source0: %name-%version.tar

%description
XML and polkit rules files for ru.basealt.alterator.displayable interface, using in Alterator Browser to show info for DBus object.

%prep
%setup

%install
mkdir -p %buildroot%{_datadir}/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.displayable.xml %buildroot%{_datadir}/dbus-1/interfaces
mkdir -p %buildroot%{_sysconfdir}/polkit-1/rules.d
install -v -p -m 644 -D 48-alterator-interface-displayable.rules %buildroot%{_sysconfdir}/polkit-1/rules.d

%files
%{_datadir}/dbus-1/interfaces/ru.basealt.alterator.displayable.xml
%{_sysconfdir}/polkit-1/rules.d/48-alterator-interface-displayable.rules

%changelog
* Tue Oct 24 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
