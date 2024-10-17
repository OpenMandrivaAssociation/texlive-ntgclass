Name:		texlive-ntgclass
Version:	65522
Release:	1
Summary:	"European" versions of standard classes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ntgclass
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntgclass.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntgclass.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntgclass.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Versions of the standard LaTeX article and report classes,
rewritten to reflect a more European design, by the Dutch TeX
Users Group NTG.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ntgclass
%doc %{_texmfdistdir}/doc/latex/ntgclass
#- source
%doc %{_texmfdistdir}/source/latex/ntgclass

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
