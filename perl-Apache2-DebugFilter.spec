%define upstream_name    Apache2-DebugFilter
Name:		perl-%{upstream_name}
Version:	0.02
Release:	6

Summary:	Apache2::DebugFilter - Debug mod_perl and native Apache2 filters
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Apache2/%{upstream_name}-%{version}.tar.bz2

BuildRequires:	make
BuildRequires:	apache-mod_perl
BuildRequires:	apache-mod_perl-devel
BuildRequires:	perl-devel
BuildRequires:	perl(Apache::Test) >= 1.25
BuildArch:	noarch

%description
Apache2::DebugFilter - Debug mod_perl and native Apache2 filters.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Apache2/DebugFilter.pm
%{_mandir}/*/*

