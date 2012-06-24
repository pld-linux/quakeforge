#
# Conditional build:
%bcond_without	alsa		# without ALSA
%bcond_without	svga		# without SVGAlib & 3dfx support
#
%ifnarch %{ix86} alpha
%undefine	with_svga
%endif
Summary:	3D game engine based on id Software's Quake engine
Summary(pl):	Silnik gry 3D bazuj�cy na silniku Quake id Software
Name:		quakeforge
Version:	0.5.4
Release:	2
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/quake/%{name}-%{version}.tar.bz2
# Source0-md5:	63d56b50fddfe81c877e67981d4c013f
Source1:	%{name}.conf
Source2:	%{name}-servers.tgz
# Source2-md5:	e30556f153d979860bc2e3a9ed598b2b
Source3:	%{name}.png
Patch0:		%{name}-alsa.patch
Patch1:		%{name}-svga-noasm.patch
Patch2:		%{name}-libdir.patch
Patch3:		%{name}-noio.patch
URL:		http://www.quakeforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	bison
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
%{?with_svga:BuildRequires:	svgalib-devel}
BuildRequires:	xmms-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags	-ffast-math -fomit-frame-pointer

%description
3D game engine based on id Software's Quake engine.

%description -l pl
Silnik gry 3D bazuj�cy na silniku Quake id Software.

%package common
Summary:	QuakeForge - Common files
Summary(pl):	QuakeForge - pliki wsp�lne
Group:		Applications/Games
Obsoletes:	quakeforge < 0.5.2-2.20030214.2

%description common
QuakeForge is a source port of Quake and QuakeWorld, the successors to
id Software's very popular DOOM series. Its primary development goal
is to remain compatible with the original games released by id
Software while adding portability and optional extensions to enhance
gameplay.

This package contains common files for all game versions.

%description common -l pl
QuakeForge jest portem �r�de� gier Quake i QuakeWorld - sukcesor�w
bardzo popularnej serii DOOM firmy id Software. Podstawowym celem
projektu jest zachowanie zgodno�ci z oryginalnymi odpowiednikami
tych�e gier przy jednoczesnym dodaniu opcjonalnych rozszerze�
s�u��cych podniesieniu jako�ci zabawy.

Ten pakiet zawiera wsp�lne pliki dla wszystkich wersji gry.

%package devel
Summary:	QuakeForge - headers and devel libs
Summary(pl):	QuakeForge - pliki nag��wkowe
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description devel
QuakeForge - headers and devel libs

%description devel -l pl
QuakeForge - pliki nag��wkowe

%package static
Summary:	QuakeForge 3D game engine - static libraries
Summary(pl):	Silnik gry 3D QuakeForge - biblioteki statyczne
Group:		Applications/Games
Requires:	%{name}-devel = %{version}-%{release}

%description static
QuakeForge 3D game engine - static libraries

%description static -l pl
Silnik gry 3D QuakeForge - biblioteki statyczne

%package servers
Summary:	QuakeForge Servers
Summary(pl):	Serwery QuakeForge
Group:		Applications/Games
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}

%description servers
QuakeForge Servers.

%description servers -l pl
Serwery QuakeForge.

%package utils
Summary:	QuakeForge - utility programs
Summary(pl):	QuakeForge - programy narz�dziowe
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description utils
QuakeForge - utility programs.

%description utils -l pl
QuakeForge - programy narz�dziowe.

%package 3dfx
Summary:	QuakeForge client for 3dfx
Summary(pl):	Klient QuakeForge pod 3dfx
Group:		Applications/Games
Requires:	%{name}-libs-gl = %{version}-%{release}

%description 3dfx
Quakeforge client for 3dfx device.

%description 3dfx -l pl
Klient QuakeForge pod 3dfx.

%package fbdev
Summary:	QuakeForge client for fbdev
Summary(pl):	Klient QuakeForge pod fbdev
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}-%{release}

%description fbdev
Quakeforge client for framebuffer device.

%description fbdev -l pl
Klient QuakeForge pod framebuffer.

