#
# Conditional build:
# bcond_off_alsa - without ALSA
#
Summary:	3D game engine based on id Software's Quake engine
Summary(pl):	Silnik gry 3D bazuj±cy na silniku Quake id Software
Name:		quakeforge
Version:	0.3.0
Release:	3
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	http://download.sourceforge.net/quake/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac_fix.patch
Patch2:		%{name}-acconfig.h.patch
Patch3:		%{name}-ah_fixes.patch
Icon:		quakeforge.xpm
URL:		http://www.quakeforge.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
%ifnarch sparc
%{!?bcond_off_alsa:BuildRequires:	alsa-lib-devel}
%endif
BuildRequires:	svgalib-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
3D game engine server based on id Software's Quake engine.

%description -l pl
Serwer gry 3D bazuj±cy na silniku Quake id Software.

%package svgalib
Summary:	quakeforge client for svgalib
Summary(pl):	klient quakeforge pod svgalib
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry

%description  svgalib
Quakeforge client for svgalib.

%description -l pl svgalib
Klient quakeforge pod svgalib.

%package sdl
Summary:	quakeforge client for SDL
Summary(pl):	klient quakeforge pod SDL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry

%description  sdl
Quakeforge client for SDL.

%description -l pl sdl
Klient quakeforge pod SDL.

%package x11
Summary:	quakeforge client for x11
Summary(pl):	klient quakeforge pod x11
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry

%description  x11
Quakeforge client for x11.

%description -l pl x11
Klient quakeforge pod x11.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoheader
aclocal
autoconf
automake -a -c
%configure \
	--with-x \
	--with-libz \
	--enable-vidmode \
	--enable-dga \
	--with-glx \
	--with-sharepath=%{_datadir}/games/%{name} \
	--with-global-cfg=%{_sysconfdir}/%{name}.conf \
	--with-server \
	--with-newstyle \
	%{?bcond_off_alsa:--disable-alsa}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/%{name},%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS NEWS README doc/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/qf-server
%dir %{_datadir}/games/%{name}
%{_infodir}/*info*
%{_mandir}/man*/*

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-svga

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-sdl

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-x11
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
