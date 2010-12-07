%define upstream_name    Net-Google-Code
%define upstream_version 0.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Simple client library for projects hosted in Google Code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(DateTime)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::MMagic)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(HTML::TreeBuilder)
BuildRequires: perl(JSON)
BuildRequires: perl(MIME::Types)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::Mock::LWP)
BuildRequires: perl(Test::MockModule)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(WWW::Mechanize::Link)
BuildRequires: perl(XML::FeedPP)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