%package glx
Summary:	QuakeForge glx client
Summary(pl):	Klient QuakeForge glx
Group:		X11/Applications/Games
Requires:	%{name}-libs-gl = %{version}-%{release}

%description glx
Quakeforge client for X Window that uses OpenGL through GLX extension.

%description glx -l pl
Klient QuakeForge pod X Window u�ywaj�cy OpenGL poprzez rozszerzenie
GLX.

%package sdl
Summary:	QuakeForge client for SDL with 8-bit color
Summary(pl):	Klient QuakeForge pod SDL z 8-bitowym kolorem
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}-%{release}

%description sdl
Quakeforge client for SDL with 8-bit color.

%description sdl -l pl
Klient QuakeForge pod SDL z 8-bitowym kolorem.

%package sdl32
Summary:	QuakeForge client for SDL with various color depths support
Summary(pl):	Klient QuakeForge pod SDL z obs�ug� r�nych g��bi kolor�w
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}-%{release}

%description sdl32
Quakeforge client for SDL with various color depths support (8, 16,
32-bit).

%description sdl32 -l pl
Klient QuakeForge pod SDL z obs�ug� r�nych g��bi kolor�w (8, 16 i
32-bitowej).

%package sgl
Summary:	QuakeForge client for SDL with GL
Summary(pl):	Klient QuakeForge pod SDL z obs�ug� GL
Group:		X11/Applications/Games
Requires:	%{name}-libs-gl = %{version}-%{release}

%description sgl
QuakeForge client for SDL that uses OpenGL through SDL.

%description sgl -l pl
Klient QuakeForge pod SDL, u�ywaj�cy OpenGL za po�rednictwem SDL.

%package svga
Summary:	QuakeForge client for svgalib
Summary(pl):	Klient QuakeForge pod svgalib
Group:		Applications/Games
Requires:	%{name}-libs-sw = %{version}-%{release}
Obsoletes:	quakeforge-svgalib

%description svga
Quakeforge client for svgalib.

%description svga -l pl
Klient QuakeForge pod svgalib.

%package x11
Summary:	QuakeForge client for x11
Summary(pl):	Klient QuakeForge pod x11
Group:		X11/Applications/Games
Requires:	%{name}-libs-sw = %{version}-%{release}

%description x11
Quakeforge client for x11.

%description x11 -l pl
Klient QuakeForge pod x11.

%package cd-linux
Summary:	QuakeForge - Linux CD plugin
Summary(pl):	QuakeForge - wtyczka CD dla Linuksa
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description cd-linux
QuakeForge - native Linux CD plugin.

%description cd-linux -l pl
QuakeForge - wtyczka CD u�ywaj�ca mechanizm�w charakterystycznych dla
Linuksa.

%package cd-sdl
Summary:	QuakeForge - SDL CD plugin
Summary(pl):	QuakeForge - wtyczka CD dla SDL
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description cd-sdl
QuakeForge - CD plugin that uses SDL to access drive.

%description cd-sdl -l pl
QuakeForge - wtyczka CD odwo�uj�ca si� do odtwarzacza poprzez SDL.

%package cd-xmms
Summary:	QuakeForge - xmms CD plugin
Summary(pl):	QuakeForge - wtyczka CD dla xmms
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description cd-xmms
QuakeForge - CD plugin that uses xmms to access drive.

%description cd-xmms -l pl
QuakeForge - wtyczka CD odwo�uj�ca si� do odtwarzacza poprzez xmms.

%package libs-gl
Summary:	QuakeForge - OpenGL renderer libraries
Summary(pl):	QuakeForge - biblioteki renderujace OpenGL
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}
Requires:	OpenGL

%description libs-gl
QuakeForge - OpenGL renderer libraries.

%description libs-gl -l pl
QuakeForge - biblioteki renderuj�ce z u�yciem OpenGL.

%package libs-sw
Summary:	QuakeForge - Software renderer libraries
Summary(pl):	QuakeForge - biblioteki do renderowania programowego
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description libs-sw
QuakeForge - Software renderer libraries.

