#
# Conditional build:
# _without_alsa - without ALSA
# _without_svga - without SVGAlib support
#
%ifarch sparc
%define			_without_alsa	1
%endif

%ifnarch %{ix86}
%define			_without_svga	1
%endif

Summary:	3D game engine based on id Software's Quake engine
Summary(pl):	Silnik gry 3D bazuj±cy na silniku Quake id Software
Name:		quakeforge
Version:	0.5.1.20020712
Release:	2
License:	GPL
Group:		Applications/Games
# From http://www.quakeforge.net/files/quakeforge-current.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.png
Source2:	%{name}-servers.tgz
URL:		http://www.%{name}.net/
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
BuildRequires:	nas-devel
%{!?_without_svga:BuildRequires: svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define 	_xbindir	/usr/X11R6/bin

%description
QuakeForge is a source port of Quake and QuakeWorld, the successors to
id Software's very popular DOOM series. Its primary development goal
is to remain compatible with the original games released by id
Software while adding portability and optional extensions to enhance
gameplay.

%description -l pl
QuakeForge jest portem ¼róde³ gier Quake i QuakeWorld - sukcesorów
bardzo popularnej serii DOOM firmy id Software. Podstawowym celem
projektu jest zachowanie zgodno¶ci z oryginalnymi odpowiednikami
tych¿e gier przy jednoczesnym dodaniu opcjonalnych rozszerzeñ
s³u¿±cych podniesieniu jako¶ci zabawy.

%package cd-linux
Summary:	QuakeForge - linux CD plugin
Summary(pl):	QuakeForge - wtyczka CD pod linuxa
Group:		Applications/Games

%description cd-linux
QuakeForge - linux CD plugin

%description cd-linux -l pl
QuakeForge - wtyczka CD pod linuxa

%package cd-sdl
Summary:	QuakeForge - sdl CD plugin
Summary(pl):	QuakeForge - wtyczka CD pod sdl
Group:		Applications/Games

%description cd-sdl
QuakeForge - sdl CD plugin

%description cd-sdl -l pl
QuakeForge - wtyczka CD pod sdl

%package devel
Summary:	QuakeForge - headers and devel libs
Summary(pl):	QuakeForge - pliki nag³ówkowe
Group:		Applications/Games

%description devel
QuakeForge - headers and devel libs

%description devel -l pl
QuakeForge - pliki nag³ówkowe

%package fbdev
Summary:	QuakeForge client for fbdev
Summary(pl):	Klient QuakeForge pod fbdev
Group:		Applications/Games

%description fbdev
Quakeforge client for fbdev.

%description fbdev -l pl
Klient QuakeForge pod fbdev.

%package glx
Summary:	QuakeForge client for glx
Summary(pl):	Klient QuakeForge pod glx
Group:		Applications/Games

%description  glx
Quakeforge client for glx.

%description glx -l pl
Klient QuakeForge pod glx.

%package libs-gl
Summary:	QuakeForge - OpenGL renderer libraries
Summary(pl):	QuakeForge - biblioteki renderujace OpenGL
Group:		Applications/Games

%description libs-gl
QuakeForge - OpenGL renderer libraries

%description libs-gl -l pl
QuakeForge - biblioteki renderujace OpenGL

%package libs-sw
Summary:	QuakeForge - Software renderer libraries
Summary(pl):	QuakeForge - biblioteki do renderowania programowego
Group:		Applications/Games

%description libs-sw
QuakeForge - Software renderer libraries

%description libs-sw -l pl
QuakeForge - biblioteki do renderowania programowego

%package sdl
Summary:	QuakeForge client for sdl
Summary(pl):	Klient QuakeForge pod sdl
Group:		Applications/Games

%description  sdl
Quakeforge client for sdl.

%description sdl -l pl
Klient QuakeForge pod sdl.

%package sdl32
Summary:	QuakeForge client for sdl32
Summary(pl):	Klient QuakeForge pod sdl32
Group:		Applications/Games

%description  sdl32
Quakeforge client for sdl32.

%description sdl -l pl
Klient QuakeForge pod sdl32.

%package servers
Summary:	QuakeForge Servers
Summary(pl):	Serwery QuakeForge
Group:		Applications/Games

%description servers
QuakeForge Servers.

%description servers -l pl
Serwery QuakeForge.

%package sgl
Summary:	QuakeForge client for sdl-gl
Summary:	Klient QuakeForge pod sdl-gl
Group:		Applications/Games

%description sgl
QuakeForge client for sdl-gl.

%description sgl -l pl
Klient QuakeForge pod sdl-gl.

%package snd-alsa
Summary:	ALSA sound plugin for QuakeForge
Summary(pl):	Wtyczka d¼wiêkowa ALSA dla QuakeForge
Group:		Applications/Games

%description snd-alsa
The ALSA plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%description snd-alsa -l pl
Wtyczka ALSA dla QuakeForge dostarcza cyfrowe wyj¶cie d¼wiêkowe dla
klientów gry.

%package snd-oss
Summary:	OSS sound plugin for QuakeForge
Summary(pl):	Wtyczka d¼wiêkowa OSS dla QuakeForge
Group:		Applications/Games

%description snd-oss
The OSS plugin for QuakeForge provides digital audio output (using
OSS/Linux, OSS/Free, or kernel sound) for QuakeForge targets that
contain clients.

NOTE: This plugin does not work on all systems, since it uses
memory-mapped I/O for the output device. If you have trouble, try the
%{name}-snd-alsa package.

%description snd-oss -l pl
Wtyczka OSS dla QuakeForge dostarcza cyfrowe wyj¶cie d¼wiekowe
(u¿ywaj±ce OSS/Linux, OSS/Free lub obs³ugi d¼wiêku wkompilowanej w
kernel) dla klientów gry.

UWAGA: Ta wtyczka nie dzia³a na wszystkich systemach, gdy uzywaj± one
mapowanego w pamiêci I/O dla urz±dzenia wyj¶ciowego. Jesli masz z ni±
k³opoty - spróbuj u¿yæ pakietu %{name}-snd-alsa.

%package snd-sdl
Summary:	SDL sound plugin for QuakeForge
Summary(pl):	Wtyczka d¼wiêkowa SDL dla QuakeForge
Group:		Applications/Games

%description snd-sdl
The SDL plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%description snd-sdl -l pl
Wtyczka SDL dla QuakeForge dostarcza cyfrowe wyj¶cie d¼wiêkowe dla
klientów gry.

%package static
Summary:	QuakeForge 3D game engine - static libraries
Summary(pl):	Silnik gry 3D QuakeForge - biblioteki statyczne
Group:		Applications/Games

%description static
QuakeForge 3D game engine - static libraries

%description static -l pl
Silnik gry 3D QuakeForge - biblioteki statyczne

%package svga
Summary:	QuakeForge client for svgalib
Summary(pl):	Klient QuakeForge pod svgalib
Group:		Applications/Games

%description  svga
Quakeforge client for svgalib.

%description svga -l pl
Klient QuakeForge pod svgalib.

%package utils
Summary:	QuakeForge - utility programs
Summary(pl):	QuakeForge - programy narzêdziowe
Group:		Applications/Games

%description utils
%description utils -l pl

%package x11
Summary:	QuakeForge client for x11
Summary(pl):	Klient QuakeForge pod x11
Group:		Applications/Games

%description x11
Quakeforge client for x11.

%description x11 -l pl
Klient QuakeForge pod x11.

%prep
%setup -q -n %{name}

%build
aclocal
autoheader
libtoolize --automake
%{__automake}
%{__autoconf}
%configure \
	--with-x \
	--enable-vidmode \
	--enable-dga \
	--with-user-cfg="~/.%{name}/%{name}.conf" \
	%{?_without_alsa:--disable-alsa} \
	%{?_without_svga:--without-svga}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_datadir}/games/%{name}/qw} \
	$RPM_BUILD_ROOT{%{_xbindir},%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/{*glx,*sdl*,*sgl,*x11} $RPM_BUILD_ROOT%{_xbindir}

install  %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
cp RPM/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}

