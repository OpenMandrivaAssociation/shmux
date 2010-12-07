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

