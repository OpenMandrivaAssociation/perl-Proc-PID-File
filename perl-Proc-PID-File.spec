%define upstream_name    Proc-PID-File
%define upstream_version 1.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A module to manage process id files
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml Changes LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


