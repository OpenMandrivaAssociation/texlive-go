# revision 15878
# category Package
# catalog-ctan /fonts/go
# catalog-date 2010-02-19 00:25:14 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-go
Version:	20100219
Release:	2
Summary:	Fonts and macros for typesetting go games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/go
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/go.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/go.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The macros provide for nothing more complicated than the
standard 19x19 board; the fonts are written in MetaFont.

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
#- source
%doc %{_texmfdistdir}/source/latex/go/gomaps.ltx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex source %{buildroot}%{_texmfdistdir}
