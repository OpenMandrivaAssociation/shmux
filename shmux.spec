%define name shmux
%define version 1.0.2
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Program for executing the same command on many hosts in parallel
License: 	GPL
Group:		Networking/Remote access
Url: 		http://web.taranis.org/shmux/
Source0: 	%{name}-%{version}.tgz
BuildRequires:  pcre-devel
BuildRequires:  ncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}


%description
Shmux is program for executing the same command on many hosts in parallel.
For each target, a child process is spawned by shmux, and a shell on the 
target obtained one of the supported methods: rsh, ssh, or sh. The output 
produced by the children is received by shmux and either (optionally) output 
in turn to the user using an easy to read format, or written to files for
later processing making it well suited for use in scripts.

%prep 
%setup -q -n %name-%{version}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc tests/* CHANGES INSTALL LICENSE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%name.1*
%_datadir/%name



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 614862
- the mass rebuild of 2010.1 packages

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 1.0.2-1mdv2010.1
+ Revision: 497220
- release 1.0.2

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.0-0.beta9.4mdv2010.0
+ Revision: 445105
- rebuild

* Mon Mar 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-0.beta9.3mdv2009.1
+ Revision: 355572
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request
    - import shmux


* Wed Jul 12 2006 Lenny Cartier <lenny@mandriva.com> 1.0-0.beta9.1mdv2007.0
- beta9

* Tue Mar 22 2005 Antoine Ginies <aginies@n1.mandrakesoft.com> 1.0-0.beta6.2mdk
- rebuild

* Thu Dec 16 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0-0.beta6.1mdk
- 1.0b6

* Wed Jun 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.13b-1mdk
- 0.13b

* Wed May 26 2004  <mdkc@n2.mandrakesoft.com> 0.12b-1mdk
- first mandrake release
