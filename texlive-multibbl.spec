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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package multibbl redefines the standard bibliographic
commands so that one can generate multiple reference sections.
Each section has it own auxiliary file (for use with BibTeX)
and title.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
