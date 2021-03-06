Summary:	A shell/frontend for the command line task list manager taskwarrior
Name:		tasksh
Version:	1.2.0
Release:	2
License:	MIT
Group:		Applications
Source0:	https://www.taskwarrior.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c05f7b7b0203f3f4e44a4d32f24e5746
URL:		http://taskwarrior.org/
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A shell/frontend for the command line task list manager taskwarrior.

%prep
%setup -q

%build
%cmake -B build
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
