Name:		texlive-multibbl
Version:	15878
Release:	1
Summary:	Multiple bibliographies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multibbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
