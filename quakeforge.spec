#
# Conditional build:
# _without_alsa - without ALSA
# _without_svga - without SVGAlib support
#
Summary:	3D game engine based on id Software's Quake engine
Summary(pl):	Silnik gry 3D bazuj±cy na silniku Quake id Software
Name:		quakeforge
Version:	0.3.0
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	http://download.sourceforge.net/quake/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-ac_fix.patch
Patch2:		%{name}-acconfig.h.patch
Patch3:		%{name}-ah_fixes.patch
Patch4:		%{name}-compat.patch
Icon:		quakeforge.xpm
URL:		http://www.quakeforge.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	libtool
%{!?_without_svgalib:BuildRequires:	svgalib-devel}
BuildRequires:	libggi-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%ifarch sparc
%define		_without_alsa	1
%endif

%ifnarch %{ix86}
%define		_without_svga	1
%endif

%description
3D game engine server based on id Software's Quake engine.

%description -l pl
Serwer gry 3D bazuj±cy na silniku Quake id Software.

%package svgalib
Summary:	quakeforge client for svgalib
Summary(pl):	klient quakeforge pod svgalib
Group:		Applications/Games

%description  svgalib
Quakeforge client for svgalib.

%description svgalib -l pl
Klient quakeforge pod svgalib.

%package sdl
Summary:	quakeforge client for SDL
Summary(pl):	klient quakeforge pod SDL
Group:		Applications/Games

%description  sdl
Quakeforge client for SDL.

%description sdl -l pl
Klient quakeforge pod SDL.

%package x11
Summary:	quakeforge client for x11
Summary(pl):	klient quakeforge pod x11
Group:		Applications/Games

%description  x11
Quakeforge client for x11.

%description x11 -l pl
Klient quakeforge pod x11.

%package fbdev
Summary:        quakeforge client for fbdev
Summary(pl):    klient quakeforge pod fbdev
Group:          Applications/Games

%description  fbdev
Quakeforge client for fbdev.

%description fbdev -l pl
Klient quakeforge pod fbdev.

%package ggi
Summary:        quakeforge client for ggi
Summary(pl):    klient quakeforge pod ggi
Group:          Applications/Games

%description  ggi
Quakeforge client for ggi.

%description ggi -l pl
Klient quakeforge pod ggi.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
autoheader
aclocal
%{__autoconf}
%{__automake}
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
	%{?_without_alsa:--disable-alsa} \
	%{?_without_svga:--without-svga}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/games/%{name},%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README doc/readme.txt
%attr(755,root,root) %{_bindir}/qf-server
%dir %{_datadir}/games/%{name}
%{_infodir}/*info*
%{_mandir}/man*/*

%{?!_without_svga:%files svgalib}
%{?!_without_svga:%defattr(644,root,root,755)}
%{?!_without_svga:%attr(755,root,root) %{_bindir}/qf-client-svga}

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-sdl

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-x11
%{_applnkdir}/Games/*
%{_pixmapsdir}/*

%files fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-fbdev

%files ggi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-ggi
