%define pkgname		feedparser
%define version		4.1
%define __python	%{_bindir}/python2.4

Summary:       Parse RSS and Atom feeds in Python
Name:          python2.4-feedparser
Version:       %{version}
Release:       %mkrel 8
Source0:       http://ovh.dl.sourceforge.net/sourceforge/%{pkgname}/%{pkgname}-%{version}.tar.bz2
License:       BSD
URL:           http://feedparser.org/
Group:         Development/Python
%if %{mdkversion} <= 200800
BuildRoot:     %{_tmppath}/%{name}-%{version}-buildroot
%endif
Requires:      python2.4
BuildRequires: python2.4-devel
BuildArch:     noarch

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%prep
%setup -q -n %{pkgname}-%{version} -c  
perl -pi -e 's/\r\n$/\n/' $(find docs -type f)

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc LICENSE README docs/
