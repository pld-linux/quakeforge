#
# Conditional build:
# _without_alsa - without ALSA
# _without_svga - without SVGAlib & 3dfx support
#
%ifarch sparc sparcv9 sparc64
%define			_without_alsa	1
%endif

%ifnarch %{ix86} alpha
%define			_without_svga	1
%endif

Summary:	3D game engine based on id Software's Quake engine
Summary(pl):	Silnik gry 3D bazuj±cy na silniku Quake id Software
Name:		quakeforge
Version:	0.5.2
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://download.sourceforge.net/quake/%{name}-%{version}.tar.bz2
Source1:	%{name}.png
Source2:	%{name}-servers.tgz
URL:		http://www.%{name}.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
%{!?_without_alsa:BuildRequires: alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	bison
BuildRequires:	nas-devel
%{!?_without_svga:BuildRequires: svgalib-devel}
BuildRequires:	texinfo
BuildRequires:	xmms-devel
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

%package devel
Summary:	QuakeForge - headers and devel libs
Summary(pl):	QuakeForge - pliki nag³ówkowe
Group:		Applications/Games
Requires:	%{name} = %{version}

%description devel
QuakeForge - headers and devel libs

%description devel -l pl
QuakeForge - pliki nag³ówkowe

%package static
Summary:	QuakeForge 3D game engine - static libraries
Summary(pl):	Silnik gry 3D QuakeForge - biblioteki statyczne
Group:		Applications/Games
Requires:	%{name}-devel = %{version}

%description static
QuakeForge 3D game engine - static libraries

%description static -l pl
Silnik gry 3D QuakeForge - biblioteki statyczne

%package servers
Summary:	QuakeForge Servers
Summary(pl):	Serwery QuakeForge
Group:		Applications/Games
Requires:	%{name} = %{version}

%description servers
QuakeForge Servers.

%description servers -l pl
Serwery QuakeForge.

%package utils
Summary:	QuakeForge - utility programs
Summary(pl):	QuakeForge - programy narzêdziowe
Group:		Applications/Games
Requires:	%{name} = %{version}

%description utils
QuakeForge - utility programs.

%description utils -l pl
QuakeForge - programy narzêdziowe.

%package 3dfx
Summary:	QuakeForge client for 3dfx
Summary(pl):	Klient QuakeForge pod 3dfx
Group:		Applications/Games
Requires:	%{name}-libs-gl = %{version}

%description 3dfx
Quakeforge client for 3dfx device.

%description 3dfx -l pl
Klient QuakeForge pod 3dfx.

%package fbdev
Summary:	QuakeForge client for fbdev
Summary(pl):	Klient QuakeForge pod fbdev
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}

%description fbdev
Quakeforge client for framebuffer device.

%description fbdev -l pl
Klient QuakeForge pod framebuffer.

%package glx
Summary:	QuakeForge glx client
Summary(pl):	Klient QuakeForge glx
Group:		Applications/Games
Requires:	%{name}-libs-gl = %{version}

%description  glx
Quakeforge client for X Window that uses OpenGL through GLX extension.

%description glx -l pl
Klient QuakeForge pod X Window u¿ywaj±cy OpenGL poprzez rozszerzenie
GLX.

%package sdl
Summary:	QuakeForge client for SDL with 8-bit color
Summary(pl):	Klient QuakeForge pod SDL z 8-bitowym kolorem
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}

%description  sdl
Quakeforge client for SDL with 8-bit color.

%description sdl -l pl
Klient QuakeForge pod SDL z 8-bitowym kolorem.

%package sdl32
Summary:	QuakeForge client for SDL with various color depths support
Summary(pl):	Klient QuakeForge pod SDL z obs³ug± ró¿nych g³êbi kolorów
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}

%description sdl32
Quakeforge client for SDL with various color depths support (8, 16,
32-bit).

%description sdl32 -l pl
Klient QuakeForge pod SDL z obs³ug± ró¿nych g³êbi kolorów (8, 16 i
32-bitowej).

%package sgl
Summary:	QuakeForge client for SDL with GL
Summary(pl):	Klient QuakeForge pod SDL z obs³ug± GL
Group:		Applications/Games
Requires:	%{name}-libs-gl = %{version}

%description sgl
QuakeForge client for SDL that uses OpenGL through SDL.

%description sgl -l pl
Klient QuakeForge pod SDL, u¿ywaj±cy OpenGL za po¶rednictwem SDL.

%package svga
Summary:	QuakeForge client for svgalib
Summary(pl):	Klient QuakeForge pod svgalib
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}
Obsoletes:	%{name}-svgalib

%description  svga
Quakeforge client for svgalib.

%description svga -l pl
Klient QuakeForge pod svgalib.