cd $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/init.d
tar zxfv %{SOURCE2}
cd -

qfver="glx sdl sdl32 sgl x11"

for f in $qfver; do
	desktopfile="$RPM_BUILD_ROOT%{_applnkdir}/Games/qw-client-$f.desktop"
	echo "[Desktop Entry]\nName=QuakeWorld ($f)\nExec=qw-client-$f \
	\nIcon=%{name}.png\nTerminal=0\nType=Application" > $desktopfile

	desktopfile="$RPM_BUILD_ROOT%{_applnkdir}/Games/nq-$f.desktop"
	echo "[Desktop Entry]\nName=Quake ($f)\nExec=nq-$f \
	\nIcon=%{name}.png\nTerminal=0\nType=Application" > $desktopfile
done

mv doc/man/%{name}* $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf doc/{CVS,Makefile*,man,config/{CVS,gib/CVS},data/{CVS,docs/CVS},ideas/CVS}

%clean
rm -rf $RPM_BUILD_ROOT

%post servers
/sbin/chkconfig --add qw-serverd
if [ -f /var/lock/subsys/qw-serverd ]; then
	/etc/rc.d/init.d/qw-serverd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/qw-serverd start\" to start QuakeWorld Server."
fi
/sbin/chkconfig --add nq-serverd
if [ -f /var/lock/subsys/nq-serverd ]; then
	/etc/rc.d/init.d/nq-serverd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/nq-serverd start\" to start NQuake Server."
