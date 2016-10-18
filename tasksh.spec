Summary:	A shell/frontend for the command line task list manager taskwarrior
Name:		tasksh
Version:	1.1.0
Release:	2
License:	MIT
Group:		Applications
Source0:	http://www.taskwarrior.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	54dda1da1a802924dcc89554b6af1ac4
URL:		http://taskwarrior.org/
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A shell/frontend for the command line task list manager taskwarrior.

%prep
%setup -q

%build
%cmake

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
