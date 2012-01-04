# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/qstest
# catalog-date 2008-08-24 10:50:19 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-qstest
Version:	20080824
Release:	2
Summary:	Bundle for unit tests and pattern matching
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/qstest
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qstest.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qstest.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qstest.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is the public release of the qstest bundle (written for
DocScape Publisher) (C) 2006, 2007 QuinScape GmbH. The bundle
contains the packages 'makematch' for matching patterns to
targets (with a generalization in the form of pattern lists and
keyword lists), and 'qstest' for performing unit tests,
allowing the user to run a number of logged tests ensuring the
consistency of values, properties and call sequences during
execution of test code. Both packages make extensive use of in
their package documentation, providing illustrated examples
that are automatically verified to work as expected. Check the
README file for details.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/qstest/makematch.sty
%{_texmfdistdir}/tex/latex/qstest/qstest.sty
%doc %{_texmfdistdir}/doc/latex/qstest/README
%doc %{_texmfdistdir}/doc/latex/qstest/makematch-qs.tex
%doc %{_texmfdistdir}/doc/latex/qstest/makematch.pdf
%doc %{_texmfdistdir}/doc/latex/qstest/qstest-qs.tex
%doc %{_texmfdistdir}/doc/latex/qstest/qstest.pdf
#- source
%doc %{_texmfdistdir}/source/latex/qstest/Makefile
%doc %{_texmfdistdir}/source/latex/qstest/makematch.drv
%doc %{_texmfdistdir}/source/latex/qstest/makematch.dtx
%doc %{_texmfdistdir}/source/latex/qstest/qstest.drv
%doc %{_texmfdistdir}/source/latex/qstest/qstest.dtx
%doc %{_texmfdistdir}/source/latex/qstest/qstest.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
