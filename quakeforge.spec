Summary:	3D game engine based on id Software's Quake engine
Summary(pl):	Silnik gry 3D bazuj±cy na silniku Quake id Software
Name:		quakeforge
Version:	0.2.99beta5
Release:	1
License:	GPL
Group:		Games
Source0:	http://download.sourceforge.net/quake/%{name}-%{version}.tar.bz2 
URL:		http://www.quakeforge.net/
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	SDL-devel
BuildRequires:	svgalib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3D game engine based on id Software's Quake engine

%description -l pl
Silnik gry 3D bazuj±cy na silniku Quake id Software

%package svgalib
Summary:        quakeforge client for svgalib
Summary(pl):	klient quakeforge pod svgalib
Group:          Games

%description  svgalib
quakeforge client for svgalib

%description -l pl svgalib
klient quakeforge pod svgalib

%package sdl
Summary:        quakeforge client for SDL
Summary(pl):    klient quakeforge pod SDL
Group:          Games

%description  sdl
quakeforge client for SDL

%description -l pl sdl
klient quakeforge pod SDL

%package x11
Summary:        quakeforge client for x11
Summary(pl):    klient quakeforge pod x11
Group:          Games

%description  x11
quakeforge client for x11

%description -l pl x11
klient quakeforge pod x11

%prep
%setup  -q

%build
aclocal
automake
autoconf
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
	--disable-profile \
	--disable-debug
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/bin
install -d $RPM_BUILD_ROOT%{_datadir}/games/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
mv $RPM_BUILD_ROOT%{_bindir}/qf-client-x11	$RPM_BUILD_ROOT/usr/X11R6/bin/

gzip -9nf AUTHORS NEWS README doc/readme.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/qf-server
%{_infodir}/*.gz
%{_mandir}/man*/*.gz
%dir %{_datadir}/games/%{name}

%files svgalib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-svga

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qf-client-sdl

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/qf-client-x11