%package x11
Summary:	QuakeForge client for x11
Summary(pl):	Klient QuakeForge pod x11
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}

%description x11
Quakeforge client for x11.

%description x11 -l pl
Klient QuakeForge pod x11.

%package cd-linux
Summary:	QuakeForge - Linux CD plugin
Summary(pl):	QuakeForge - wtyczka CD dla Linuksa
Group:		Applications/Games
Requires:	%{name} = %{version}

%description cd-linux
QuakeForge - native Linux CD plugin.

%description cd-linux -l pl
QuakeForge - wtyczka CD u¿ywaj±ca mechanizmów charakterystycznych dla
Linuksa.

%package cd-sdl
Summary:	QuakeForge - SDL CD plugin
Summary(pl):	QuakeForge - wtyczka CD dla SDL
Group:		Applications/Games
Requires:	%{name} = %{version}

%description cd-sdl
QuakeForge - CD plugin that uses SDL to access drive.

%description cd-sdl -l pl
QuakeForge - wtyczka CD odwo³uj±ca siê do odtwarzacza poprzez SDL.

%package cd-xmms
Summary:	QuakeForge - xmms CD plugin
Summary(pl):	QuakeForge - wtyczka CD dla xmms
Group:		Applications/Games
Requires:	%{name} = %{version}

%description cd-xmms
QuakeForge - CD plugin that uses xmms to access drive.

%description cd-xmms -l pl
QuakeForge - wtyczka CD odwo³uj±ca siê do odtwarzacza poprzez xmms.

%package libs-gl
Summary:	QuakeForge - OpenGL renderer libraries
Summary(pl):	QuakeForge - biblioteki renderujace OpenGL
Group:		Applications/Games
Requires:	%{name} = %{version}
Requires:	OpenGL

%description libs-gl
QuakeForge - OpenGL renderer libraries.

%description libs-gl -l pl
QuakeForge - biblioteki renderuj±ce z u¿yciem OpenGL.

%package libs-sw
Summary:	QuakeForge - Software renderer libraries
Summary(pl):	QuakeForge - biblioteki do renderowania programowego
Group:		Applications/Games
Requires:	%{name} = %{version}

%description libs-sw
QuakeForge - Software renderer libraries.

%description libs-sw -l pl
QuakeForge - biblioteki do renderowania programowego.

%package snd-alsa
Summary:	ALSA sound plugin for QuakeForge
Summary(pl):	Wtyczka d¼wiêkowa ALSA dla QuakeForge
Group:		Applications/Games
Requires:	%{name} = %{version}

%description snd-alsa
The ALSA plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%description snd-alsa -l pl
Wtyczka ALSA dla QuakeForge udostêpnia cyfrowe wyj¶cie d¼wiêku dla
klientów gry.

%package snd-oss
Summary:	OSS sound plugin for QuakeForge
Summary(pl):	Wtyczka d¼wiêkowa OSS dla QuakeForge
Group:		Applications/Games
Requires:	%{name} = %{version}

%description snd-oss
The OSS plugin for QuakeForge provides digital audio output (using
OSS/Linux, OSS/Free, or kernel sound) for QuakeForge targets that
contain clients.

NOTE: This plugin does not work on all systems, since it uses
memory-mapped I/O for the output device. If you have trouble, try the
%{name}-snd-alsa package.

%description snd-oss -l pl
Wtyczka OSS dla QuakeForge udostêpnia cyfrowe wyj¶cie d¼wieku
(u¿ywaj±ce OSS/Linux, OSS/Free lub obs³ugi d¼wiêku wkompilowanej w
kernel) dla klientów gry.

UWAGA: Ta wtyczka nie dzia³a na wszystkich systemach, gdy uzywaj± one
mapowanego w pamiêci I/O dla urz±dzenia wyj¶ciowego. Je¶li masz z ni±
k³opoty - spróbuj u¿yæ pakietu %{name}-snd-alsa.

%package snd-sdl
Summary:	SDL sound plugin for QuakeForge
Summary(pl):	Wtyczka d¼wiêkowa SDL dla QuakeForge
Group:		Applications/Games
Requires:	%{name} = %{version}

%description snd-sdl
The SDL plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%description snd-sdl -l pl
Wtyczka SDL dla QuakeForge udostêpnia cyfrowe wyj¶cie d¼wiêku dla
klientów gry.

%prep
%setup -q