fi
/sbin/chkconfig --add qw-masterd
if [ -f /var/lock/subsys/qw-masterd ]; then
	/etc/rc.d/init.d/qw-masterd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/qw-masterd start\" to start QuakeWorld Master."
fi

%preun servers
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/qw-serverd ]; then
		/etc/rc.d/init.d/qw-serverd stop 1>&2
	fi
	/sbin/chkconfig --del qw-serverd
fi
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/nq-serverd ]; then
		/etc/rc.d/init.d/nq-serverd stop 1>&2
	fi
	/sbin/chkconfig --del nq-serverd
fi
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/qw-masterd ]; then
		/etc/rc.d/init.d/qw-masterd stop 1>&2
	fi
	/sbin/chkconfig --del qw-masterd
fi

%files
%defattr(644,root,root,755)
%doc COPYING INSTALL TODO doc/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/id1
%dir %{_datadir}/games/%{name}/qw
%attr(755,root,root)%{_libdir}/libQFcd.so.*
%attr(755,root,root)%{_libdir}/libQFconsole.so.*
%attr(755,root,root)%{_libdir}/libQFcsqc.so.*
%attr(755,root,root)%{_libdir}/libQFgamecode.so.*
%attr(755,root,root)%{_libdir}/libQFgamecode_builtins.so.*
%attr(755,root,root)%{_libdir}/libQFjs.so.*
%attr(755,root,root)%{_libdir}/libQFmodels.so.*
%attr(755,root,root)%{_libdir}/libQFsound.so.*
%attr(755,root,root)%{_libdir}/libQFutil.so.*
%attr(755,root,root)%{_libdir}/%{name}/libcd_null.so*
%attr(755,root,root)%{_libdir}/%{name}/libconsole_client.so*
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_disk.so*
%attr(755,root,root)%{_libdir}/%{name}/libsnd_render_default.so*
%{_datadir}/games/%{name}/id1/menu.dat*
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*

%files cd-linux
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/libcd_linux.so*