%description libs-sw -l pl
QuakeForge - biblioteki do renderowania programowego.

%package snd-alsa
Summary:	ALSA sound plugin for QuakeForge
Summary(pl):	Wtyczka d�wi�kowa ALSA dla QuakeForge
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description snd-alsa
The ALSA plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%description snd-alsa -l pl
Wtyczka ALSA dla QuakeForge udost�pnia cyfrowe wyj�cie d�wi�ku dla
klient�w gry.

%package snd-oss
Summary:	OSS sound plugin for QuakeForge
Summary(pl):	Wtyczka d�wi�kowa OSS dla QuakeForge
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description snd-oss
The OSS plugin for QuakeForge provides digital audio output (using
OSS/Linux, OSS/Free, or kernel sound) for QuakeForge targets that
contain clients.

NOTE: This plugin does not work on all systems, since it uses
memory-mapped I/O for the output device. If you have trouble, try the
%{name}-snd-alsa package.

%description snd-oss -l pl
Wtyczka OSS dla QuakeForge udost�pnia cyfrowe wyj�cie d�wieku
(u�ywaj�ce OSS/Linux, OSS/Free lub obs�ugi d�wi�ku wkompilowanej w
kernel) dla klient�w gry.

UWAGA: Ta wtyczka nie dzia�a na wszystkich systemach, gdy uzywaj� one
mapowanego w pami�ci I/O dla urz�dzenia wyj�ciowego. Je�li masz z ni�
k�opoty - spr�buj u�y� pakietu %{name}-snd-alsa.

%package snd-sdl
Summary:	SDL sound plugin for QuakeForge
Summary(pl):	Wtyczka d�wi�kowa SDL dla QuakeForge
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description snd-sdl
The SDL plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%description snd-sdl -l pl
Wtyczka SDL dla QuakeForge udost�pnia cyfrowe wyj�cie d�wi�ku dla
klient�w gry.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoheader}
%{__libtoolize} --automake
%{__automake}
%{__autoconf}
# --without-arch --disable-debug --disable-optimize mean only not to
# override our CFLAGS passed by %%configure
%configure \
	--with-x \
	--without-arch \
	--disable-debug \
	--disable-optimize \
	--enable-vidmode \
	--enable-dga \
	--with-plugin-path=%{_libdir}/%{name} \
	--with-sharepath=%{_datadir}/%{name} \
	--with-global-cfg="%{_sysconfdir}/%{name}/%{name}.conf" \
	--with-user-cfg="~/.%{name}/%{name}.conf" \
	--with-clients=fbdev,glx,sdl,sdl32,sgl,%{?with_svga:3dfx,svga,}x11 \
	%{!?with_alsa:--disable-alsa}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,%{name}},%{_datadir}/%{name}/qw} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

echo "map e1m3" > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/nq-server.cfg

touch $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/qw-server.cfg

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/qw
ln -sf %{_sysconfdir}/%{name}/qw-server.cfg server.cfg
cd -

cd $RPM_BUILD_ROOT/etc/rc.d/init.d
tar zxfv %{SOURCE2}
cd -

install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

qfver="glx sdl sdl32 sgl x11"

for f in $qfver; do
	desktopfile="$RPM_BUILD_ROOT%{_desktopdir}/qw-client-$f.desktop"
	cat >$desktopfile <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=QuakeWorld ($f)
Comment=QuakeWorld client ($f version)
Comment[pl]=Klient QuakeWorld (w wersji $f)
Exec=qw-client-$f
Icon=%{name}.png
Terminal=false
Type=Application
Categories=Game;FirstPersonGame;
EOF
	desktopfile="$RPM_BUILD_ROOT%{_desktopdir}/nq-$f.desktop"
	cat >$desktopfile <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Quake ($f)
Exec=nq-$f
Icon=%{name}.png
Terminal=false
Type=Application
Categories=Game;FirstPersonGame;
EOF
done

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{la,a}

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

