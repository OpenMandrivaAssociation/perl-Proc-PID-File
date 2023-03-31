%define modname	Proc-PID-File
%define modver	1.28

Summary:	A module to manage process id files
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This Perl module is useful for writers of daemons and other processes that
need to tell whether they are already running, in order to prevent multiple
process instances. The module accomplishes this via *nix-style _pidfiles_,
which are files that store a process identifier.

The module provides two interfaces: 1) a simple call, and 2) an
object-oriented interface

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README META.yml Changes LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