%files cd-sdl
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/libcd_sdl.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/qfcc
%attr(755,root,root)%{_libdir}/libQFcd.so
%attr(755,root,root)%{_libdir}/libQFcd.la
%attr(755,root,root)%{_libdir}/libQFconsole.so
%attr(755,root,root)%{_libdir}/libQFconsole.la
%attr(755,root,root)%{_libdir}/libQFcsqc.so
%attr(755,root,root)%{_libdir}/libQFcsqc.la
%attr(755,root,root)%{_libdir}/libQFgamecode.so
%attr(755,root,root)%{_libdir}/libQFgamecode.la
%attr(755,root,root)%{_libdir}/libQFgamecode_builtins.so
%attr(755,root,root)%{_libdir}/libQFgamecode_builtins.la
%attr(755,root,root)%{_libdir}/libQFjs.so
%attr(755,root,root)%{_libdir}/libQFjs.la
%attr(755,root,root)%{_libdir}/libQFmodels.so
%attr(755,root,root)%{_libdir}/libQFmodels.la
%attr(755,root,root)%{_libdir}/libQFmodels_gl.so
%attr(755,root,root)%{_libdir}/libQFmodels_gl.la
%attr(755,root,root)%{_libdir}/libQFrenderer_gl.so
%attr(755,root,root)%{_libdir}/libQFrenderer_gl.la
%attr(755,root,root)%{_libdir}/libQFmodels_sw.so
%attr(755,root,root)%{_libdir}/libQFmodels_sw.la
%attr(755,root,root)%{_libdir}/libQFrenderer_sw32.so
%attr(755,root,root)%{_libdir}/libQFrenderer_sw32.la
%attr(755,root,root)%{_libdir}/libQFsound.so
%attr(755,root,root)%{_libdir}/libQFsound.la
%attr(755,root,root)%{_libdir}/libQFutil.so
%attr(755,root,root)%{_libdir}/libQFutil.la
%attr(755,root,root)%{_libdir}/%{name}/libcd_linux.la
%attr(755,root,root)%{_libdir}/%{name}/libcd_null.la
%attr(755,root,root)%{_libdir}/%{name}/libcd_sdl.la
%attr(755,root,root)%{_libdir}/%{name}/libconsole_client.la
%attr(755,root,root)%{_libdir}/%{name}/libconsole_server.la
%{!?_without_alsa:%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_alsa0_5.la}
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_disk.la
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_oss.la
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_sdl.la
%attr(755,root,root)%{_libdir}/%{name}/libsnd_render_default.la
%attr(755,root,root)%{_includedir}/QF/GL/*.h
%attr(755,root,root)%{_includedir}/QF/*.h
%attr(755,root,root)%{_includedir}/QF/plugin/*.h
%{_mandir}/man1/qfcc.1*

%files fbdev
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/*fbdev

%files glx
%defattr(644,root,root,755)
%attr(755,root,root)%{_xbindir}/*glx
%{_applnkdir}/Games/*glx.desktop

%files libs-gl
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/libQFmodels_gl.so.*
%attr(755,root,root)%{_libdir}/libQFrenderer_gl.so.*

%files libs-sw
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/libQFmodels_sw.so.*
%attr(755,root,root)%{_libdir}/libQFrenderer_sw32.so.*

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root)%{_xbindir}/*sdl
%{_applnkdir}/Games/*sdl.desktop

%files sdl32
%defattr(644,root,root,755)
%attr(755,root,root)%{_xbindir}/*sdl32
%{_applnkdir}/Games/*sdl32.desktop

%files servers
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/qw-server
%attr(755,root,root)%{_bindir}/nq-server
%attr(755,root,root)%{_bindir}/qw-master
%attr(755,root,root)%{_libdir}/%{name}/libconsole_server.so*
%attr(754,root,root)%{_sysconfdir}/rc.d/init.d/*

%files sgl
%defattr(644,root,root,755)
%attr(755,root,root)%{_xbindir}/*sgl
%{_applnkdir}/Games/*sgl.desktop

%if %{!?_without_alsa:1}%{?_without_alsa:0}
%files snd-alsa
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_alsa0_5.so*
%endif

%files snd-oss
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_oss.so*

%files snd-sdl
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_sdl.so*

%files static
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/libQFcd.a
%attr(755,root,root)%{_libdir}/libQFconsole.a
%attr(755,root,root)%{_libdir}/libQFcsqc.a
%attr(755,root,root)%{_libdir}/libQFgamecode.a
%attr(755,root,root)%{_libdir}/libQFgamecode_builtins.a
%attr(755,root,root)%{_libdir}/libQFjs.a
%attr(755,root,root)%{_libdir}/libQFmodels.a
%attr(755,root,root)%{_libdir}/libQFmodels_gl.a
%attr(755,root,root)%{_libdir}/libQFrenderer_gl.a
%attr(755,root,root)%{_libdir}/libQFmodels_sw.a
%attr(755,root,root)%{_libdir}/libQFrenderer_sw32.a
%attr(755,root,root)%{_libdir}/libQFsound.a
%attr(755,root,root)%{_libdir}/libQFutil.a
%attr(755,root,root)%{_libdir}/%{name}/libcd_linux.a
%attr(755,root,root)%{_libdir}/%{name}/libcd_null.a
%attr(755,root,root)%{_libdir}/%{name}/libcd_sdl.a
%attr(755,root,root)%{_libdir}/%{name}/libconsole_client.a
%attr(755,root,root)%{_libdir}/%{name}/libconsole_server.a
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_alsa0_5.a
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_disk.a
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_oss.a
%attr(755,root,root)%{_libdir}/%{name}/libsnd_output_sdl.a
%attr(755,root,root)%{_libdir}/%{name}/libsnd_render_default.a

%{?!_without_svga:%files svga}
%{?!_without_svga:%defattr(644,root,root,755)}
%{?!_without_svga:%attr(755,root,root)%{_bindir}/*svga}

%files utils
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/pak
%attr(755,root,root)%{_bindir}/qfprogs
%{_mandir}/man1/pak.1*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root)%{_xbindir}/*x11
%{_applnkdir}/Games/*x11.desktop