%build
# --without-arch not to override -march passed by %%configure
%configure \
	--with-x \
	--without-arch \
	--enable-vidmode \
	--enable-dga \
	--with-plugin-path=%{_libdir}/%{name} \
	--with-global-cfg="%{_sysconfdir}/%{name}/%{name}.conf" \
	--with-user-cfg="~/.%{name}/%{name}.conf" \
	%{?_without_svga:--disable-3dfx} \
	%{?_without_alsa:--disable-alsa} \
	%{?_without_svga:--without-svga}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,%{name}},%{_datadir}/games/%{name}/qw} \
	$RPM_BUILD_ROOT{%{_xbindir},%{_pixmapsdir},%{_applnkdir}/Games}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%ifnarch ppc
mv $RPM_BUILD_ROOT{%{_bindir}/{%{?!_without_3dfx:*3dfx,}*glx,*sdl*,*sgl,*x11},%{_xbindir}}
%else
mv $RPM_BUILD_ROOT{%{_bindir}/{*glx,*sdl*,*sgl,*x11},%{_xbindir}}
%endif

install  %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
cp RPM/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/qw-server.cfg
echo "map e1m3" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/nq-server.cfg

cd $RPM_BUILD_ROOT%{_datadir}/games/%{name}/qw
ln -sf %{_sysconfdir}/%{name}/qw-server.cfg server.cfg
cd -

cd $RPM_BUILD_ROOT/etc/rc.d/init.d
tar zxfv %{SOURCE2}
cd -

qfver="%{?!_without_3dfx:3dfx }glx sdl sdl32 sgl x11"

for f in $qfver; do
	desktopfile="$RPM_BUILD_ROOT%{_applnkdir}/Games/qw-client-$f.desktop"
	echo "[Desktop Entry]\nName=QuakeWorld ($f)\nExec=qw-client-$f \
	\nIcon=%{name}.png\nTerminal=0\nType=Application" > $desktopfile

	desktopfile="$RPM_BUILD_ROOT%{_applnkdir}/Games/nq-$f.desktop"
	echo "[Desktop Entry]\nName=Quake ($f)\nExec=nq-$f \
	\nIcon=%{name}.png\nTerminal=0\nType=Application" > $desktopfile
done

cp doc/man/%{name}* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

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
%doc NEWS TODO ChangeLog doc/[!Mm]*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/%{name}.conf
%attr(755,root,root) %{_libdir}/libQFcd.so.*
%attr(755,root,root) %{_libdir}/libQFconsole.so.*
%attr(755,root,root) %{_libdir}/libQFcsqc.so.*
%attr(755,root,root) %{_libdir}/libQFgamecode.so.*
%attr(755,root,root) %{_libdir}/libQFgamecode_builtins.so.*
%attr(755,root,root) %{_libdir}/libQFjs.so.*
%attr(755,root,root) %{_libdir}/libQFmodels.so.*
%attr(755,root,root) %{_libdir}/libQFsound.so.*
%attr(755,root,root) %{_libdir}/libQFutil.so.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/cd_null.so*
%attr(755,root,root) %{_libdir}/%{name}/console_client.so*
%attr(755,root,root) %{_libdir}/%{name}/snd_output_disk.so*
%attr(755,root,root) %{_libdir}/%{name}/snd_output_null.so*
%attr(755,root,root) %{_libdir}/%{name}/snd_render_default.so*
%dir %{_datadir}/games/%{name}
%dir %{_datadir}/games/%{name}/id1
%{_datadir}/games/%{name}/id1/game.dat*
%{_datadir}/games/%{name}/id1/menu.dat*
%dir %{_datadir}/games/%{name}/qw
%{_pixmapsdir}/%{name}.png
%{_mandir}/man1/%{name}.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qfcc
%attr(755,root,root) %{_libdir}/libQFcd.so
%{_libdir}/libQFcd.la
%attr(755,root,root) %{_libdir}/libQFconsole.so
%{_libdir}/libQFconsole.la
%attr(755,root,root) %{_libdir}/libQFcsqc.so
%{_libdir}/libQFcsqc.la
%attr(755,root,root) %{_libdir}/libQFgamecode.so
%{_libdir}/libQFgamecode.la
%attr(755,root,root) %{_libdir}/libQFgamecode_builtins.so
%{_libdir}/libQFgamecode_builtins.la
%attr(755,root,root) %{_libdir}/libQFjs.so
%{_libdir}/libQFjs.la
%attr(755,root,root) %{_libdir}/libQFmodels.so
%{_libdir}/libQFmodels.la
%attr(755,root,root) %{_libdir}/libQFmodels_gl.so
%{_libdir}/libQFmodels_gl.la
%attr(755,root,root) %{_libdir}/libQFrenderer_gl.so
%{_libdir}/libQFrenderer_gl.la
%attr(755,root,root) %{_libdir}/libQFmodels_sw.so
%{_libdir}/libQFmodels_sw.la
%attr(755,root,root) %{_libdir}/libQFrenderer_sw32.so
%{_libdir}/libQFrenderer_sw32.la
%attr(755,root,root) %{_libdir}/libQFsound.so
%{_libdir}/libQFsound.la
%attr(755,root,root) %{_libdir}/libQFutil.so
%{_libdir}/libQFutil.la
%{_libdir}/%{name}/cd_linux.la
%{_libdir}/%{name}/cd_null.la
%{_libdir}/%{name}/cd_sdl.la
%{_libdir}/%{name}/cd_xmms.la
%{_libdir}/%{name}/console_client.la
%{_libdir}/%{name}/console_server.la
%{!?_without_alsa:%{_libdir}/%{name}/snd_output_alsa*.la}
%{_libdir}/%{name}/snd_output_disk.la
%{_libdir}/%{name}/snd_output_null.la
%{_libdir}/%{name}/snd_output_oss.la
%{_libdir}/%{name}/snd_output_sdl.la
%{_libdir}/%{name}/snd_render_default.la
%{_includedir}/QF
%{_mandir}/man1/qfcc.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libQFcd.a
%{_libdir}/libQFconsole.a
%{_libdir}/libQFcsqc.a
%{_libdir}/libQFgamecode.a
%{_libdir}/libQFgamecode_builtins.a
%{_libdir}/libQFjs.a
%{_libdir}/libQFmodels.a
%{_libdir}/libQFmodels_gl.a
%{_libdir}/libQFrenderer_gl.a
%{_libdir}/libQFmodels_sw.a
%{_libdir}/libQFrenderer_sw32.a
%{_libdir}/libQFsound.a
%{_libdir}/libQFutil.a
%{_libdir}/%{name}/cd_linux.a
%{_libdir}/%{name}/cd_null.a
%{_libdir}/%{name}/cd_sdl.a
%{_libdir}/%{name}/cd_xmms.a
%{_libdir}/%{name}/console_client.a
%{_libdir}/%{name}/console_server.a
%{!?_without_alsa:%{_libdir}/%{name}/snd_output_alsa*.a}
%{_libdir}/%{name}/snd_output_disk.a
%{_libdir}/%{name}/snd_output_null.a
%{_libdir}/%{name}/snd_output_oss.a
%{_libdir}/%{name}/snd_output_sdl.a
%{_libdir}/%{name}/snd_render_default.a

