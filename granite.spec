%define api		1.0
%define major		7
%define libname		%mklibname %{name}
%define oldlibname		%mklibname %{name} 7
%define girgranitename	%mklibname %{name}-gir
%define oldgirgranitename	%mklibname %{name}-gir 1.0
%define develname	%mklibname %{name} -d

Name:		granite
Summary:	elementary companion library for GTK+ and GLib
Version:	7.5.0
Release:	1
License:	LGPLv3+
Group:		System/Libraries
URL:		https://github.com/elementary/granite
Source0:	https://github.com/elementary/granite/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:  meson
BuildRequires:	gettext
BuildRequires:	vala >= 0.40
BuildRequires:  sassc
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

# granite provides and needs some generic icons
Requires:	hicolor-icon-theme

%description
Granite is a companion library for GTK+ and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary.

#------------------------------------------------

%package -n	%{libname}
Summary:	elementary companion library for GTK+ and GLib
Group:		System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
Granite is a companion library for GTK+ and GLib. Among other things, it
provides complex widgets and convenience functions designed for use in
apps built for elementary.

#------------------------------------------------

%package -n	%{girgranitename}
Summary:	GObject Introspection interface description for Granite
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
%rename %{oldgirgranitename}

%description -n	%{girgranitename}
GObject Introspection interface description for Granite.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girgranitename} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1

#Fix broken requires on gir package
sed -i "s|@PLAINNAME@|libgranite-7.so.%{major}|" lib/meson.build

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}-%{major}

%files -f %{name}-%{major}.lang
%doc README.md
%license COPYING
%{_bindir}/granite-7-demo
%{_datadir}/applications/io.elementary.granite-%{major}.demo.desktop
%{_datadir}/metainfo/granite-%{major}.appdata.xml
#{_iconsdir}/hicolor/*/actions/appointment.svg
#{_iconsdir}/hicolor/*/actions/open-menu.svg
#{_iconsdir}/hicolor/scalable/actions/open-menu-symbolic.svg

%files -n %{libname}
%doc README.md
%{_libdir}/lib%{name}-%{major}.so.%{major}{,.*}

%files -n %{girgranitename}
%doc README.md
%{_libdir}/girepository-%{api}/Granite-%{major}.0.typelib

%files -n %{develname}
%doc README.md
%{_includedir}/granite-%{major}/granite-7.h
%{_libdir}/lib%{name}-%{major}.so
%{_libdir}/pkgconfig/%{name}-%{major}.pc
%{_datadir}/gir-%{api}/Granite-%{major}.0.gir
%{_datadir}/vala/vapi/granite-%{major}.deps
%{_datadir}/vala/vapi/granite-%{major}.vapi
