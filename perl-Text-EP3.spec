%include	/usr/lib/rpm/macros.perl
Summary:	Text-EP3 perl module
Summary(pl):	Modu³ perla Text-EP3
Name:		perl-Text-EP3
Version:	1.00
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-EP3-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-EP3 - The Extensible Perl PreProcessor.

%description -l pl
Text-EP3 - The Extensible Perl PreProcessor.

%prep
%setup -q -n Text-EP3-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/ep3
%{perl_sitelib}/Text/EP3.pm
%{perl_sitelib}/auto/Text/EP3
%{_mandir}/man3/*
