# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ntgclass
# catalog-date 2006-12-05 17:23:05 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-ntgclass
Version:	20061205
Release:	8
Summary:	"European" versions of standard classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ntgclass
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntgclass.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntgclass.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntgclass.source.tar.xz
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
%{_texmfdistdir}/tex/latex/ntgclass/a4.sty
%{_texmfdistdir}/tex/latex/ntgclass/artikel1.cls
%{_texmfdistdir}/tex/latex/ntgclass/artikel2.cls
%{_texmfdistdir}/tex/latex/ntgclass/artikel3.cls
%{_texmfdistdir}/tex/latex/ntgclass/boek.cls
%{_texmfdistdir}/tex/latex/ntgclass/boek3.cls
%{_texmfdistdir}/tex/latex/ntgclass/brief.cls
%{_texmfdistdir}/tex/latex/ntgclass/ntg10.clo
%{_texmfdistdir}/tex/latex/ntgclass/ntg11.clo
%{_texmfdistdir}/tex/latex/ntgclass/ntg12.clo
%{_texmfdistdir}/tex/latex/ntgclass/rapport1.cls
%{_texmfdistdir}/tex/latex/ntgclass/rapport3.cls
%doc %{_texmfdistdir}/doc/latex/ntgclass/00readme.txt
%doc %{_texmfdistdir}/doc/latex/ntgclass/a4.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/artdoc.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/artdoc.tex
%doc %{_texmfdistdir}/doc/latex/ntgclass/brief.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/brief.tex
%doc %{_texmfdistdir}/doc/latex/ntgclass/briefdoc.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/briefdoc.tex
%doc %{_texmfdistdir}/doc/latex/ntgclass/catalog.txt
%doc %{_texmfdistdir}/doc/latex/ntgclass/changes.txt
%doc %{_texmfdistdir}/doc/latex/ntgclass/classdoc.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/classdoc.tex
%doc %{_texmfdistdir}/doc/latex/ntgclass/manifest.txt
%doc %{_texmfdistdir}/doc/latex/ntgclass/ntgclass.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/rapdoc.pdf
%doc %{_texmfdistdir}/doc/latex/ntgclass/rapdoc.tex
#- source
%doc %{_texmfdistdir}/source/latex/ntgclass/a4.dtx
%doc %{_texmfdistdir}/source/latex/ntgclass/a4.ins
%doc %{_texmfdistdir}/source/latex/ntgclass/brief.dtx
%doc %{_texmfdistdir}/source/latex/ntgclass/ntgclass.dtx
%doc %{_texmfdistdir}/source/latex/ntgclass/ntgclass.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061205-2
+ Revision: 754444
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061205-1
+ Revision: 719138
- texlive-ntgclass
- texlive-ntgclass
- texlive-ntgclass
- texlive-ntgclass

