%define upstream_name    Net-Google-Code
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simple client library for projects hosted in Google Code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::MMagic)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(HTML::TreeBuilder)
BuildRequires:	perl(JSON)
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Mock::LWP)
BuildRequires:	perl(Test::MockModule)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(WWW::Mechanize::Link)
BuildRequires:	perl(XML::FeedPP)
BuildArch:	noarch

%description
Net::Google::Code is a simple client library for projects hosted in Google
Code.

Since 0.15, Net::Google::Code offers google's official issues api support.
Besides the new 'Net::Google::Code::Issue::list',
'Net::Google::Code::Issue::Comment::list' and
<Net::Googlel::Code::Issue::load_comments> methods, which use the api from
start, you can set '$Net::Google::Code::Issue::USE_HYBRID' to true to load,
create and update issue with the api too.

But the official api is not function complete yet( e.g. no attachment
support, can't merge, etc. ), Net::Google::Code will back to the scraping
way to accomplish those stuff.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.190.0-3mdv2011.0
+ Revision: 657802
- rebuild for updated spec-helper

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.190.0-2mdv2011.0
+ Revision: 614526
- the mass rebuild of 2010.1 packages

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.190.0-1mdv2010.1
+ Revision: 542839
- import perl-Net-Google-Code


* Wed May 05 2010 cpan2dist 0.19-1mdv
- initial mdv release, generated with cpan2dist