%files servers
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*-server.cfg
%attr(755,root,root) %{_bindir}/qw-server
%attr(755,root,root) %{_bindir}/nq-server
%attr(755,root,root) %{_bindir}/qw-master
%attr(755,root,root) %{_libdir}/%{name}/console_server.so*
%{_datadir}/games/%{name}/qw/server.cfg
%attr(754,root,root) /etc/rc.d/init.d/*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pak
%attr(755,root,root) %{_bindir}/qfbsp
%attr(755,root,root) %{_bindir}/qfdefs
%attr(755,root,root) %{_bindir}/qflight
%attr(755,root,root) %{_bindir}/qfmodelgen
%attr(755,root,root) %{_bindir}/qfprogs
%attr(755,root,root) %{_bindir}/qfvis
%attr(755,root,root) %{_bindir}/qfwavinfo
%attr(755,root,root) %{_bindir}/zpak
%{_mandir}/man1/pak.1*
%{_mandir}/man1/qflight.1*
%{_mandir}/man1/qfvis.1*
#%{_mandir}/man1/qfprogs.1*
#%{_mandir}/man1/qfwavinfo.1*

%if %{?_without_svga:0}%{!?_without_svga:1}
%files 3dfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*3dfx
%{_applnkdir}/Games/*3dfx.desktop
%endif

%files fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*fbdev

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*glx
%{_applnkdir}/Games/*glx.desktop

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*sdl
%{_applnkdir}/Games/*sdl.desktop

%files sdl32
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*sdl32
%{_applnkdir}/Games/*sdl32.desktop

%files sgl
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*sgl
%{_applnkdir}/Games/*sgl.desktop

%if %{?_without_svga:0}%{!?_without_svga:1}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*svga
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*x11
%{_applnkdir}/Games/*x11.desktop

%files cd-linux
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/cd_linux.so*

%files cd-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/cd_sdl.so*

%files cd-xmms
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/%{name}/cd_xmms.so*

%files libs-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQFmodels_gl.so.*
%attr(755,root,root) %{_libdir}/libQFrenderer_gl.so.*

%files libs-sw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQFmodels_sw.so.*
%attr(755,root,root) %{_libdir}/libQFrenderer_sw32.so.*

%if %{?_without_alsa:0}%{!?_without_alsa:1}
%files snd-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snd_output_alsa*.so*
%endif

%files snd-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snd_output_oss.so*

%files snd-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snd_output_sdl.so*
