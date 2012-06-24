#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	SOAP
%define	pnam	Lite-SmartProxy
Summary:	SOAP-Lite-SmartProxy - redirect/forward a SOAP client or request
Summary(pl):	SOAP-Lite-SmartProxy - przekierowywanie/przekazywanie klient�w lub ��da� SOAP
Name:		perl-SOAP-Lite-SmartProxy
Version:	0.11
Release:	1
# same as perl
License:	GPL or Artistic
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

%description -l pl
Pakiet SmartProxy jest przeznaczony do u�ywania w �rodowisku
wieloserwerowym, gdzie jeden lub wi�cej serwer�w nie s� bezpo�rednio
dost�pne dla skrypt�w od strony klienta. Pakiet SmartProxy w prosty
spos�b przekierowuje i przekazuje ��dania w zale�no�ci od klasy.
Skrypty klienckie nie musz� wiedzie�, kt�ry serwer jest w�a�ciwy dla
danego ��dania i mog� wysy�a� wszystkie ��dania do pojedynczego
serwera g��wnego, kt�ry wykonuje przekierowania klient�w do serwera
aktualnie wykonuj�cego dane ��danie. Zdejmuje to ci�ar zarz�dzania ze
strony kienckiej. Serwer mo�e tak�e przekierowywa� klient�w na now�
nazw� klasy lub pe�ni URI dla akcji (jednak zak�ada si�, �e metody i
argumenty pozostaj� sta�e).

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
