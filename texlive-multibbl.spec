%global tl_name multibbl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Multiple bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/multibbl
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/multibbl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package multibbl redefines the standard bibliographic commands so
that one can generate multiple reference sections. Each section has it
own auxiliary file (for use with BibTeX) and title.