%files common
%defattr(644,root,root,755)
%doc NEWS TODO ChangeLog doc/[!Mm]*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/%{name}.conf
%attr(755,root,root) %{_libdir}/libQFcd.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFconsole.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFcsqc.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFgamecode.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFgamecode_builtins.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFgib.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFjs.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFmodels.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFsound.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFutil.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/console_client.so
%attr(755,root,root) %{_libdir}/%{name}/snd_output_disk.so
%attr(755,root,root) %{_libdir}/%{name}/snd_render_default.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/qw
%{_datadir}/%{name}/QF
%{_pixmapsdir}/%{name}.png

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
%attr(755,root,root) %{_libdir}/libQFgib.so
%{_libdir}/libQFgib.la
%attr(755,root,root) %{_libdir}/libQFjs.so
%{_libdir}/libQFjs.la
%attr(755,root,root) %{_libdir}/libQFmodels.so
%{_libdir}/libQFmodels.la
%attr(755,root,root) %{_libdir}/libQFmodels_gl.so
%{_libdir}/libQFmodels_gl.la
%attr(755,root,root) %{_libdir}/libQFmodels_sw.so
%{_libdir}/libQFmodels_sw.la
%attr(755,root,root) %{_libdir}/libQFrenderer_gl.so
%{_libdir}/libQFrenderer_gl.la
%attr(755,root,root) %{_libdir}/libQFrenderer_sw32.so
%{_libdir}/libQFrenderer_sw32.la
%attr(755,root,root) %{_libdir}/libQFsound.so
%{_libdir}/libQFsound.la
%attr(755,root,root) %{_libdir}/libQFutil.so
%{_libdir}/libQFutil.la
%{_includedir}/QF
%{_mandir}/man1/qfcc.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libQFcd.a
%{_libdir}/libQFconsole.a
%{_libdir}/libQFcsqc.a
%{_libdir}/libQFgamecode.a
%{_libdir}/libQFgamecode_builtins.a
%{_libdir}/libQFgib.a
%{_libdir}/libQFjs.a
%{_libdir}/libQFmodels.a
%{_libdir}/libQFmodels_gl.a
%{_libdir}/libQFrenderer_gl.a
%{_libdir}/libQFmodels_sw.a
%{_libdir}/libQFrenderer_sw32.a
%{_libdir}/libQFsound.a
%{_libdir}/libQFutil.a
%{_libdir}/ruamoko

%files servers
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*-server.cfg
%attr(755,root,root) %{_bindir}/hw-master
%attr(755,root,root) %{_bindir}/qw-master
%attr(755,root,root) %{_bindir}/qw-server
%attr(755,root,root) %{_bindir}/nq-server
%attr(755,root,root) %{_libdir}/%{name}/console_server.so
%{_datadir}/%{name}/qw/server.cfg
%attr(754,root,root) /etc/rc.d/init.d/*-[!m]*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pak
%attr(755,root,root) %{_bindir}/bsp2img
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

%if %{with svga}
%files 3dfx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*3dfx
%endif

%files fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*fbdev

%files glx
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*glx
%{_desktopdir}/*glx.desktop

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*sdl
%{_desktopdir}/*sdl.desktop

%files sdl32
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*sdl32
%{_desktopdir}/*sdl32.desktop

%files sgl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*sgl
%{_desktopdir}/*sgl.desktop

%if %{with svga}
%files svga
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*svga
%endif

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*x11
%{_desktopdir}/*x11.desktop

%files cd-linux
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/cd_linux.so

%files cd-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/cd_sdl.so

%files cd-xmms
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/cd_xmms.so

%files libs-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQFmodels_gl.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFrenderer_gl.so.*.*.*

%files libs-sw
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQFmodels_sw.so.*.*.*
%attr(755,root,root) %{_libdir}/libQFrenderer_sw32.so.*.*.*

%if %{with alsa}
%files snd-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snd_output_alsa*.so
%endif

%files snd-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snd_output_oss.so

%files snd-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/snd_output_sdl.so
