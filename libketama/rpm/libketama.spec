Name:	    libketama	
Version:    1.0	
Release:	2%{?dist}
Summary:	a consistent hashing library
Group:      libs
License:	BSD
URL:	    https://github.com/RJ/ketama	

#git archive master --format=tar --prefix=libketama-1.0-2/ \
#./libketama | gzip |sudo tee /root/rpmbuild/SOURCES/libketama-1.0-2.tar.gz

Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
 libketama is a library for consistently hashing data across nodes.

%prep
%setup -q


%build
#%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

