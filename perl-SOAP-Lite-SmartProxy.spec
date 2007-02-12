#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SOAP
%define		pnam	Lite-SmartProxy
Summary:	SOAP-Lite-SmartProxy - redirect/forward a SOAP client or request
Summary(pl.UTF-8):   SOAP-Lite-SmartProxy - przekierowywanie/przekazywanie klientów lub żądań SOAP
Name:		perl-SOAP-Lite-SmartProxy
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc97f030cbcdae32212e5159792e1c06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# not BRed yet for test
Requires:	perl-SOAP-Lite >= 0.46
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SmartProxy package is intended for use in a multi-server setting
where one or more servers may not be directly accessible to client
side scripts. The SmartProxy package makes request redirection and
forwarding on a per class basis easy. Client scripts need not know
which server is appropriate for a specific request and may make all
requests from a single master server which can be relied upon to
redirect clients to the server currently fulfilling a given request.
The relieves a maintenance burden on the client side. The server may
also redirect clients to a new class name or fully qualified action
URI (methods and arguments are assumed to remain constant however).

%description -l pl.UTF-8
Pakiet SmartProxy jest przeznaczony do używania w środowisku
wieloserwerowym, gdzie jeden lub więcej serwerów nie są bezpośrednio
dostępne dla skryptów od strony klienta. Pakiet SmartProxy w prosty
sposób przekierowuje i przekazuje żądania w zależności od klasy.
Skrypty klienckie nie muszą wiedzieć, który serwer jest właściwy dla
danego żądania i mogą wysyłać wszystkie żądania do pojedynczego
serwera głównego, który wykonuje przekierowania klientów do serwera
aktualnie wykonującego dane żądanie. Zdejmuje to ciężar zarządzania ze
strony klienckiej. Serwer może także przekierowywać klientów na nową
nazwę klasy lub pełni URI dla akcji (jednak zakłada się, że metody i
argumenty pozostają stałe).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache/SmartProxy.pm
%{perl_vendorlib}/SOAP/Transport/HTTPX.pm
%{_mandir}/man3/*
