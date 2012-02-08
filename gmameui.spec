Summary: Frontend for MAME
Name: gmameui
Version: 0.2.10
Release: 2%{?dist}
License: GPLv2+
Group: Applications/Emulators
URL: http://gmameui.sourceforge.net/
Source: http://downloads.sf.net/gmameui/gmameui-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel
BuildRequires: libgnome-devel
BuildRequires: expat-devel
BuildRequires: libglade2-devel
BuildRequires: gettext, bison
BuildRequires: intltool, perl(XML::Parser)
BuildRequires: libarchive-devel
BuildRequires: gnome-doc-utils

%description
GMAMEUI is a front-end program that helps you run MAME (either xmame or
sdlmame), allowing you to run your arcade games quickly and easily.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} _docs
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

# Put the docs back into place
%{__mkdir} _docs
%{__mv} %{buildroot}%{_docdir}/%{name}*/* _docs/


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc _docs/*
%{_bindir}/gmameui
%{_datadir}/applications/gmameui.desktop
%{_datadir}/pixmaps/gmameui.png
%{_datadir}/gmameui/
%{_datadir}/gnome/help/gmameui/
%{_datadir}/omf/gmameui/
%{_mandir}/man6/gmameui.6*


%changelog
* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul  5 2009 Matthias Saou <http://freshrpms.net/> 0.2.10-1
- Update to 0.2.10.
- Add new libgnome-devel and libarchive-devel build requirements.
- Re-enable translations, they build/install again.

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.2.2-3
- rebuild for new F11 features

* Sat Oct 18 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.2.2-2
- rebuild for RPM Fusion

* Fri May 16 2008 Matthias Saou <http://freshrpms.net/> 0.2.2-1
- Initial RPM package, based on the gxmame spec file.

