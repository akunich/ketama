Name:	    libketama	
Version:    1.0.2
Release:	1%{?dist}
Summary:	a consistent hashing library
Group:      libs
License:	BSD
URL:	    https://github.com/RJ/ketama	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
 libketama is a library for consistently hashing data across nodes.

%prep
%setup -q


%build
#%%configure
cd libketama
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd libketama
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/include/ketama.h
/usr/lib/libketama.so
/usr/lib/libketama.so.1



%changelog

