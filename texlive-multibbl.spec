# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/multibbl
# catalog-date 2007-05-25 16:15:27 +0200
# catalog-license lppl
# catalog-version v1.1
Name:		texlive-multibbl
Version:	v1.1
Release:	1
Summary:	Multiple bibliographies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multibbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package multibbl redefines the standard bibliographic
commands so that one can generate multiple reference sections.
Each section has it own auxiliary file (for use with BibTeX)
and title.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multibbl/multibbl.sty
%doc %{_texmfdistdir}/doc/latex/multibbl/multibbl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/multibbl/multibbl.dtx
%doc %{_texmfdistdir}/source/latex/multibbl/multibbl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
