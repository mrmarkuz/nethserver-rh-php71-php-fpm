Name: nethserver-rh-php71-php-fpm
Version: 0.0.1
Release: 1%{?dist}
Summary: NethServer rh-php71-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php71, rh-php71-php-fpm

%description
Basic support for PHP 7.1 using SCL

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Tue Feb 26 2018 Markus Neuberger <info@markusneuberger.at> - 1.0.0-1
- First release
- For Moodle 3.4
- Add /etc/opt/rh/rh-php71/php-fpm.d/www.conf template for port 9071
