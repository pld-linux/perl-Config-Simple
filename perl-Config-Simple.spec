#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	Simple
Summary:	Config::Simple - simple configuration file class
Summary(pl.UTF-8):	Config::Simple - prosta klasa do obsługi plików konfiguracyjnych
Name:		perl-Config-Simple
Version:	4.59
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/SHERZODR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96513b61c7db591339ce2577878a3b32
URL:		http://search.cpan.org/dist/Config-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::Simple is a class representing configuration file object. It
supports several configuration file syntax and tries to identify the
file syntax to parse them accordingly. Library supports parsing,
updating and creating configuration files.

%description -l pl.UTF-8
Config::Simple stanowi klasę reprezentującą obiekty plików
konfiguracyjnych. Zawiera wsparcie dla kilku składni plików
konfiguracyjnych a próbuje zidentyfikować rodzaj używanej w danym
pliku składni poprzez kolejne próby ich analizy. Biblioteka wspiera
analizę, aktualizację i tworzenie plików konfiguracyjnych.

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
%{perl_vendorlib}/Config/Simple.pm
%{perl_vendorlib}/auto/Config/Simple
%{_mandir}/man3/Config::Simple.3pm*
