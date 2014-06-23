%global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)
%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")
%global php_includedir  %(php-config --include-dir 2>/dev/null || echo "undefined")
%global php_version %(php-config --version 2>/dev/null || echo 0)

Name:       php-ketama
Version:    1.0.2
Release:    1%{?dist}
Summary:    The php ketama extension

Group:      Development/Languages
License:    PHP
URL:        https://github.com/RJ/ketama
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: php-devel
Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_apiver}


%description
The php ketama extension

%prep
%setup -q


%build
cd php_ketama
%{_bindir}/phpize
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd php_ketama
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%{__mkdir} -p $RPM_BUILD_ROOT%{_sysconfdir}/php.d
echo "extension=ketama.so" >  $RPM_BUILD_ROOT%{_sysconfdir}/php.d/ketama.ini

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/php.d/ketama.ini
%{php_extdir}/ketama.so

%changelog
