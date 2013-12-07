# revision 28628
# category Package
# catalog-ctan /fonts/go
# catalog-date 2012-05-17 22:49:03 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-go
Version:	20120517
Release:	4
Summary:	Fonts and macros for typesetting go games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/go
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/go.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/go.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/go.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros provide for nothing more complicated than the
standard 19x19 board; the fonts are written in Metafont.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/go/go.mf
%{_texmfdistdir}/fonts/source/public/go/go10.mf
%{_texmfdistdir}/fonts/source/public/go/go15.mf
%{_texmfdistdir}/fonts/source/public/go/go1bla10.mf
%{_texmfdistdir}/fonts/source/public/go/go1bla15.mf
%{_texmfdistdir}/fonts/source/public/go/go1bla20.mf
%{_texmfdistdir}/fonts/source/public/go/go1black.mf
%{_texmfdistdir}/fonts/source/public/go/go1whi10.mf
%{_texmfdistdir}/fonts/source/public/go/go1whi15.mf
%{_texmfdistdir}/fonts/source/public/go/go1whi20.mf
%{_texmfdistdir}/fonts/source/public/go/go1white.mf
%{_texmfdistdir}/fonts/source/public/go/go20.mf
%{_texmfdistdir}/fonts/source/public/go/go2bla10.mf
%{_texmfdistdir}/fonts/source/public/go/go2bla15.mf
%{_texmfdistdir}/fonts/source/public/go/go2bla20.mf
%{_texmfdistdir}/fonts/source/public/go/go2black.mf
%{_texmfdistdir}/fonts/source/public/go/go2whi10.mf
%{_texmfdistdir}/fonts/source/public/go/go2whi15.mf
%{_texmfdistdir}/fonts/source/public/go/go2whi20.mf
%{_texmfdistdir}/fonts/source/public/go/go2white.mf
%{_texmfdistdir}/fonts/source/public/go/gosign50.mf
%{_texmfdistdir}/fonts/tfm/public/go/go10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1bla10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1bla15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1bla20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1whi10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1whi15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go1whi20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2bla10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2bla15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2bla20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2whi10.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2whi15.tfm
%{_texmfdistdir}/fonts/tfm/public/go/go2whi20.tfm
%{_texmfdistdir}/fonts/tfm/public/go/gosign50.tfm
%{_texmfdistdir}/tex/latex/go/go.sty
%doc %{_texmfdistdir}/doc/fonts/go/gomaps.ltx
#- source
%doc %{_texmfdistdir}/source/fonts/go/go.bat
%doc %{_texmfdistdir}/source/fonts/go/go1.bat

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
