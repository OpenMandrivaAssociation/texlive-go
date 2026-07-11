%global tl_name go
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts and macros for typesetting go games
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/go
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/go.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/go.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/go.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The macros provide for nothing more complicated than the standard 19x19
board; the fonts are written in Metafont.

