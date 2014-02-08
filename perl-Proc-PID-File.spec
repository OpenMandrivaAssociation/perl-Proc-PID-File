%define upstream_name    Proc-PID-File
%define upstream_version 1.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A module to manage process id files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch: noarch

%description
This Perl module is useful for writers of daemons and other processes that
need to tell whether they are already running, in order to prevent multiple
process instances. The module accomplishes this via *nix-style _pidfiles_,
which are files that store a process identifier.

The module provides two interfaces: 1) a simple call, and 2) an
object-oriented interface

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.270.0-4mdv2012.0
+ Revision: 765609
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.270.0-3
+ Revision: 764136
- rebuilt for perl-5.14.x

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.270.0-2
+ Revision: 658547
- rebuild for updated spec-helper

* Sat Jul 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.270.0-1mdv2011.0
+ Revision: 554644
- import perl-Proc-PID-File


* Sun Jul 04 2010 cpan2dist 1.27-1mdv
- initial mdv release, generated with cpan2dist
