%include	/usr/lib/rpm/macros.perl
Summary:	Text-EP3 perl module
Summary(pl):	Modu³ perla Text-EP3
Name:		perl-Text-EP3
Version:	1.00
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-EP3-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-EP3 - The Extensible Perl PreProcessor. 

%description -l pl
Text-EP3 - The Extensible Perl PreProcessor.

%prep
%setup -q -n Text-EP3-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/EP3
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz
%attr(755,root,root) %{_bindir}/ep3

%{perl_sitelib}/Text/EP3.pm
%{perl_sitelib}/auto/Text/EP3
%{perl_sitearch}/auto/Text/EP3

%{_mandir}/man3/*
